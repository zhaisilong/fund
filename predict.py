import logging
from pathlib import Path

import pandas as pd
from prophet import Prophet
from fund.utils import get_config, get_logger

from fund import Fund

log = get_logger(__name__)
log.setLevel(logging.INFO)

def predict(conf: dict):
    m = Prophet
    air_passengers_df = pd.read_csv(Path('data/others/air_passengers.csv'))
    multi_ts_df = pd.read_csv(Path("data/others/multi_ts.csv"), index_col=0)
    air_passengers_df.columns = ["time", "value"]

    air_passengers_ts = TimeSeriesData(air_passengers_df)
    multi_ts = TimeSeriesData(multi_ts_df)

    # create a model param instance
    params = ProphetParams(seasonality_mode='multiplicative')  # additive mode gives worse results
    # create a prophet model instance
    m = ProphetModel(air_passengers_ts, params)
    # fit model simply by calling m.fit()
    m.fit()
    # make prediction for next 30 month
    fcst = m.predict(steps=30, freq="MS")
    # the predict method returns a dataframe as follows
    print(fcst.head())



    # analysis_path = conf['analysis_path']
    # fund_path = conf['fund_path']
    # for fund_db_path in Path(fund_path).iterdir():
    #     fund = Fund(fund_db_path)
    #     log.info(f'Get Fund Images and Reports for {fund_db_path}')
    #     fund.show(parent=analysis_path)  # 输出图片




if __name__ == '__main__':
    conf = get_config('config.yml')
    log.info('人工智能预测...')
    predict(conf)
