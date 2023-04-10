#bmystek
import os
import io
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import shutil
import tkinter as tk
import winsound
import regex as re
import time
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window
        row_c=14
        row_height=25
        cols=[350,100]
        prop=cols[0]//cols[1]

        root_width=sum(cols)
        root_height=row_c*row_height

        # root = tk.Tk()
        self.geometry('{}x{}'.format(root_width,root_height))
        self.title('Oznacz pdfy "Do realizacji"')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=prop)
        self.columnconfigure(1, weight=1)

        self.create_widgets()

    def run(self):    
        self.copy_folders()
        self.count_files()

        # pobiera dane z okienek
        tekst =     self.entry_state[1].get()
        wym_rys =   self.entry_state[3].get()
        wym_opis =  self.entry_state[4].get()
        alt_name =  self.entry_state[7].get()
        wym_alt =   self.entry_state[8].get()

        # wsp cale/mm = 0,352 - do przeliczenia wymiarów na wartości przesunięć
        wsp=0.352

        delta_rys=[int(float(i)/wsp) for i in wym_rys.split('x')]
        delta_opis=[int(float(i)/wsp) for i in wym_opis.split('x')]
        delta_alt=[int(float(i)/wsp) for i in wym_alt.split('x')]

        # ustala labele do aktualizacji
        self.done=self.entry_state[12]
        self.done_time=self.entry_state[13]
        self.all=self.entry_state[14]

        self.done_text=self.texts_state[12]
        self.done_time_text=self.texts_state[13]
        self.all_text=self.texts_state[14]

        self.last=self.texts_state[15]

        self.act_labs=[self.done,
                  self.done_time,
                  self.all,
                  self.done_text,
                  self.done_time_text,
                  self.all_text,
                  self.last]

        self.progressbar=self.entry_state[15]

        # liczniki
        self.pdf_c=0

        def make_can(pdf_w,pdf_h):
            global new_pdf
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=(int(pdf_w),int(pdf_h)))

            can.setFillColorRGB(255,0,0) #kolor czcionki
            can.setFont("Helvetica", 12) #font i jego wielkość
            can.drawString(pdf_w-cd_x,cd_y,tekst) # tekst i jego lokalizacja
            
            can.save()
            packet.seek(0)
            new_pdf = PdfReader(packet)

        self.start_time = time.time()

        for path,_,files in os.walk(self.input_dir):
            if '_do realizacji' in path:continue
            else:
                for pdf_file in files:
                    if pdf_file.endswith(".pdf"):
                        self.pdf_c+=1
                        pdf_reader = PdfReader(open('{}\\{}'.format(path, pdf_file), "rb"))
                        pdf_w,pdf_h=pdf_reader.pages[0].mediabox[-2:]

                        # odległości do prawego dolnego narożnika
                        if len(pdf_reader.pages)==1:
                            cd_x,cd_y=delta_rys #rysunki
                            # podniesienie napisu dla mniejszych tabelek(nietypowych)
                            if alt_name in pdf_file:
                                cd_x,cd_y=delta_alt
                        else:
                            cd_x,cd_y=delta_opis # opisy techniczne

                        make_can(pdf_w,pdf_h)

                        pdf_merged = pdf_reader.pages[0]
                        pdf_merged.merge_page(new_pdf.pages[0])
                        pdf_merged.compress_content_streams()
                        pdf_writer = PdfWriter()
                        
                        for i in range(len(pdf_reader.pages)):
                            if i == 0:
                                pdf_writer.add_page(pdf_merged)
                            else:
                                pdf_writer.add_page(pdf_reader.pages[i])

                        # ściażka dostępu do nowej lokalizacji pliku
                        if self.var.get()==1:
                            pdf_file=self.remove_rew(pdf_file)
                        n_file='{}\\{}'.format(path, pdf_file)[len(self.input_dir):]
                        n_file='{}\\_do realizacji{}'.format(self.input_dir,n_file)

                        with open(n_file, "wb") as output_file:
                            pdf_writer.write(output_file)

                        self.update_status(time.time())
                        # time.sleep(3)

        self.update_last()

    def create_widgets(self):
        #set labels
        texts=['',
            'Tekst:',
            'Odległość od prawego dolnego narożnika:',
            'rysunków [mm x mm]:',
            'opisów [mm x mm]:',
            '',
            'Alternatywne przesunięcie:',
            'nazwa pliku zawiera:',
            'odległość [mm x mm]:',
            '',
            'Usuń opis rewizji z nazwy pliku',
            '',
            '',
            '',
            '',
            '']
        self.texts_state={}

        for i,j in enumerate(texts):
            label = ttk.Label(self, text=j,font=('helvetica', 10))
            label.grid(column=0, row=i, sticky=tk.E, padx=5)
            self.texts_state[i]=label

        # set entry
        entrys=['',
                "DO REALIZACJI rew.000",
                '',
                '55x8',
                '75x280',
                '',
                '',
                'KPEM',
                '55x80',
                '',
                'checkbox',
                'button',
                '',
                '',
                '',
                'progresbar']
        self.entry_state={}

        for i,j in enumerate(entrys):
            if j=='':
                entry = ttk.Label(self, text=j,font=('helvetica', 10))
                entry.grid(column=0, row=i, sticky=tk.E, padx=5)
            elif j=='checkbox':
                self.var = tk.IntVar(value=1)
                entry=tk.Checkbutton(self,variable=self.var)
            elif j=='button':
                entry=tk.Button(text='Oznacz pdfy', command=self.run, bg='brown', fg='white', font=('helvetica', 10, 'bold'),width=16)
            elif j=='progresbar':
                entry=ttk.Progressbar(self, orient='horizontal',mode='determinate', length=140)
            else:
                entry = ttk.Entry(self,textvariable=j,width=22)
                entry.insert(-1, j)

            entry.grid(column=1, row=i, sticky=tk.W, padx=5)
            self.entry_state[i]=entry
        
    def copy_folders(self):

         # ***************tworzenie kopii struktury katalogów *******************

        # defining the function to ignore the files
        # if present in any folder
        def ignore_files(dir, files):
            return [f for f in files if os.path.isfile(os.path.join(dir, f))]
        
        # calling the shutil.copytree() method and
        # passing the src,dst,and ignore parameter

        self.input_dir = os.getcwd()
        self.output_dir = '{}\\{}'.format(self.input_dir,'_do realizacji')

        if not os.path.exists(self.output_dir):
            shutil.copytree(self.input_dir,
                            self.output_dir,
                            ignore=ignore_files)

        # ***************tworzenie kopii struktury katalogów *******************

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def count_files(self):
        self.files_c=0
        self.all_pdf_c=0
        for path,_,files in os.walk(self.input_dir):
            if '_do realizacji' in path:continue
            else:
                for file in files:
                    if file.endswith(".pdf"):
                        self.all_pdf_c+=1
                    self.files_c+=1

    def speed_test(self,delta_time):

        if delta_time > 60:
            minutes, seconds = delta_time // 60, delta_time % 60
            return f"{int(minutes)}min {int(seconds)}s"
        else:
            return f"{int(delta_time)}s"

    def update_status(self,end_time):
        delta_time = round(end_time - self.start_time, 3)
        # wypisuje dane o ilości plików i czasie

        self.done.config(text='{}/{}'.format(self.pdf_c,self.all_pdf_c))
        self.done_time.config(text='{} ({}s/pdf)'.format(self.speed_test(delta_time),int(delta_time/self.pdf_c)))
        self.all.config(text=str(self.files_c-self.all_pdf_c))
        self.done_text.config(text='Oznaczone pdfy:')
        self.done_time_text.config(text='W czasie:')
        self.all_text.config(text='Inne pliki w podkatalogach:')
        self.last.config(text='Pozostało ok. {}'.format(self.speed_test((self.all_pdf_c-self.pdf_c)*(delta_time/self.pdf_c))))
        self.progressbar['value']=int(100*(self.pdf_c/self.all_pdf_c))

        for i in self.act_labs:
            i.update_idletasks()

    def update_last(self):
        self.update_status(time.time())

        for i in self.act_labs:
            i.config(background='light green', font=('helvetica', 10, 'bold'))
            i.update_idletasks()
        self.last.config(text='',background='')
        self.progressbar['value']=0

        try:
            winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        except:
            pass

    def remove_rew(self,pdf_file):
        reg_pat='''(.+)([_.]rew.\d{3})(.pdf)'''
        x_match=re.match(reg_pat,pdf_file)
        if x_match:
            new_name = pdf_file.replace(x_match.group(2),'')
            return new_name
        return pdf_file

if __name__ == "__main__":
    app = App()
    app.mainloop()