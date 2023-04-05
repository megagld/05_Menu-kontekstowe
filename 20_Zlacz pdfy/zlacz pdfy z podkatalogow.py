from PyPDF2 import PdfMerger
import os

#Create an instance of PdfFileMerger() class
merger = PdfMerger(strict=False)

#Create a list with the file paths
folder_path = os.getcwd()
pdf_files=[]
for path,_,files in os.walk(folder_path):
    for pdf_file in files:
        if pdf_file.endswith(".pdf") and not "_OT_" in pdf_file:
            pdf_files.append('{}\\{}'.format(path, pdf_file))

#Iterate over the list of the file paths
for pdf_file in pdf_files:
    #Append PDF files
    merger.append(pdf_file)

#Write out the merged PDF file
merger.write("{}\\_scalone.pdf".format(folder_path))
merger.close()