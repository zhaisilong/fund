from typing import List
import logging
from fund.utils import get_fund, get_config, get_logger
from fund import Fund, Wallet
from pathlib import Path

log = get_logger(__name__)
log.setLevel(logging.INFO)




# def track(conf: dict):
#     wallet = Wallet(10000)
#     account = Account(fund, fee, wallet)
#
#     pass




def main(conf_path: str):
    log.info(f'导入配置: {conf_path}')
    conf = get_config(conf_path)

    crawl(conf=conf)
    # 分析基金
    # analysis(conf=conf)

    # 跟踪购买记录
    # track(conf=conf)


if __name__ == "__main__":
    main('config.yml')


    # buy_df = pd.read_csv('buy.csv')
    # sell_df = pd.read_csv('sell.csv')
    # for i, row in buy_df.iterrows():
    #     account.buy(date=row['date'], money=row['money'])
    # for i, row in sell_df.iterrows():
    #     account.sell(date=row['date'], stock=row['stock'])
    # # strategy = Strategy(account)
    #
    # print(f'account: \n{account}')
    # print(f'invest: {account.invest}')
    # print(f'stock: {account.stock}')
    # print(f'asset: {account.asset}')
    # print(f'gain: {account.gain}')
    # print(f'wallet: {wallet}')
    # print(f'wallet history: \n{wallet.history}')
    #
    # print(account.show('month'))
