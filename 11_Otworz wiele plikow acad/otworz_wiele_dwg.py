import os

acad_loc="C:\Program Files\Common Files\Autodesk Shared\AcShellEx\AcLauncher.exe"

input_dir = os.getcwd()
# input_dir = os.path.dirname(__file__)

with open(input_dir+'\otworz_wiele_dwg.bat', 'w', encoding="utf-8") as file:
    file.write('''"{}"'''.format(acad_loc))

with open(input_dir+'\otworz_wiele_dwg - lista plikow.txt', 'w', encoding="utf-8") as file:
    file.write('Lista plików do otwarcia:\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')

pliki_pominiete=[]

for path, subdirs, files in os.walk(input_dir):
    for name in files:
        if name.endswith('.dwg'):
            if  not 'xref' in path:
                with open(input_dir+"\\otworz_wiele_dwg.bat", "a") as file:
                    file.write(''' "{}"'''.format(os.path.join(path, name)))
                with open(input_dir+"\\otworz_wiele_dwg - lista plikow.txt", "a") as file:
                    file.write('{}\n'.format(name))
            else:
                pliki_pominiete.append(name)

with open(input_dir+"\\otworz_wiele_dwg - lista plikow.txt", "a", encoding="utf-8") as file:
    file.write('\nLista plików pominiętych:\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
    
for name in pliki_pominiete:
    with open(input_dir+"\\otworz_wiele_dwg - lista plikow.txt", "a", encoding="utf-8") as file:
        file.write('{}\n'.format(name))