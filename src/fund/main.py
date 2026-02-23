from collections import defaultdict
import click

from pathlib import Path
from loguru import logger

from fund.utils import get_config, get_fund, get_options, write_data
from fund.summary import SummaryOptions, write_summary


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--config_path", type=str, default=Path.cwd() / "config.yml", help="基金配置路径"
)
def crawl(config_path):
    conf = get_config(config_path)
    logger.info(f"crawl (load config from {config_path})")

    codes = conf["codes"]
    fund_path = conf["fund_path"]
    for code in codes:
        try:
            get_fund(code, fund_path)
        except Exception as e:
            logger.exception(e)
            logger.error(f"error when fetching {code}")


@cli.command()
@click.option(
    "--config_path", type=str, default=Path.cwd() / "config.yml", help="基金配置路径"
)
def analysis(config_path):
    from fund import Fund

    conf = get_config(config_path)
    analysis_path = conf["analysis_path"]
    fund_path = Path(conf["fund_path"])
    logger.info(f"analysis (load config from {config_path})")

    for fund_db_path in fund_path.iterdir():
        fund = Fund(fund_db_path)
        logger.info(f"{fund.latest_day.date()}: {fund.name}-{fund.code}")
        fund.show(parent=analysis_path)  # 输出图片

@cli.command()
@click.option(
    "--config_path", type=str, default=Path.cwd() / "config.yml", help="基金配置路径"
)
def track(config_path):
    from fund import Fund, Trace, FinanceReporter

    conf = get_config(config_path)
    track_path = conf["track_path"]
    fund_path = Path(conf["fund_path"])
    logger.info(f"track (load config from {config_path})")
    
    buy_fee = conf["buy_fee"]
    buy_fee_dict = defaultdict(lambda: 0.0015)
    for k, v in buy_fee.items():
        buy_fee_dict[str(k)] = v  # make sure the key is a string
        
    # 生成总报告
    investments = []
    values = []
    gains = []
    for track in Path(track_path).iterdir():
        if track.is_file() and track.with_suffix('.csv'):  # only read csv files
            fund = Fund(fund_path / track.name)
            logger.info(f"处理 {fund.latest_day.date()}: {fund.name}-{fund.code}")
            trace = Trace(track, fund, buy_fee_dict[fund.code])
            trace.show(track_path)
            investments.append(trace.investment)
            values.append(trace.value)
            gains.append(trace.gain)
            
    # 输出总报告
    if not investments:
        logger.info("没有数据,不做报告")
        return
    file = Path(track_path) / 'reports' / 'finance.txt'
    finance_reporter = FinanceReporter(investments, gains, values)
    finance_reporter.to_txt(file)

@cli.command()
@click.option(
    "--trace_dir", type=str, default=Path.cwd() / "data/trace", help="基金跟踪路径"
)
def record(trace_dir):
    trace_dir = Path(trace_dir)
    trace_dir.mkdir(exist_ok=True, parents=True)
    
    file = get_options(trace_dir)
    while (file != "q") or (not file):
        try:
            write_data(file)
            file = get_options(trace_dir)
        except KeyboardInterrupt:
            exit(1)


@cli.command()
@click.option("--code_id", type=str, required=True, help="基金代码")
@click.option(
    "--config_path", type=str, default=Path.cwd() / "config.yml", help="基金配置路径"
)
@click.option(
    "--output_dir", type=str, default=Path.cwd() / "data/agent", help="输出路径"
)
@click.option(
    "--include_values",
    type=bool,
    default=True,
    help="是否包含全量 date/value 序列",
)
def summary(code_id, config_path, output_dir, include_values):
    options = SummaryOptions(
        code_id=code_id,
        config_path=Path(config_path),
        funds_dir=Path("data/funds"),
        trace_dir=Path("data/trace"),
        analysis_reports_dir=Path("data/analysis/reports"),
        output_dir=Path(output_dir),
        include_values=include_values,
    )
    summary_path = write_summary(options)
    logger.info(f"summary saved: {summary_path}")
