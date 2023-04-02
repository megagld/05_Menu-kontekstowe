#!/usr/bin/env python

import os
from pdfrw import PdfReader, PdfWriter, PageMerge

def set_rot(inn, input_dir, output_dir):

    inpfn = "{}\\{}".format(input_dir,inn)
    outfn = "{}\\{}".format(output_dir,inn)

    inp = PdfReader(inpfn)
    out = PdfWriter()

    page=inp.pages[0]

    # Ustawia obrót na 0

    page.Rotate=0

    out.addpage(page)

    out.write(outfn)

# tworzy podkatalog z obóconymi pdfami
input_dir = os.getcwd()
output_dir="{}\\_wyzerowany widok".format(input_dir)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# pobiera pdfy z katalogu, ustawia obrót (Rotate) na 0 i zapisuje w podkatalogu
for i in next(os.walk(input_dir), (None, None, []))[2]:
    if i.endswith('.pdf'):
        set_rot(i,input_dir,output_dir)