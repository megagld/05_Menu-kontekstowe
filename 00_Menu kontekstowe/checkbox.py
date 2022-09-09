from tkinter import *
import json
import os

def var_states():
    print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    for i in scripts_state.keys():
        print(scripts_cb_state[i].get(),':',i)

    scr_loc = os.path.dirname(__file__)
    os.system('''python "{}\\{}"'''.format(scr_loc,'get_scripts_list.py'))

    make_win()

# zapisuje stan checboxów do pliku
def save_state():
    # to zmienić na funkcję pobierającą listę skryptów na podstawie katalogów
    # scr_loc=os.getcwd()
    scr_loc = os.path.dirname(__file__)

    for i in scripts_state.keys():
        scripts_state[i]=scripts_cb_state[i].get()

    with open('{}\\{}'.format(scr_loc,'data.json'), 'w') as fp:
        json.dump(scripts_state, fp)

# pobiera stan checkboxów
def get_cb_state():
    # scr_loc=os.getcwd()
    scr_loc = os.path.dirname(__file__)
    with open('{}\\{}'.format(scr_loc,'data.json'), 'r') as fp:
        scripts_state = json.load(fp)
    return scripts_state

def add_menu():
    save_state()
    scr_loc = os.path.dirname(__file__)
    os.system('''python "{}\\{}"'''.format(scr_loc,'dodaj_menu.py'))
def remove_menu():
    scr_loc = os.path.dirname(__file__)
    os.system('''python "{}\\{}"'''.format(scr_loc,'usun_menu.py'))

def make_win():
    Label(master, text="Lista skryptów:").grid(row=0, sticky=W)
    # dodaje checkboxy
    for j,i in enumerate(scripts_cb_state.keys()):
        scripts_cb_state[i] = Variable()
        l=Checkbutton(master, text=i, variable=scripts_cb_state[i]).grid(row=j+1, sticky=W)

    # ustala stan checkboxów
    for i,j in scripts_cb_state.items():
        j.set(scripts_state[i])


    # dodaje przyciski
    sc_len=len(scripts_state)
    Button(master, text='Quit', command=master.quit).grid(row=sc_len+2, pady=4)
    Button(master, text='Zapisz stan', command=save_state).grid(row=sc_len+3, pady=4)
    Button(master, text='Odśwież listę skryptów', command=var_states).grid(row=sc_len+4, pady=4)
    Button(master, text='Dodaj menu kontekstowe', command=add_menu).grid(row=sc_len+5, pady=4)
    Button(master, text='Usuń menu kontekstowe', command=remove_menu).grid(row=sc_len+6, pady=4)

    mainloop()


scripts_state=get_cb_state()    
scripts_cb_state=scripts_state.copy()

master = Tk()

make_win()