import logging

from fund.utils import get_fund, get_config, get_logger

log = get_logger(__name__)
log.setLevel(logging.INFO)


def crawl(conf):
    codes = conf['codes']
    fund_path = conf['fund_path']
    for code in codes:
        get_fund(code, fund_path)


if __name__ == '__main__':
    conf = get_config('config.yml')
    log.info('爬取信息...')
    crawl(conf)
