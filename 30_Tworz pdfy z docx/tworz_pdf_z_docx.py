#bmystek
from docx2pdf import convert
import os
import pymsgbox
import sys

def main():


    input_dir = os.getcwd()

    f = open("E:\\usun\\log.out", 'w')

    sys.stdout = f
    print ('test')
    
    for i,_,k in os.walk(input_dir):
        for l in k:
            if l.endswith('.docx'):
                file_path='{}\\{}'.format(i,l)
                file_path_pdf='{}\\{}'.format(i,l).replace('.docx','.pdf')
                print(file_path)
                print(file_path_pdf)

                try:
                    # pymsgbox.alert(text=file_path_pdf)

                    convert(file_path,file_path_pdf,keep_active=False)

                except:
                    with open('{}/uszkodzone pliki.txt'.format(input_dir), 'a') as f:

                        f.write('{}\n'.format(file_path))
    f.close()

if __name__ == "__main__":
    main()