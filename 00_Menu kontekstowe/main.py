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

def close_win():
    set_sc_states()
    update_sc_list()
    master.quit()

def draw_win():
    Label(master, text="Lista skryptów:").grid(row=0, sticky=W)

    # dodaje checkboxy
    for j,i in enumerate(scripts_states_cb.keys()):
        scripts_states_cb[i] = Variable()
        Checkbutton(master, text=i, variable=scripts_states_cb[i]).grid(row=j+1, sticky=W)

    # ustala stan checkboxów
    for i,j in scripts_states_cb.items():
        j.set(scripts_states[i])

    # dodaje przyciski
    sc_len=len(scripts_states_cb)
    Button(master, text='Dodaj menu kontekstowe', command=add_menu).grid(row=sc_len+2, pady=4)
    Button(master, text='Usuń menu kontekstowe', command=remove_menu).grid(row=sc_len+3, pady=4)
    Button(master, text='Quit', command = lambda: close_win()).grid(row=sc_len+4, pady=4)

    mainloop()


scr_loc=os.path.dirname(__file__)

get_sc_states()

master = Tk()

draw_win()
