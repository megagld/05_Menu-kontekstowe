import os

acad_loc="C:/Program Files/Autodesk/AutoCAD 2018/acad.exe"

input_dir = os.getcwd()
# input_dir = os.path.dirname(__file__)

with open(input_dir+'\otworz_wiele_dwg.bat', 'w', encoding="utf-8") as file:
    file.write('''"{}"'''.format(acad_loc))

for path, subdirs, files in os.walk(input_dir):
    for name in files:
        if name.endswith('.dwg') and not 'xref' in path:
            with open(input_dir+"\\otworz_wiele_dwg.bat", "a") as file:
                file.write(''' "{}"'''.format(os.path.join(path, name)))