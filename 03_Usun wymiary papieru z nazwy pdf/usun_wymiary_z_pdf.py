#bmystek
import imp
import os
# from pathlib import Path

input_dir = os.getcwd()

# Ilość znaków do usunięcia
###############################################

ct=9

###############################################

for x in os.listdir(input_dir):
    if not x.endswith('.pdf') or len(x)<9 or x[-9]!='x':
        continue
    old_name = '{}\\{}'.format(input_dir,x)
    new_name = '{}{}'.format(old_name[:-ct-4],'.pdf')
    if new_name not in input_dir:
        os.rename(old_name, new_name)