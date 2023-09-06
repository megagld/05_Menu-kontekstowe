# do napisania -  dodać okienko tkinter pobierające ścieżki dostępu, dodać porównanie dat zapisu i względnych lokalizacji zapisu

import os

dir_1='P:/0139_A2_Siedlce_Cicibor_VII/04_PW/02_PW_M/03_PDF'
dir_2='O:/0139_A2_Siedlce_Cicibor_VII/18_Materialy przekazane/2023.06.29 - PW, PT - wydruk - pdf/PW/02_PW_M'

def get_size(start_path):
    total_size = 0
    li=[]
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
            li.append(f+str(os.path.getsize(fp)))
    return total_size,li

s_1,d_1=get_size(dir_1)
s_2,d_2=get_size(dir_2)

dif1=[i for i in d_1 if i not in d_2]
dif2=[i for i in d_2 if i not in d_1]

print('pliki różnicowe: ',dif1)
print('pliki różnicowe: ',dif2)