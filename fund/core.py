from datetime import timedelta, datetime, date
from typing import Optional

import pandas as pd
from plotnine import *
from pathlib import Path
from fund.db import FundDB, TraceDB
from fund.utils import get_logger
import warnings
import matplotlib

warnings.filterwarnings('ignore')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
log = get_logger(__name__)


class Fund:
    def __init__(self, path: str):
        self.fund_db = FundDB(path)
        self.path = self.fund_db.path
        self.name, self.code = self._get_name()

    @property
    def latest_day(self):
        return self.fund_db.df.date.tolist()[-1]

    @property
    def latest_value_stock(self):
        return self.fund_db.df['value'].tolist()[-1]

    def _get_name(self):
        """从路径中获取名字和代码"""
        name = self.path.name.split('-')[0]
        code = self.path.name.split('.')[0].split('-')[-1]
        return name, code

    def __repr__(self):
        return f'name: {self.name}, code: {self.code}'

    def __len__(self):
        return len(self.fund_db)

    def __str__(self):
        return repr(self)

    @property
    def df(self):
        return self.fund_db.df

    def _plot(self, parent: Path):
        parent.mkdir(exist_ok=True, parents=True)
        df = self.df.copy()
        df['delta'] = df.value - df.value.shift(periods=1, fill_value=1.)  # 标签为增量
        df['delta_percent'] = df['delta'] / df.value.shift(periods=1, fill_value=1.) * 100
        df = df.iloc[-240 * 4:]  # 最长展示 4 年
        df.reset_index(drop=True, inplace=True)
        # 插入三根垂直线 周 月 年
        vline_day = [df.date.iloc[-i] for i in [240, 20, 5]]  # 除去双休日
        # 插入两根水平线 0.3 0.7
        df.value.quantile([0.3, 0.7])
        hline_value = df.value.quantile([0.3, 0.7]).tolist()
        # 加入标签 每隔 1 个月
        txt_df = df.iloc[::-20]
        txt = {'x': txt_df.date.tolist(), 'y': txt_df.value.tolist(),
               'label': txt_df.apply(lambda row: f'{row["delta_percent"]:.2f}%', axis=1).tolist()}
        base_plot = (ggplot() +
                     geom_line(aes(x='date', y='value'), size=1, color='blue', data=df) +
                     geom_vline(xintercept=vline_day, colour=['red', 'orange', 'green'], size=1, data=df) +
                     geom_hline(yintercept=hline_value, colour=['black', 'pink'], size=2, data=df) +
                     geom_point(aes(x=txt['x'], y=txt['y']), color='red', size=1) +
                     geom_text(aes(label=txt['label'], x=txt['x'], y=txt['y']), color='black', size=14, ha='left',
                               va='top') +  # 从最新到最旧
                     scale_x_date(date_labels="%y-%m", date_breaks="3 month") +
                     xlab("Months") +
                     ylab("Values") +
                     ggtitle(f'{self.name}-{self.code}') +
                     theme(figure_size=(40, 10), text=element_text(family='SimHei'))
                     )
        base_plot.save(parent / f'{self.name}-{self.code}.png', limitsize=False, dpi=250)

    def _report(self, parent: Path):
        parent.mkdir(exist_ok=True, parents=True)
        content = []
        df = self.df.copy()
        df['delta'] = df.value - df.value.shift(periods=1, fill_value=1.)  # 标签为增量
        content.append('星期一到星期五的累计涨幅:\n')
        df['week'] = df['date'].dt.dayofweek + 1
        groups = df.groupby('week')
        for week, group in groups:
            content.append(f'{week}: {group["delta"].sum() * 100:.2f}%\n')
        content.append('年份的累计涨幅:\n')
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        for year, group in df.groupby('year'):
            content.append(f'{year}: {group["delta"].sum() * 100:.2f}%\n')

        content.append('月的累计涨幅:\n')
        for month, group in df.groupby('month'):
            content.append(f'{month}: {group["delta"].sum() * 100:.2f}%\n')

        file = parent / f'{self.name}-{self.code}.txt'
        with file.open('w') as f:
            f.writelines(content)

    def show(self, parent: Optional[str]):
        if parent:
            # 指定图像存放目录
            _parent = Path(parent)
            _parent.mkdir(exist_ok=True, parents=True)
        else:
            # 否则放在目录
            _parent = self.path
        imgs_path = _parent / 'imgs'
        report_path = _parent / 'reports'
        self._plot(parent=imgs_path)
        self._report(parent=report_path)


