#bmystek
import os

input_dir = os.getcwd()

# lista znaków do zmiany
###############################################

znaki={
    'ą':'a',
    'ć':'c',
    'ę':'e',
    'ł':'l',
    'ń':'n',
    'ó':'o',
    'ś':'s',
    'ź':'z',
    'ż':'z',
    'ł':'l'
}

###############################################

# których plików dotyczy:
###############################################

fil_ext=[
    '.dwg',
    '.pdf'
]

###############################################

for path, subdirs, files in os.walk(input_dir):
    for name in files:
        x=os.path.join(path, name)
        if not any(x.endswith(i) for i in fil_ext):
            continue
        old_name = x
        new_name = name
        for i,j in znaki.items():
            new_name=new_name.replace(i,j)

        new_name=  '{}\\{}'.format(path,new_name) 

        if new_name not in input_dir:
            os.rename(old_name, new_name)