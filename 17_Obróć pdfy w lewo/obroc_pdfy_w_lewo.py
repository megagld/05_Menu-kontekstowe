#!/usr/bin/env python

import os
from pdfrw import PdfReader, PdfWriter, PageMerge

def rot(inn, input_dir, output_dir):

    inpfn = "{}\\{}".format(input_dir,inn)
    outfn = "{}\\{}".format(output_dir,inn)

    inp = PdfReader(inpfn)
    out = PdfWriter()

    def fixpage():
        # Stwórz kanwe, dodaj obróconą stronę
        canvas = PageMerge()
        canvas.add(page, rotate=-90)

        canvas.mbox = outbox
        return canvas.render()

    page=inp.pages[0]

    # # Pobranie wymiarów pdfa

    outbox=list(float(x) for x in page.inheritable.MediaBox)

    # Zmiana długości z wysokością

    outbox[2],outbox[3]=outbox[3],outbox[2]

    out.addpage(fixpage())

    out.write(outfn)

# tworzy podkatalog z obóconymi pdfami
input_dir = os.getcwd()
output_dir="{}\\_obrócone w lewo".format(input_dir)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# pobiera pdfy z katalogu, obraca i zapisuje w podkatalogu
for i in next(os.walk(input_dir), (None, None, []))[2]:
    if i.endswith('.pdf'):
        rot(i,input_dir,output_dir)