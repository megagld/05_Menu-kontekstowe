#bmystek
import os
from pdfrw import PdfReader
import shutil

# tworzy podkatalogi
input_dir = os.getcwd()
output_dir_rot="{}\\_obrócone".format(input_dir)
output_dir_ok="{}\\_prawidłowe".format(input_dir)


if not os.path.exists(output_dir_rot):
    os.makedirs(output_dir_rot)

if not os.path.exists(output_dir_ok):
    os.makedirs(output_dir_ok)

# kopiuje plik do wskazanego katalogu
def copy_to(pdf,dest):
        pdf_from='{}\\{}'.format(input_dir,pdf)
        pdf_to='{}\\{}'.format(dest,pdf)
        shutil.copyfile(pdf_from, pdf_to)

# pobiera pdfy z katalogu, sprawdza ilość stron, wymiary i kopiuje do odpowiedniego podkatalogu
for i in next(os.walk(input_dir), (None, None, []))[2]:
    if i.endswith('.pdf'):
        file_to_move=PdfReader("{}\\{}".format(input_dir,i))
        w,h=(float(i) for i in file_to_move.pages[0].inheritable.MediaBox[2:])

        if len(file_to_move.pages)>1 or w>=h:
            print('ok')
            copy_to(i,output_dir_ok)
        else:
            print('nie ok')
            copy_to(i,output_dir_rot)



