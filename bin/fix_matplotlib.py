import matplotlib
from pathlib import Path
import shutil
import os, platform

simhei = 'SimHei.ttf'
target_path = Path(matplotlib.matplotlib_fname()).parent
source_path = Path('data/others')
# different system has different cache_path
if platform.system() == 'Darwin':
    print('your system is Darwin')
    cache_path = Path(os.environ['HOME'] + '/.matplotlib')
elif platform.system() == 'Linux':
    print('your system is Linux')
    cache_path = Path(os.environ['HOME'] + '/.cache/matplotlib')
print(f'your cache path is {cache_path}')
if cache_path.exists():
    shutil.rmtree(cache_path)
    print('Cache deleted successfully')

source = source_path / simhei
target = target_path / 'fonts/ttf' / simhei
shutil.copyfile(source, target)

print(f'Move \n\t{source}\nto \n\t{target}')
print('Finished, then your can use:')
print("\tplt.rcParams['font.sans-serif']=['SimHei']")
