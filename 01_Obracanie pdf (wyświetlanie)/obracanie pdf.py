#bmystek
from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir
import os
from pathlib import Path
import os

# input_dir = '{}{}'.format(Path(__file__).parent,'''\\''')
input_dir = os.getcwd()
output_dir = input_dir+'''\\output_pdf\\'''

Path(output_dir).mkdir(parents=True, exist_ok=True)

# Kąt obrotu
###############################################

kat=90

###############################################

for x in listdir(input_dir):
    if not x.endswith('.pdf'):
        continue
    pdf_in = open(input_dir+'\\' + x, 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    pdf_writer = PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(kat)
        pdf_writer.addPage(page)
    pdf_out = open(output_dir+'\\' + x, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()