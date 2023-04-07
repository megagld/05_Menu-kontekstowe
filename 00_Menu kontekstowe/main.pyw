from tkinter import *
import json
import os

def get_sc_states():
    global scripts_states, scripts_states_cb
    with open('{}\\{}'.format(scr_loc,'scripts_states.json'), 'r') as fp:
        scripts_states = json.load(fp)
    scripts_states_cb=scripts_states.copy()

def set_sc_states():
    for i in scripts_states.keys():
        scripts_states[i]=scripts_states_cb[i].get()
    with open('{}\\{}'.format(scr_loc,'scripts_states.json'), 'w') as fp:
        json.dump(scripts_states, fp)

def update_sc_list():
    os.system('''python "{}\\{}"'''.format(scr_loc,'get_scripts_list.py'))

def add_menu():
    set_sc_states()
    os.system('''python "{}\\{}"'''.format(scr_loc,'dodaj_menu.py'))

def remove_menu():
    os.system('''python "{}\\{}"'''.format(scr_loc,'usun_menu.py'))
    
def get_libs():
    os.system('''python "{}\\{}"'''.format(scr_loc,'get_libs_state.py'))
    get_libs_stat()
    show_libs()

def get_libs_stat():
    global needed_lib_list,lib_diff
    needed_tar_loc= "{}\\needed_libs.txt".format(scr_loc)
    lib_list = open(needed_tar_loc, "r")
    needed_lib_list = lib_list.read().split('\n')
    needed_lib_list=[i.split('==')[0] for i in needed_lib_list if i]

    diff_tar_loc= "{}\\diff_libs.txt".format(scr_loc)
    lib_diff = open(diff_tar_loc, "r").read().split('\n')

def install_libs():
    os.system('''python "{}\\{}"'''.format(scr_loc,'install_libs.py'))

def show_libs():
    global needed_lib_list, lib_diff, sis

    sis_x_pos,sis_y_pos=master.winfo_x() + 300, master.winfo_y()  + 100

    sis = Tk()
    sis.minsize(200,50)
    sis.geometry('+{}+{}'.format(sis_x_pos,sis_y_pos))

    Label(sis, text="Lista wymaganych bibliotek:").grid(row=0, sticky=S)

    for i,j in enumerate(needed_lib_list):
        if j in lib_diff: col='#FF6347'
        else: col='#99D4B1'
        Label(sis, text=j, bg=col).grid(row=i+1, sticky=S)

    Button(sis, text='Instaluj brakujące biblioteki', command = install_libs, width=25).grid(row=i+2, pady=4, padx=20)
    Button(sis, text='Quit', command = sis.destroy).grid(row=i+3, pady=4, padx=20)

    mainloop()

def close_master_win():
    set_sc_states()
    update_sc_list()
    master.destroy()

def draw_win():
    Label(master, text="Lista skryptów:").grid(row=0, sticky=W)

    # dodaje checkboxy
    for j,i in enumerate(sorted(scripts_states_cb.keys())):
        scripts_states_cb[i] = Variable()
        Checkbutton(master, text=i, variable=scripts_states_cb[i]).grid(row=j+1, sticky=W)

    # ustala stan checkboxów
    for i,j in scripts_states_cb.items():
        j.set(scripts_states[i])

    # dodaje przyciski
    sc_len=len(scripts_states_cb)
    Button(master, text='Dodaj menu kontekstowe', command=add_menu).grid(row=sc_len+2, pady=4)
    Button(master, text='Usuń menu kontekstowe', command=remove_menu).grid(row=sc_len+3, pady=4)
    Button(master, text='Wymagane biblioteki', command =get_libs).grid(row=sc_len+4, pady=4)
    Button(master, text='Quit', command = lambda: close_master_win()).grid(row=sc_len+5, pady=4)

    mainloop()


scr_loc=os.path.dirname(__file__)

get_sc_states()

master = Tk()

draw_win()
