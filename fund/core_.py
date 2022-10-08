from typing import Tuple, Optional
from datetime import datetime
import pandas as pd

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
