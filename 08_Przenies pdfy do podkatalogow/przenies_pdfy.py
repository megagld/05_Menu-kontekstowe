#bmystek
import os
import shutil
import regex as re
import pymsgbox

# pobranie listy katalogów tomów opracowania

input_dir = os.getcwd()

tomy=next(os.walk(input_dir))[1]

# przenoszenie pdfów
# pdfy muszą być w katalogu _pdf

input_pdf_dir = '{}\\{}'.format(input_dir,'_pdf')

for x in os.listdir(input_pdf_dir):
    if not x.endswith('.pdf'):
        continue
    # określenie obiektu (tomu)
    tom=re.search('(\d{4,}_.*_M_)(.*?)(_.*)',x).group(2)

    # szukanie katalogu
    for i in tomy:
        if tom in i:
            pdf_from='{}\\{}\\{}'.format(input_dir,'_pdf',x)
            pdf_to='{}\\{}\\{}'.format(input_dir,i,x)
            shutil.move(pdf_from, pdf_to)

# sprawdzenie czy wszystkie pdfy zostały przeniesione

if os.listdir(input_pdf_dir):
    ad='_zostały pdfy do przeniesienia!'
    new_name=input_pdf_dir.replace('_pdf','_zostały pdfy do przeniesienia!')     
else:
    ad='_wszystkie pdfy zostały przeniesione'
new_name=input_pdf_dir.replace('_pdf',ad)

os.rename(input_pdf_dir,new_name)
pymsgbox.alert(ad)