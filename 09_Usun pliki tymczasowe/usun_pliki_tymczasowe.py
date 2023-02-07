#bmystek
import os
import pymsgbox

# usuwa wszystkie pliki z poniższymi rozszerzeniami ze wszystkich podkatalogów

# rozszerzenia plików do usunięcia
###############################################

tails=[
    '.bak',
    '.dwl',
    '.log',
    '.dwl2',
    '.err',
    '.db'
]

###############################################


input_dir = os.getcwd()

ct=0

for path, subdirs, files in os.walk(input_dir):
    for name in files:
        for tail in tails:
            if name.endswith(tail):
                print(os.path.join(path, name))
                os.remove(os.path.join(path, name))
                ct+=1

pymsgbox.alert(text='Usunięto {} plików.'.format(ct), title='{}'.format(', '.join(tails)), button='OK')