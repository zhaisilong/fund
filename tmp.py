from pathlib import Path


cache_path = Path('/home/seeyou/.cache/matplotlib/fontlist-v330.json')
p = Path('/home/seeyou')
print(cache_path.exists())
if cache_path.exists():
    print('Delete cache')
if p.exists():
    print('p')
