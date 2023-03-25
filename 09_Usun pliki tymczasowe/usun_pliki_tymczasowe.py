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
vol=0

for path, subdirs, files in os.walk(input_dir):
    for name in files:
        for tail in tails:
            if name.endswith(tail):
                ct+=1
                vol+=os.path.getsize(os.path.join(path, name))
                os.remove(os.path.join(path, name))
print(vol)

pymsgbox.alert(text='Usunięto {} plików, {} KB.'.format(ct, round(vol*(10**-3))), title='{}'.format(', '.join(tails)), button='OK')