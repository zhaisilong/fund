import logging
import os
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
    """获取 URL 访问链接
    :param fscode: 基金代码
    """
    head = 'http://fund.eastmoney.com/pingzhongdata/'  # 东方财富
    tail = '.js?v=' + time.strftime("%Y%m%d%H%M%S", time.localtime())
    return head + fscode + tail


def get_fund(fscode: str, parent: str = '.'):
    """获取基金数据,写入 csv 文件
    :param code: 基金代码
    """
    time.sleep(1)  # 防止被反爬虫
    # todo: 检查文件的最新日期
    # for file in os.listdir(parent):
    #     if file.endswith('.csv'):
    #         file.rstrip('.csv').split('-')[-1]
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
    """导入基金的 yaml 配置
    :param conf_path: 基金配置路径
    """
    with open(conf_path) as f:
        conf = yaml.full_load(f)
    return conf


def path2name(path: Union[str, Path]):
    """从路径中读取基金名字与代码
    :param path: Path
    """
    if isinstance(path, str):
        _path = Path(path)
    elif isinstance(path, Path):
        _path = path
    name = _path.name.split('-')[0]
    code = _path.name.split('.')[0].split('-')[-1]
    return name, code
