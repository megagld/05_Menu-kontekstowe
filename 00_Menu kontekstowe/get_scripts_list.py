#bmystek
import os
import json

input_dir = os.path.dirname(__file__).rstrip('00_Menu kontekstowe')

scripts={}

for path, subdirs, files in os.walk(input_dir):
    for file in files:
        if not 'git' in path and '00' not in path and file.endswith('.py'):
            scripts[path.split('\\')[-1]]=file

input_dir = os.path.dirname(__file__)
with open('{}\\{}'.format(input_dir,'data_scripts.json'), 'w') as fp:
    json.dump(scripts, fp)