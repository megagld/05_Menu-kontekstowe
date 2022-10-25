#bmystek
import os

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

for path, subdirs, files in os.walk(input_dir):
    for name in files:
        for tail in tails:
            if name.endswith(tail):
                print(os.path.join(path, name))
                os.remove(os.path.join(path, name))