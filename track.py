import logging
from pathlib import Path

from fund.utils import get_config, get_logger
from fund.core import Trace, Fund

log = get_logger(__name__)
log.setLevel(logging.INFO)


def track(conf: dict):
    track_path = conf['track_path']
    fund_path = conf['fund_path']
    for track in Path(track_path).iterdir():
        if track.is_file():
            fund = Fund(Path(fund_path) / track.name)
            trace = Trace(track, fund)
            trace.show(track_path)


if __name__ == '__main__':
    conf = get_config('config.yml')
    log.info('导入买入卖出的数据...')
    track(conf)
