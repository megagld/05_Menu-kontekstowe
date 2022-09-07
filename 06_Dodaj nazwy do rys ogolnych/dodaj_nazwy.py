#bmystek
from pathlib import Path
import os

input_dir = os.getcwd()

# Numeracja rysunków i ich nazwy
###############################################

rys=[
    ['_01','_01 - OG.Zalozenia drogowe'],
    ['_02','_02 - OG.Rzut'],
    ['_03','_03 - OG.Przekroj podluzny'],
    ['_04','_04 - OG.Przekroj poprzeczny']
]

###############################################

for x in os.listdir(input_dir):
    if not x.endswith('.pdf') or len(x)<10 or x[0]!='0':
        continue
    old_name = '{}\\{}'.format(input_dir,x)
    new_name = old_name
    for i,j in rys:
        if j not in old_name:
            new_name = new_name.replace(i,j)
    if new_name not in input_dir:
        os.rename(old_name, new_name)