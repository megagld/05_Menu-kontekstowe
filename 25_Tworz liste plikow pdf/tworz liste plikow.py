#bmystek
import os

input_dir = os.getcwd()

lista_plikow=[]
files_count=0

for path,_,files in os.walk(input_dir):
    for pdf_file in files:
        if pdf_file.endswith(".pdf"):
            lista_plikow.append([path.split('\\')[-1],pdf_file])
            files_count+=1

with open("{}\{}.txt".format(input_dir,'lista plików'), 'a', encoding="utf-8") as file:
    file.write('Liczba plików: {}'.format(files_count)+'\n\n'+'Katalog:'+'\t'+'Plik:'+'\n')

for i in lista_plikow:
    with open("{}\{}.txt".format(input_dir,'lista plików'), 'a', encoding="utf-8") as file:
        file.write('\t'.join(i)+'\n')