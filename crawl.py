import logging

from fund.utils import get_fund, get_config, get_logger

log = get_logger(__name__)
log.setLevel(logging.INFO)


def crawl(conf):
    codes = conf['codes']
    fund_path = conf['fund_path']
    for code in codes:
        try:
            get_fund(code, fund_path)
        except Exception as e:
            log.warning(e)
            log.warning(f"error when fetching {codes}")


if __name__ == '__main__':
    conf = get_config('config.yml')
    log.info('爬取信息...')
    crawl(conf)
