import logging
from pathlib import Path


from fund.utils import get_config, get_logger
from fund import Fund

log = get_logger(__name__)
log.setLevel(logging.INFO)

def analysis(conf: dict):
    analysis_path = conf['analysis_path']
    fund_path = conf['fund_path']
    log.info(f'Get Fund Images and Reports:')
    for fund_db_path in Path(fund_path).iterdir():
        fund = Fund(fund_db_path)
        log.info(f'{fund.latest_day.date()}: {fund.name}-{fund.code}')
        fund.show(parent=analysis_path)  # 输出图片




if __name__ == '__main__':
    conf = get_config('config.yml')
    log.info('分析基金...')
    analysis(conf)
