#bmystek
import shutil
import os
 
def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]
 
input_dir = os.getcwd()
output_dir = '{}\\{}'.format(input_dir,'_kopia struktury katalogów')

shutil.copytree(input_dir,
                output_dir,
                ignore=ignore_files)