import matplotlib
from pathlib import Path
import shutil

simhei = 'SimHei.ttf'
target_path = Path(matplotlib.matplotlib_fname()).parent
source_path = Path('data/others')
source = source_path / simhei
target = target_path / 'fonts/ttf' / simhei
shutil.copyfile(source, target)
shutol.rmtree('~/.cache/matplotlib')
print('Delete cache')
print(f'Move \n\t{source}\nto \n\t{target}')
print('Finished, then your can use:')
print("\tplt.rcParams['font.sans-serif']=['SimHei']")
