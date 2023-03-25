import os

# pobiera listę wymaganych bibliotek

scr_loc = os.path.dirname(__file__).replace("\\00_Menu kontekstowe","")
needed_tar_loc= "{}\\00_Menu kontekstowe\\needed_libs.txt".format(scr_loc)

os.system('''pipreqs "{}" --encoding=utf8 --savepath "{}"'''.format(scr_loc,needed_tar_loc))

# pobiera listę wymaganych bibliotek

all_tar_loc= "{}\\00_Menu kontekstowe\\all_libs.txt".format(scr_loc)
os.system('''pip freeze > "{}"'''.format(all_tar_loc))


lib_list = open(needed_tar_loc, "r")
needed_lib_list = lib_list.read().split('\n')
needed_lib_list=[i.split('==')[0] for i in needed_lib_list if i]

lib_list = open(all_tar_loc, "r")
all_lib_list = lib_list.read().split('\n')
all_lib_list=[i.split('==')[0] for i in all_lib_list if i]

# twórz listę bibliotek do zainstalowania

lib_diff=[i for i in needed_lib_list if i not in all_lib_list]

diff_tar_loc= "{}\\00_Menu kontekstowe\\diff_libs.txt".format(scr_loc)

f = open(diff_tar_loc, "w")
for i in lib_diff:
    f.write(i+'\n')
f.close()
