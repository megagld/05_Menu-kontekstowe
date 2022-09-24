#bmystek
import os
import re

input_dir = os.getcwd()

# których plików dotyczy:
###############################################

fil_ext=[
    '.dwg',
    '.pdf'
]

###############################################

for path, subdirs, files in os.walk(input_dir):
    for name in files:
        if not any(name.endswith(i) for i in fil_ext):
            continue
        old_name = os.path.join(path, name)
        new_name = re.sub(r'[^\x00-\x7F]+','_', name)
        new_name = os.path.join(path, new_name)

        if new_name not in input_dir:
            os.rename(old_name, new_name)