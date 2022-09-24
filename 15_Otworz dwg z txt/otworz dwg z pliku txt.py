import os
acad_loc="C:/Program Files/Autodesk/AutoCAD 2018/acad.exe"

input_dir = os.getcwd()

files=[]

with open(input_dir+'\dwg.txt', 'r', encoding="utf-8") as f:
     files = f.readlines()
# print(files)
f.close()

with open(input_dir+'\otworz_konkretne dwg.bat', 'w', encoding="utf-8") as file:
    file.write('''"{}"'''.format(acad_loc))

for name in files:
    with open(input_dir+"\\otworz_konkretne dwg.bat", "a") as file:
        file.write(''' "{}"'''.format(name.rstrip()))