class Fee:
    def __init__(self):
        self.buy_fee_rate = 0.15 / 100

    def get_buy_fee_rate(self):
        return self.buy_fee_rate


import queue


class Pool:
    def __init__(self):
        self._date = []
        self._stock = []

    @property
    def stock(self):
        return sum(self._stock)

    def check(self):
        assert len(self._date) == len(self._stock)

    def buy(self, date: datetime, stock: float):
        self.check()
        self._date.append(date)
        self._stock.append(stock)

    def sell(self, stock: float):
        """从前往后取出请求的 stock 数量"""
        self.check()
        request_stock = stock
        acc_date = []
        acc_stock = []
        while True:
            pop_stock = self._stock.pop(0)
            pop_date = self._date.pop(0)
            if pop_stock > request_stock:
                self._stock.insert(0, pop_stock - request_stock)
                self._date.insert(0, pop_date)
                acc_date.append(pop_date)
                acc_stock.append(request_stock)
                break
            elif pop_stock == request_stock:
                acc_date.append(pop_date)
                acc_stock.append(request_stock)
                break
            else:
                request_stock -= pop_stock
                acc_date.append(pop_date)
                acc_stock.append(pop_stock)

        return acc_date, acc_stock

    @property
    def df(self):
        return pd.DataFrame({'date': self._date, 'stock': self._stock})


