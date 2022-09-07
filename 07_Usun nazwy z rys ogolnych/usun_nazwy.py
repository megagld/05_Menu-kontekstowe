#bmystek
from pathlib import Path
import os

input_dir = os.getcwd()

for x in os.listdir(input_dir):
    if not x.endswith('.pdf') or len(x)<10 or x[0]!='0':
        continue
    old_name = '{}\\{}'.format(input_dir,x)
    new_name = old_name.split(' - ')[0]+'.pdf'
    if new_name not in input_dir:
        os.rename(old_name, new_name)