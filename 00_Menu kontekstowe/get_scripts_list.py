#bmystek
import os
import json

input_dir = os.path.dirname(__file__).rstrip('00_Menu kontekstowe')

scripts_list={}

for path, subdirs, files in os.walk(input_dir):
    for file in files:
        if not 'git' in path and '00' not in path and file.endswith('.py'):
            scripts_list[path.split('\\')[-1]]=file

input_dir = os.path.dirname(__file__)
with open('{}\\{}'.format(input_dir,'scripts_list.json'), 'w') as fp:
    json.dump(scripts_list, fp)

with open('{}\\{}'.format(input_dir,'scripts_states.json'), 'r') as fp:
        scripts_states = json.load(fp)

for k in scripts_list:
    if k not in scripts_states:
        scripts_states[k]="0"

scripts_states={k:v for k,v in scripts_states.items() if k in scripts_list}

with open('{}\\{}'.format(input_dir,'scripts_states.json'), 'w') as fp:
     json.dump(scripts_states, fp)