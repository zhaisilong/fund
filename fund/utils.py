import logging
import time
from datetime import datetime
from pathlib import Path
from typing import List, Union

import execjs
import pandas as pd
import requests
import yaml
from rich.logging import RichHandler


def get_logger(name):
    """获取一个 Rich 美化的 Logger"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(name)s: %(message)s',
        handlers=[RichHandler(
            rich_tracebacks=True,
        )])
    return logging.getLogger(name)


log = get_logger(__name__)


def _x2date(x: int):
    assert isinstance(x, int)
    return datetime.fromtimestamp(x / 1000)


def _get_url(fscode):
    head = 'http://fund.eastmoney.com/pingzhongdata/'  # 东方财富
    tail = '.js?v=' + time.strftime("%Y%m%d%H%M%S", time.localtime())
    return head + fscode + tail


def get_fund(fscode: str, parent: str = '.'):
    """获取基金数据,写入 csv 文件
    :param code: 基金代码
    """
    parent_path = Path(parent)
    parent_path.mkdir(exist_ok=True)
    content = requests.get(_get_url(fscode))
    jsContent = execjs.compile(content.text)
    name = jsContent.eval('fS_name')
    code = jsContent.eval('fS_code')
    fund_path = parent_path / f'{name}-{code}.csv'
    net_worth_trend = jsContent.eval('Data_netWorthTrend')  # 单位净值走势
    pd.DataFrame({'date': [_x2date(day['x']) for day in net_worth_trend],
                  'value': [day['y'] for day in net_worth_trend]}).to_csv(fund_path)
    log.info(f'{_x2date(net_worth_trend[-1]["x"]).date()}: {name}-{code}')


def get_config(conf_path: str):
    # 基金分析
    with open(conf_path) as f:
        conf = yaml.full_load(f)
    return conf

def path2name(path: Union[str,Path]):
    if isinstance(path, str):
        _path = Path(path)
    elif isinstance(path, Path):
        _path = path
    name = _path.name.split('-')[0]
    code = _path.name.split('.')[0].split('-')[-1]
    return name, code



