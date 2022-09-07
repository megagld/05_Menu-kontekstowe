#bmystek
from pathlib import Path
import os
import pdfplumber
import shutil

input_dir = '{}{}'.format(Path(__file__).parent,'''\\''')

# 842 odpowiada 297
# 1191 odpowiada 420
# 1684 odpowiada 594
# 2382 powinno być dla 841 - do sprawdzenia!!!!

di={842:'297',
    1191:'420',
    1684:'594',
    2382:'841',}

for x in os.listdir(input_dir):
    if not x.endswith('.pdf'):
        continue
    y = '{}\\{}'.format(input_dir,x)
    with pdfplumber.open(y) as pdf:
        page_1 = pdf.pages[0]
        height, width = page_1.height, page_1.width

        if len(pdf.pages)>1 or (height, width)==(842,595):
            output_dir = '{}{}'.format(Path(__file__).parent,'''\\_do druku\\_inne\\''')
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            shutil.copyfile(y, output_dir+x)
        elif height in di.keys():
            output_dir = '{}{}'.format(Path(__file__).parent,'''\\_do druku\\{}\\'''.format(di[height]))
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            shutil.copyfile(y, output_dir+x)
        else:
            output_dir = '{}{}'.format(Path(__file__).parent,'''\\_do druku\\_do sprawdzenia\\''')
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            shutil.copyfile(y, output_dir+x)