#bmystek
from pathlib import Path
import os

input_dir = os.getcwd()

# Numeracja rysunków i ich nazwy
###############################################

rys=[
    # ['_01.01','_01.01 - Zalozenia drogowe'],
    # ['_01.02','_01.02 - Rzut'],
    # ['_01.03','_01.03 - Przekroj podluzny'],
    # ['_01.04','_01.04 - Przekroj poprzeczny'],
    # ['_01_','_01 - Zalozenia drogowe.'],
    # ['_02_','_02 - Rzut.'],
    # ['_03_','_03 - Przekroj podluzny.'],
    # ['_04_','_04 - Przekroj poprzeczny.'],
    # ['.01_','.01 - Zalozenia drogowe.'],
    # ['.02_','.02 - Rzut.'],
    # ['.03_','.03 - Przekroj podluzny.'],
    # ['.04_','.04 - Przekroj poprzeczny.',
    ['_01.','_01_Zalozenia drogowe.'],
    ['_02.','_02_Rzut.'],
    ['_03.','_03_Przekroj podluzny.'],
    ['_04.','_04_Przekroj poprzeczny.']]

###############################################

for x in os.listdir(input_dir):
    if not x.endswith('.pdf') or len(x)<10 or x[0]!='0':
        continue
    old_name = '{}\\{}'.format(input_dir,x)
    new_name = old_name
    for i,j in rys:
        if i in old_name and j not in old_name:
            new_name = new_name.replace(i,j)
            break
    if new_name not in input_dir:
        os.rename(old_name, new_name)