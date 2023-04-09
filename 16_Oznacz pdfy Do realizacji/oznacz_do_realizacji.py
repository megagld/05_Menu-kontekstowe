#bmystek
import os
import io
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import shutil
import tkinter as tk
import winsound
import regex as re
from time import time

def run():    
    global tekst,new_pdf,status, label7

    # pobiera dane z okienek
    tekst =     entry_state[0].get()
    wym_rys =   entry_state[1].get()
    wym_opis =  entry_state[2].get()
    alt_name =  entry_state[3].get()
    wym_alt =   entry_state[4].get()

    # wsp cale/mm = 0,352 - do przeliczenia wymiarów na warotści przesunięć
    wsp=0.352

    delta_rys=[int(float(i)/wsp) for i in wym_rys.split('x')]
    delta_opis=[int(float(i)/wsp) for i in wym_opis.split('x')]
    delta_alt=[int(float(i)/wsp) for i in wym_alt.split('x')]

    # ***************tworzenie kopii struktury katalogów *******************

    # defining the function to ignore the files
    # if present in any folder
    def ignore_files(dir, files):
        return [f for f in files if os.path.isfile(os.path.join(dir, f))]
    
    # calling the shutil.copytree() method and
    # passing the src,dst,and ignore parameter

    input_dir = os.getcwd()
    output_dir = '{}\\{}'.format(input_dir,'_do realizacji')

    if not os.path.exists(output_dir):
        shutil.copytree(input_dir,
                        output_dir,
                        ignore=ignore_files)

    # ***************tworzenie kopii struktury katalogów *******************

    # liczniki
    pdf_c=0
    files_c=0

    folder_path = os.getcwd()
    output_folder = '{}\\_do realizacji'.format(input_dir)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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

    start_time = time()

    for path,_,files in os.walk(folder_path):
        if '_do realizacji' in path:continue
        else:
            for pdf_file in files:
                files_c+=1
                if pdf_file.endswith(".pdf"):
                    pdf_c+=1
                    pdf_reader = PdfReader(open('{}\\{}'.format(path, pdf_file), "rb"))
                    pdf_w,pdf_h=pdf_reader.pages[0].mediabox[-2:]

                    # odległości do prawego dolnego narożnika
                    # w starszym pythonie .pages na pyć Numpages?!
                    # if pdf_reader.numPages==1:
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
                    if var.get()==1:
                        pdf_file=remove_rew(pdf_file)
                    n_file='{}\\{}'.format(path, pdf_file)[len(folder_path):]
                    n_file='{}\\_do realizacji\\{}'.format(folder_path,n_file)

                    with open(n_file, "wb") as output_file:
                        pdf_writer.write(output_file)
    end_time = time()
    update_status(pdf_c,files_c-pdf_c, start_time,end_time)

def speed_test(delta_time):

    if delta_time > 60:
        minutes, seconds = delta_time // 60, delta_time % 60
        return f"{int(minutes)}min {int(seconds)}s"
    else:
        return f"{int(delta_time)}s"


def update_status(done, inn_2,start_time,end_time) :
    delta_time = round(end_time - start_time, 3)
    # wpisuje dane po zakończeniu tworzenia pdfów
    label7.config(text='{}' .format(done),bg='light green')
    label7.update_idletasks()

    label8.config(text='{} ({}s/pdf)' .format(speed_test(delta_time),int(delta_time/done)),bg='light green')
    label8.update_idletasks()

    label9.config(text=inn_2,bg='light green')
    label9.update_idletasks()

    label10.config(text='Oznaczone pdfy:',bg='light green')
    label10.update_idletasks()

    label11.config(text='W czasie:',bg='light green')
    label11.update_idletasks()

    label12.config(text='Inne pliki w podkatalogach:',bg='light green')
    label12.update_idletasks()

    try:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
    except:
        pass

def remove_rew(pdf_file):
    reg_pat='''(.+)([_.]rew.\d{3})(.pdf)'''
    x_match=re.match(reg_pat,pdf_file)
    if x_match:
        new_name = pdf_file.replace(x_match.group(2),'')
        return new_name
    return pdf_file

root= tk.Tk()

canvas1 = tk.Canvas(root, width=450, height=330, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Oznacz pdfy "Do realizacji"',anchor="c")
label1.config(font=('helvetica', 10, 'bold'),width=55,height=1)
canvas1.create_window(200, 25, window=label1)

# Wprowadzenie tekstu
opisy=['Tekst:','Odległość od prawego dolnego narożnika:',
       'rysunków [mm x mm]:',
       'opisów [mm x mm]:',
       '',
       'Alternatywne przesunięcie:',
       'nazwa pliku zawiera:',
       'odległość [mm x mm]:',
       '',
       'Usuń opis rewizji z nazwy pliku']

for i,j in enumerate(opisy):
    label = tk.Label(root, text=j,anchor="e")
    label.config(font=('helvetica', 10),width=30,height=1)
    canvas1.create_window(150, 50+i*20, window=label)

# Wprowadzenie danych

wejscia=["DO REALIZACJI rew.000",
         '56x7.5',
         '74x282',
         'KPEM',
         '56x81']
entry_state={}

for i,j in enumerate(wejscia):
    tmp=tk.Entry(root)
    tmp.insert(-1, j)
    canvas1.create_window(350, 50+20*(i+int(i>0)+2*int(i>2)), width=130, window=tmp)
    entry_state[i]=tmp

# Dodaje checkbox do usuwania rew.z nazwy pliku
var = tk.IntVar(value=1)
cbox1=tk.Checkbutton(root,  variable=var)
canvas1.create_window(300, 230, window=cbox1)

# Wprowadzenie przycisku
   
button1 = tk.Button(text='Oznacz pdfy', command=run, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(380, 230, window=button1)

# podsumowanie po zakończeniu

label7 = tk.Label(root, text='',anchor="w")
label7.config(font=('helvetica', 10, 'bold'),width=15,height=1)
canvas1.create_window(350, 270, window=label7)

label8 = tk.Label(root, text='',anchor="w")
label8.config(font=('helvetica', 10, 'bold'),width=15,height=1)
canvas1.create_window(350, 290, window=label8)

label9 = tk.Label(root, text='',anchor="w")
label9.config(font=('helvetica', 10, 'bold'),width=15,height=1)
canvas1.create_window(350, 310, window=label9)

label10 = tk.Label(root, text='',anchor="e")
label10.config(font=('helvetica', 10, 'bold'),width=30,height=1)
canvas1.create_window(150, 270, window=label10)

label11 = tk.Label(root, text='',anchor="e")
label11.config(font=('helvetica', 10, 'bold'),width=30,height=1)
canvas1.create_window(150, 290, window=label11)

label12 = tk.Label(root, text='',anchor="e")
label12.config(font=('helvetica', 10, 'bold'),width=30,height=1)
canvas1.create_window(150, 310, window=label12)

root.mainloop()
