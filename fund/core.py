import copy
from pathlib import Path
from typing import Tuple, Optional, Dict
import requests
import execjs
import time
from datetime import datetime, timedelta
import pandas as pd
from plotnine import *
from .plot import get_plot

class Fee:
    def __init__(self):
        self.buy_fee_rate = 0.15 / 100

    def get_sell_fee_rate(self, time_delta):
        if time_delta <= timedelta(days=6):
            return 1.5 / 100
        elif time_delta <= timedelta(days=364):
            return 0.5 / 100
        elif time_delta <= timedelta(days=729):
            return 0.25 / 100
        elif time_delta <= timedelta(days=730):
            return 0.

    def get_buy_fee_rate(self):
        return self.buy_fee_rate


class Fund:
    def __init__(self, fscode: str):
        content = requests.get(self._get_url(fscode))
        jsContent = execjs.compile(content.text)
        self.name = jsContent.eval('fS_name')
        self.code = jsContent.eval('fS_code')
        net_worth_trend = jsContent.eval('Data_netWorthTrend')  # 单位净值走势
        self.date = [self._x2date(day['x']) for day in net_worth_trend]
        self.value = [day['y'] for day in net_worth_trend]

    def __repr__(self):
        return f'name: {self.name}, code: {self.code}'

    def __len__(self):
        return len(self.date)

    def __str__(self):
        return repr(self)

    def _get_url(self, fscode):
        head = 'http://fund.eastmoney.com/pingzhongdata/'  # 东方财富
        tail = '.js?v=' + time.strftime("%Y%m%d%H%M%S", time.localtime())
        return head + fscode + tail

    def _x2date(self, x: int):
        assert isinstance(x, int)
        return datetime.fromtimestamp(x / 1000)

    @property
    def df(self) -> pd.DataFrame:
        return pd.DataFrame({'date': self.date, 'value': self.value})

    def show(self, parent: Optional[Path] = None):
        df = self.df.copy()
        df['delta'] = df.value - df.value.shift(periods=1, fill_value=1.)  # 标签为增量
        df['delta_percent'] = df['delta'] / df.value.shift(periods=1, fill_value=1.) * 100
        df = df.iloc[-240 * 4:]  # 最长展示 4 年
        df.reset_index(drop=True, inplace=True)
        # 插入三根垂直线 周 月 年
        vline_day = [self.date[-i] for i in [240, 20, 5]]  # 除去双休日
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
                     geom_text(aes(label=txt['label'], x=txt['x'], y=txt['y']), color='black', size=14, ha='left', va='top') +  # 从最新到最旧
                     scale_x_date(date_labels="%y-%m", date_breaks="3 month") +
                     xlab("Months") +
                     ylab("Values") +
                     ggtitle(f'{self.name}-{self.code}') +
                     theme(figure_size=(40, 10), text=element_text(family='SimHei'))

                     )
        if parent:
            parent.mkdir(exist_ok=True)
            base_plot.save(parent / f'{self.name}-{self.code}.png', limitsize=False, dpi=250)
        else:
            base_plot.save(parent / f'{self.name}-{self.code}.png', limitsize=False, dpi=250)


    def save(self):
        self.df.to_csv(f'{self.name}-{self.code}.csv')

    def analysis(self):
        df = self.df
        df['delta'] = 0.
        for i, row in df.iterrows():
            if i == 0:
                df.loc[i, 'delta'] = 0
            else:
                df.loc[i, 'delta'] = df.loc[i, 'value'] - df.loc[i - 1, 'value']

        print('星期一到星期五的累计涨幅')
        df['week'] = df['date'].dt.dayofweek + 1
        groups = df.groupby('week')
        for week, group in groups:
            print(week, group['delta'].sum())

        print('年份的累计涨幅')
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        for year, group in df.groupby('year'):
            print(year, group['delta'].sum())

        print('月份的累计涨幅')
        for month, group in df.groupby('month'):
            print(month, group['delta'].sum())


class History:
    def __init__(self):
        self.date = []
        self.money = []
        self.value = []

    @property
    def stock(self):
        """股份数列表
        """
        return [money / value for money, value in zip(self.money, self.value)]

    def get_stock(self):
        """获取累计股数"""
        self._check_history()
        return sum(self.stock)

    def get_invest(self):
        """计算总投资"""
        self._check_history()
        return sum(self.money)

    def get_asset(self, value):
        """计算总资产"""
        self._check_history()
        return self.get_stock() * value  # 使用最新的价格

    @property
    def df(self):
        return pd.DataFrame({'date': self.date, 'money': self.money, 'value': self.value})

    def __repr__(self):
        return repr(self.df)

    def __str__(self):
        return repr(self)

    def __len__(self):
        return len(self.date)

    def _check_history(self):
        assert len(self.date) == len(self.money) == len(self.value)

    def update(self, date, money, value, head: bool = False):
        self._check_history()
        if not head:
            self.date.append(date)
            self.money.append(money)
            self.value.append(value)
        else:
            self.date.insert(0, date)
            self.money.insert(0, money)
            self.value.insert(0, value)

    def pop(self) -> Tuple:
        """从左边开始的 pop"""
        self._check_history()
        date = self.date.pop(0)
        money = self.money.pop(0)
        value = self.value.pop(0)
        return date, money, value


