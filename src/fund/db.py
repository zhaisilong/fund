from datetime import datetime
from pathlib import Path
from typing import List

import pandas as pd


class DB:
    def __init__(self, path: str):
        self.path = Path(path)
        self.df = self.load()
        self.reset_index()  # 首次导入后都进行一次重置，保证程序运行

    def load(self):
        return pd.read_csv(self.path, parse_dates=['date'], index_col=0)

    def reset_index(self):
        return self.df.reset_index(drop=True, inplace=True)

    def save(self):
        self.reset_index()
        self.df.to_csv(self.path)

    def append(self, item):
        self.df = self.df.append(item.df)
        self.reset_index()

    def remove(self, idx: List[int]):
        self.df.drop(labels=idx, inplace=True)
        self.reset_index()

    def __len__(self):
        return len(self.df)

    def __repr__(self):
        return repr(self.df)


class TraceDB(DB):
    def __init__(self, path: str):
        super(TraceDB, self).__init__(path)


class FundDB(DB):
    def __init__(self, path: str):
        super(FundDB, self).__init__(path)


class TraceItem:
    def __init__(self, date, operation, money):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.operation = operation
        self.money = money

    @property
    def df(self):
        return pd.DataFrame({'date': [self.date], 'operation': [self.operation], 'money': [self.money]})


class FundItem:
    def __init__(self, date, value):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.value = value

    @property
    def df(self):
        return pd.DataFrame({'date': [self.date], 'value': [self.value]})


if __name__ == "__main__":
    trace_db = TraceDB('../data/trace.csv')
    trace_item = TraceItem('2022-10-10', 'buy', 2000)
    trace_db.append(trace_item)
    print(trace_db)
    trace_db.save()
    fund_db = FundDB('../data/funds/万家精选混合A-519185.csv')
    print(fund_db)
