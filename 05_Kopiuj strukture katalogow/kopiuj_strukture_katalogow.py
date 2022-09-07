#bmystek
# importing the shutil module
import shutil
from pathlib import Path
 
# importing the os module
import os
 
# defining the function to ignore the files
# if present in any folder
def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]
 
# calling the shutil.copytree() method and
# passing the src,dst,and ignore parameter

input_dir = os.getcwd()
output_dir = '{}\\{}'.format(input_dir,'_kopia struktury katalogów')

shutil.copytree(input_dir,
                output_dir,
                ignore=ignore_files)