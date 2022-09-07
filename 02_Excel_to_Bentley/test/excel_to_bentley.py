#bmystek
from pathlib import Path
from os import listdir
import pandas as pd

def make_file(file,fxt,sheet):
    dane = pd.read_excel(file, sheet_name=sheet)
    open(fxt, "w").close()

    fx=open(fxt,'a+')
    for i in range(1,len(dane)):
        a=dane.iloc[i,0:]
        b='|'.join(str(j) for j in a)+'\n'
        fx.write(b)
    fx.close()

for k in listdir(Path(__file__).parent):
    if not k.startswith("~") and k.endswith('xlsx'):
        file = '{}/{}'.format(Path(__file__).parent,k)
        fxt = '{}/{}'.format(Path(__file__).parent,k.replace('xlsx','txt'))
        sheet='Grupy nośności'
        make_file(file,fxt,sheet)