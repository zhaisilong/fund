import logging
from collections import defaultdict
from pathlib import Path

from fund.utils import get_config, get_logger
from fund.core import Trace, Fund, FinanceReporter


log = get_logger(__name__)
log.setLevel(logging.INFO)




def track(conf: dict):
    track_path = conf['track_path']
    fund_path = conf['fund_path']

    # process with buy fee rates
    buy_fee = conf['buy_fee']
    buy_fee_dict = defaultdict(lambda: 0.0015)
    for k, v in buy_fee.items():
        buy_fee_dict[str(k)] = v  # make sure the key is a string

    # 生成总报告
    investments = []
    values = []
    gains = []
    for track in Path(track_path).iterdir():
        if track.is_file():
            fund = Fund(Path(fund_path) / track.name)
            log.info(f"处理 {fund.latest_day.date()}: {fund.name}-{fund.code}")
            trace = Trace(track, fund, buy_fee_dict[fund.code])
            trace.show(track_path)
            investments.append(trace.investment)
            values.append(trace.value)
            gains.append(trace.gain)
    # 输出总报告
    file = Path(track_path) / 'reports' / 'finance.txt'
    finance_reporter = FinanceReporter(investments, gains, values)
    finance_reporter.to_txt(file)


if __name__ == '__main__':
    conf = get_config('config.yml')
    log.info('导入买入卖出的数据...')
    track(conf)
