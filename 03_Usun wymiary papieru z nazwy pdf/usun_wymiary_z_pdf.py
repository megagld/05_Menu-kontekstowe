#bmystek
import os
import regex as re

input_dir = os.getcwd()

reg_pat='''.+(_\d{3}x\d{4})\D.*pdf'''

for x in os.listdir(input_dir):
    x_match=re.match(reg_pat,x)
    if x_match:
        new_name = x.replace(x_match.group(1),'')
        old_name = '{}\\{}'.format(input_dir,x)
        new_name = '{}\\{}'.format(input_dir,new_name)
        if new_name not in input_dir:
            os.rename(old_name, new_name)