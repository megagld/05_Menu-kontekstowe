#bmystek
import os
import pdfplumber
import pymsgbox

input_dir = os.getcwd()

# wsp cale/mm = 0,352 - do przeliczenia wymiarów na wartości przesunięć
wsp=0.352

file_count=0
area_count=0

for path,_,files in os.walk(input_dir):
    for pdf_file in files:
        if pdf_file.endswith(".pdf"):
            y = '{}\\{}'.format(path,pdf_file)
            with pdfplumber.open(y) as pdf:
                if len(pdf.pages)>1:continue
                else:
                    page_1 = pdf.pages[0]
                    height, width = page_1.height*wsp, page_1.width*wsp

                    file_count+=1
                    area=height*width
                    area_count+=area
                
                    with open("{}\{}.txt".format(input_dir,'powierzchnie'), 'a', encoding="utf-8") as file:
                        file.write('{} - {}; h={}; w={}; a={}\n'.format(file_count,pdf_file,int(height),int(width),round(area)))

with open("{}\{}.txt".format(input_dir,'powierzchnie'), 'a', encoding="utf-8") as file:
    file.write('Sumaryczne powierzchnia: {} m2'.format(area_count))
    file.write('Liczba rysunków: {} szt.'.format(file_count))

pymsgbox.alert(text='Pików: {} szt., Powierzchnia: {} m2'.format(file_count,round(area_count/10**6,1)), title='{}'.format('test'), button='OK')