class Wallet:
    def __init__(self, init_money=10000):
        self.date = []
        self.money = []
        self.init_money = init_money

    def _check_history(self):
        assert len(self.date) == len(self.money)

    def pay(self, money: float, date: datetime):
        self._check_history()
        # todo: 钱包钱不够
        self.date.append(date)
        self.money.append(-money)

    @property
    def history(self):
        return pd.DataFrame({'date': self.date, 'money': self.money})

    @property
    def balance(self):
        return self.init_money + sum(self.money)

    def __str__(self):
        gains = self.balance - self.init_money
        gains_rate = gains / self.init_money * 100.
        return f'init_money: {self.init_money}, balance: {self.balance}, gains: {gains}, gains_rate: {gains_rate:.2f}%'

    def gain(self, money: float, date):
        self._check_history()
        self.date.append(date)
        self.money.append(money)



class Account:
    def __init__(self, fund, fee, wallet):
        """账户

        用于绑定基金,费用,钱包和操作
        :param fund:
        :param fee:
        :param wallet:
        """
        self.fund = fund
        self.wallet = wallet
        self.fee = fee
        self.history = History()
        self.buy_history = History()
        self.sell_history = History()

    def buy(self, date: str, money):
        try:
            _date = datetime.strptime(date, '%Y-%m-%d')
            self.wallet.pay(money, date)  # 从钱包拿钱
            _money = money - self.fee.get_buy_fee_rate() * money  # 扣除申购税
            self.history.update(_date, _money, self._get_value(_date))  # 记录购买
            self.buy_history.update(_date, _money, self._get_value(_date))
        except Exception as e:
            print(e)
            print('Something Wrong while buying')

    def sell(self, date: str, stock: Optional[float] = None, money: Optional[float] = None):
        _date = datetime.strptime(date, '%Y-%m-%d')
        _value = self._get_value(_date)  # 当日单股价
        if (not stock) and (not money):
            print('need stock or money specified')
            return
        if money:
            stock = money / _value
        try:
            # todo: 判断 stock 不足
            left_stock = stock
            money = 0.  # 扣除费用的钱，进入钱包
            while True:
                pop_date, pop_money, pop_value = self.history.pop()  # 最开始的
                pop_stock = pop_money / pop_value
                if pop_stock >= left_stock:
                    money += (1 - self.fee.get_sell_fee_rate(_date - pop_date)) * left_stock * _value
                    left_stock = pop_stock - left_stock
                    left_money = left_stock * pop_value  # 剩下的股份按那时单价放回
                    self.history.update(pop_date, left_money, pop_value, head=True)
                    break
                else:
                    left_stock -= pop_stock
            self.sell_history.update(_date, money, _value)
            self.wallet.gain(money, date)  # 卖出的钱放到钱包
        except Exception as e:
            print(e)
            print('Something Wrong while selling')

    def _get_value(self, date):
        return self.fund.value[self.fund.date.index(date)]

    @property
    def invest(self):
        return self.history.get_invest()

    @property
    def asset(self):
        return self.history.get_asset(self._get_value(max(self.fund.date)))

    @property
    def gain(self):
        return self.asset - self.invest

    @property
    def stock(self):
        return self.history.get_stock()

    def __repr__(self):
        return repr(self.history)

    def __str__(self):
        return repr(self)

    def _plot(self, fund_df, buy_df, sell_df, days: Optional[int] = None):
        if days:
            fund_df = fund_df[-days:]
            buy_df = buy_df[-days:]
            sell_df = sell_df[-days:]
        return (ggplot() +
                geom_line(aes(x='date', y='value'), size=1, color='green', data=fund_df) +
                geom_point(aes(x='date', y='value'), size=1, color='red', data=buy_df) +
                geom_point(aes(x='date', y='value'), size=1, color='blue', data=sell_df) +
                scale_x_date(date_labels="%m-%d", date_breaks="1 week") +
                xlab("Days") +
                ylab("Values") +
                theme(figure_size=(20, 10))
                )

    def show(self, span: str = 'all'):
        if span == 'month':
            return self._plot(self.fund.df, self.buy_history.df, self.sell_history.df, 30)
        elif span == 'year':
            return self._plot(self.fund.df, self.buy_history.df, self.sell_history.df, 365)
        else:
            return self._plot(self.fund.df, self.buy_history.df, self.sell_history.df, None)


class Strategy:
    def __init__(self, account: Account, goal: float):
        self.account = account
        self.state = self.account.history
        self.goal = goal

    def buy(self, up: Tuple[bool, float] = (True, 0.1)):
        gain = self.account.gain


if __name__ == '__main__':
    CODE = '007464'
    fund = Fund(CODE)
    fund.analysis()
    fee = Fee()
    wallet = Wallet(10000)
    account = Account(fund, fee, wallet)
    buy_df = pd.read_csv('buy.csv')
    sell_df = pd.read_csv('sell.csv')
    for i, row in buy_df.iterrows():
        account.buy(date=row['date'], money=row['money'])
    for i, row in sell_df.iterrows():
        account.sell(date=row['date'], stock=row['stock'])
    # strategy = Strategy(account)

    print(f'account: \n{account}')
    print(f'invest: {account.invest}')
    print(f'stock: {account.stock}')
    print(f'asset: {account.asset}')
    print(f'gain: {account.gain}')
    print(f'wallet: {wallet}')
    print(f'wallet history: \n{wallet.history}')

    print(account.show('month'))
