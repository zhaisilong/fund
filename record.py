import pandas as pd
from pathlib import Path
import os
from collections import defaultdict
from datetime import datetime

DIR = Path('data/trace')

def get_options():
    files = defaultdict(None)
    i = 0
    for file in os.listdir(DIR):
        if file.endswith('csv'):
            print(i, end=': ')
            print(file.rstrip('.csv'))
            files[i] = file
            i += 1
    try:
        an = int(input('choose your file:'))
        if isinstance(an, int):
            return files[an]
        else:
            exit(1)
    except:
        exit(1)


def write_data(file):
    path = DIR / file
    df = pd.read_csv(path, index_col=0)
    print(f"last buy operation: {df[df['operation']=='buy'].iloc[-1].values}")
    buy_sell = input('buy or sell(0 or 1)')
    if buy_sell == '1':
        buy_sell = 'sell'
    else:
        buy_sell = 'buy'
    value = input('value:')
    new_df = pd.DataFrame(
        {'date': [datetime.now().strftime('%Y-%m-%d')],
         'operation': [buy_sell],
         'quantity': [value]
         }
    )
    df = pd.concat([df, new_df], ignore_index=True)
    # 修复索引
    df.reset_index(inplace=True, drop=True)
    # 写入
    df.to_csv(path)


def main():
    file = get_options()
    while (file != 'q') or (not file):
        try:
            write_data(file)
            file = get_options()
        except KeyboardInterrupt:
            exit(1)


if __name__ == '__main__':
    main()
