#bmystek
import os

input_dir = os.path.dirname(__file__)

diff_libs='diff_libs.txt'

print('''pip install -r "{}\\{}"'''.format(input_dir,diff_libs))

os.system('''pip install -r "{}\\{}"'''.format(input_dir,diff_libs))