class Trace:
    def __init__(self, path: str, fund: Fund):
        self.trace_db = TraceDB(path)
        self.fund = fund
        self.path = self.fund.path
        self.name = self.fund.name
        self.code = self.fund.code
        self.gain = 0.
        self.pool = self._build()

    @property
    def investment(self):
        """总投资"""
        df = self.trace_db.df
        return df[df['operation'] == 'buy']['quantity'].sum()

    def plot(self):
        """在 fund 的基础上绘制 trace 图"""
        pass

    @property
    def stock(self):
        return self.pool.stock

    @property
    def latest_value_stock(self):
        return self.fund.latest_value_stock

    @property
    def value(self):
        return self.latest_value_stock * self.stock

    def _build(self) -> Pool:
        pool = Pool()
        for i, row in self.trace_db.df.iterrows():
            date = row['date']
            if date > self.fund.latest_day:
                log.info(f'最新一天尚未更新，请于工作日 15:00 后再试，此条记录将不纳入追踪')
                self.trace_db.df.drop(index=i, inplace=True)  # 直接丢弃该行
                continue
            value_stock = self._get_value_stock(date)  # float
            if row['operation'] == 'buy':
                money = row['quantity']
                stock = money * 0.9985 / value_stock
                pool.buy(date, stock)
            else:
                stock = row['quantity']
                days, stocks = pool.sell(stock)
                for day, stock in zip(days, stocks):
                    time_delta = date - day
                    fee_rate = self._get_sell_fee_rate(time_delta)
                    self.gain += stock * value_stock * (1 - fee_rate)

        return pool

    def _get_sell_fee_rate(self, time_delta):
        if time_delta <= timedelta(days=6):
            return 1.5 / 100
        elif time_delta <= timedelta(days=364):
            return 0.5 / 100
        elif time_delta <= timedelta(days=729):
            return 0.25 / 100
        else:
            return 0.

    def _get_value_stock(self, date: datetime):
        df = self.fund.df
        return df[df['date'] == date]['value'].tolist()[0]

    def _plot(self, parent: Path):
        parent.mkdir(exist_ok=True, parents=True)
        df = self.fund.df.copy()
        df['delta'] = df.value - df.value.shift(periods=1, fill_value=1.)  # 标签为增量
        df['delta_percent'] = df['delta'] / df.value.shift(periods=1, fill_value=1.) * 100
        df = df.iloc[-240 * 4:]  # 最长展示 4 年
        df.reset_index(drop=True, inplace=True)
        # 插入三根垂直线 周 月 年
        vline_day = [df.date.iloc[-i] for i in [240, 20, 5]]  # 除去双休日
        # 插入两根水平线 0.3 0.7
        df.value.quantile([0.3, 0.7])
        hline_value = df.value.quantile([0.3, 0.7]).tolist()
        # 加入标签 每隔 1 个月
        txt_df = df.iloc[::-20].reset_index(drop=True)
        txt = {'x': txt_df.date.tolist(), 'y': txt_df.value.tolist(),
               'label': txt_df.apply(lambda row: f'{row["delta_percent"]:.2f}%', axis=1).tolist()}
        # 加入买入卖出的点
        buy_days = []  # 占位，防止为空的输入
        sell_days = []
        for operation, group in self.trace_db.df.groupby('operation'):
            if operation == 'buy':
                buy_days = group['date'].tolist()
            if operation == 'sell':
                sell_days = group['date'].tolist()
        buys = {'date': buy_days, 'value': [self._get_value_stock(day) for day in buy_days]}
        sells = {'date': sell_days, 'value': [self._get_value_stock(day) for day in sell_days]}
        base_plot = (ggplot() +
                     geom_line(aes(x='date', y='value'), size=1, color='blue', data=df) +
                     geom_vline(xintercept=vline_day, colour=['red', 'orange', 'green'], size=1, data=df) +
                     geom_hline(yintercept=hline_value, colour=['black', 'pink'], size=2, data=df) +
                     geom_point(aes(x=txt['x'], y=txt['y']), color='green', size=2) +
                     geom_text(aes(label=txt['label'], x=txt['x'], y=txt['y']), color='black', size=14, ha='left',
                               va='top') +  # 从最新到最旧
                     geom_point(aes(x=buys['date'], y=buys['value']), color='black', size=1) +  # 这里买入的点
                     geom_point(aes(x=sells['date'], y=sells['value']), color='red', size=1) +  # 这里加入卖出的点
                     scale_x_date(date_labels="%y-%m", date_breaks="3 month") +
                     xlab("Months") +
                     ylab("Values") +
                     ggtitle(f'{self.name}-{self.code}') +
                     theme(figure_size=(40, 10), text=element_text(family='SimHei'))
                     )
        base_plot.save(parent / f'{self.name}-{self.code}.png', limitsize=False, dpi=250)

    def _report(self, parent: Path):
        parent.mkdir(exist_ok=True, parents=True)
        if self.investment:
            content = list()
            content.append(f'投资总金额：{self.investment:.2f}元\n')
            content.append(f'股份数：{self.stock:.2f}份\n')
            content.append(f'当前每股单价：{self.latest_value_stock:.2f}元/份\n')
            content.append(f'卖出收益(扣税后)：{self.gain:.2f}元\n')
            content.append(f'基金价值：{self.value:.2f}元\n')
            content.append(
                f'收益率(卖出收益+基金价值/投资总金额,部分扣税)：{(self.value + self.gain - self.investment) / self.investment * 100:.2f}%\n')
            pool_pro = self.pool.df.copy()
            today = datetime.strptime(str(date.today()), '%Y-%m-%d')
            pool_pro['day_delta'] = pool_pro['date'].apply(lambda x: today - x)
            pool_pro['fee/%'] = pool_pro['day_delta'].apply(lambda x: self._get_sell_fee_rate(x) * 100)
            pool_pro['value'] = pool_pro['date'].apply(self._get_value_stock)
            pool_pro['improve/%'] = pool_pro.apply(
                lambda x: (self.latest_value_stock - x['value']) / x['value'] * 100, axis=1)
            content.append(f'池子:\n{repr(pool_pro)}\n')
            file = parent / f'{self.name}-{self.code}.txt'
            with file.open('w') as f:
                f.writelines(content)
        else:
            log.warning(f"您还未做任何投资！请按格式填写{self.name}-{self.code}.csv")

    def show(self, parent: Optional[str]):
        if parent:
            # 指定图像存放目录
            _parent = Path(parent)
            _parent.mkdir(exist_ok=True, parents=True)
        else:
            # 否则放在目录
            _parent = self.path
        imgs_path = _parent / 'imgs'
        report_path = _parent / 'reports'
        self._plot(parent=imgs_path)
        self._report(parent=report_path)


if __name__ == '__main__':
    fund = Fund('../data/funds/万家精选混合A-519185.csv')
    print(fund)
    print(fund.df)
    fund.show(parent='../data/analysis')

    trace = Trace('../data/trace/trace.csv', fund=fund)
    trace.show(parent='../data/trace')
