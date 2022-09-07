if __name__ == '__main__':
    from context_menu import menus
    import sys
    import os
    
    try:
        menus.removeMenu('mgld_pomoc', 'DIRECTORY_BACKGROUND')
    except:
        pass

    pyt_loc=sys.executable

    scripts={
        "03_Usun wymiary papieru z nazwy pdf":                      "03_Usun wymiary papieru z nazwy pdf\\usun_wymiary_z_pdf.py",
        "05_Kopiuj strukturę katalogów":                            "05_Kopiuj strukture katalogow\\kopiuj_strukture_katalogow.py",
        "06_Dodaj nazwy do rysunków ogólnych (tylko pliki pdf)":    "06_Dodaj nazwy do rys ogolnych\\dodaj_nazwy.py",
        "07_Usuń nazwy z rysunków ogólnych (tylko pliki pdf)":      "07_Usun nazwy z rys ogolnych\\usun_nazwy.py",
        "08_Przenieś pdf'y":                                        "08_Przenies pdfy do podkatalogow\\przenies_pdfy.py",
        "09_Usuń pliki tymczasowe":                                 "09_Usun pliki tymczasowe\\usun_pliki_tymczasowe.py",
        "10_Usun Polskie znaki":                                    "10_Usun Polskie znaki\\usun_polskie_znaki.py"


    }

    # tu podać lokalizację skryptów
    # scr_loc='E:\\Python\\05_Menu kontekstowe\\'
    scr_loc=os.getcwd()

    for i,j in scripts.items():
        scripts[i]='{}\\{}'.format(scr_loc,j)



    cm = menus.ContextMenu('mgld_pomoc', type='DIRECTORY_BACKGROUND')
    for sc_name,script in scripts.items():
        cm.add_items([
            menus.ContextCommand(sc_name, command='''"{}" "{}"'''.format(pyt_loc,script)),
        ])

    cm.compile()