#bmystek
import os
import regex as re
import pymsgbox

input_dir = os.getcwd()
ct=0

reg_pat='''.+(segment|Segment)( |_)([VIXvix, ]*).+(pdf|dwg)'''

for x in os.listdir(input_dir):
    x_match=re.match(reg_pat,x)
    if x_match:
        new_name = x.replace(x_match.group(3),x_match.group(3).upper())
        old_name = '{}\\{}'.format(input_dir,x)
        new_name = '{}\\{}'.format(input_dir,new_name)
        if new_name not in input_dir:
            os.rename(old_name, new_name)
            ct+=1

pymsgbox.alert(text='Zmieniono nazwy {} plików'.format(ct))