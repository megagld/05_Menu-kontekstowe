if __name__ == '__main__':
    from context_menu import menus
    import sys
    import os
    import json
    
    try:
        menus.removeMenu('mgld_pomoc', 'DIRECTORY_BACKGROUND')
    except:
        pass

    pyt_loc=sys.executable

    def get_cb_state():
        scr_loc = os.path.dirname(__file__)
        with open('{}\\{}'.format(scr_loc,'scripts_states.json'), 'r') as fp:
            scripts_states = json.load(fp)
        return scripts_states

    def get_sc_list():
        scr_loc = os.path.dirname(__file__)
        with open('{}\\{}'.format(scr_loc,'scripts_list.json'), 'r') as fp:
            scripts_list = json.load(fp)
        return scripts_list

    scripts_st=get_cb_state()

    scripts_list=get_sc_list()
    
    scr_loc=os.getcwd()

    for i,j in scripts_list.items():
        scripts_list[i]='{}\\{}\\{}'.format(scr_loc,i,j)

    cm = menus.ContextMenu('mgld_pomoc', type='DIRECTORY_BACKGROUND')
    pytw_loc=pyt_loc.replace('.exe','w.exe')
    
    for sc_name,script in scripts_list.items():
        if sc_name in scripts_st.keys() and scripts_st[sc_name]=='1':
            cm.add_items([
                menus.ContextCommand(sc_name, command='''"{}" "{}"'''.format(pytw_loc,script)),
            ])

    main_loc='{}\\{}\\{}'.format(scr_loc,'00_Menu kontekstowe','main.py')   

    cm.add_items([
        menus.ContextCommand('...', command='''"{}" "{}"'''.format(pytw_loc,main_loc)),
    ])


    cm.compile()