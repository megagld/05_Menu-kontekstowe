#bmystek
import os
import regex as re
import pymsgbox

folder_path = os.getcwd()

reg_pat='''(.+)(_rew.\d{3})(.pdf)'''

pdf_c=0
pdf_cd=0

for path,_,files in os.walk(folder_path):
    for pdf_file in files:
        if pdf_file.endswith(".pdf"):
            pdf_cd+=1
        x_match=re.match(reg_pat,pdf_file)
        if x_match:
            new_name = pdf_file.replace(x_match.group(2),'')
            old_name = '{}\\{}'.format(path,pdf_file)
            new_name = '{}\\{}'.format(path,new_name)
            if new_name not in path:
                pdf_c+=1                
                os.rename(old_name, new_name)

pymsgbox.alert("Zmienion nazwy {} plików, pominięto {} pdfów".format(pdf_c, pdf_cd-pdf_c))