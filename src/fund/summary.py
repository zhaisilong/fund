import csv
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from fund.utils import get_config, path2name

PERIOD_WINDOWS = {
    "7d": 7,
    "30d": 30,
    "90d": 90,
    "180d": 180,
    "1y": 365,
}


@dataclass
class SummaryOptions:
    code_id: str
    config_path: Path
    funds_dir: Path
    trace_dir: Path
    analysis_reports_dir: Path
    output_dir: Path
    include_values: bool = True


def _percent_change(latest: float, previous: float) -> float:
    if not previous or previous == 0:
        return 0.0
    return (latest - previous) / previous * 100


def _read_fund_rows(fund_path: Path) -> List[Tuple[datetime, float]]:
    rows: List[Tuple[datetime, float]] = []
    with fund_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = datetime.strptime(row["date"], "%Y-%m-%d")
            value = float(row["value"])
            rows.append((date, value))
    rows.sort(key=lambda x: x[0])
    return rows


def _read_trace_rows(trace_path: Path) -> List[Dict[str, Any]]:
    if not trace_path.exists():
        return []
    rows: List[Dict[str, Any]] = []
    with trace_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(
                {
                    "date": row["date"],
                    "operation": row["operation"],
                    "quantity": float(row["quantity"]),
                }
            )
    return rows


def _parse_analysis_report(report_path: Path) -> Dict[str, Dict[str, float]]:
    tech = {
        "weekday_cum_change_percent": {},
        "year_cum_change_percent": {},
        "month_cum_change_percent": {},
    }
    if not report_path.exists():
        return tech

    section: Optional[str] = None
    for raw in report_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("星期一到星期五的累计涨幅"):
            section = "weekday"
            continue
        if line.startswith("年份的累计涨幅"):
            section = "year"
            continue
        if line.startswith("月的累计涨幅"):
            section = "month"
            continue
        if ":" in line and line.endswith("%") and section:
            key, val = line.split(":", 1)
            try:
                num = float(val.strip().rstrip("%"))
            except ValueError:
                continue
            if section == "weekday":
                tech["weekday_cum_change_percent"][key.strip()] = num
            elif section == "year":
                tech["year_cum_change_percent"][key.strip()] = num
            elif section == "month":
                tech["month_cum_change_percent"][key.strip()] = num
    return tech


def _parse_track_report(report_path: Path) -> Dict[str, Any]:
    if not report_path.exists():
        return {}
    text = report_path.read_text(encoding="utf-8")
    result: Dict[str, Any] = {}
    patterns = {
        "investment": r"投资总金额：([0-9.]+)元",
        "holdings": r"股份数：([0-9.]+)份",
        "latest_value_stock": r"当前每股单价：([0-9.]+)元/份",
        "gain": r"卖出收益\(扣税后\)：([0-9.]+)",
        "current_value": r"基金价值：([0-9.]+)元",
        "return_percent": r"收益率\(.+?\)：([0-9.\-]+)%",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            try:
                result[key] = float(match.group(1))
            except ValueError:
                continue
    return result


def _parse_finance_report(report_path: Path) -> Dict[str, Any]:
    if not report_path.exists():
        return {}
    text = report_path.read_text(encoding="utf-8")
    result: Dict[str, Any] = {}
    patterns = {
        "investment_total": r"投资总金额：([0-9.]+)元",
        "gain_total": r"卖出收益\(扣税后\)：([0-9.]+)",
        "value_total": r"基金价值：([0-9.]+)元",
        "return_percent": r"收益率\(.+?\)：([0-9.\-]+)%",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            try:
                result[key] = float(match.group(1))
            except ValueError:
                continue
    return result


def build_summary(options: SummaryOptions) -> Dict[str, Any]:
    config = get_config(options.config_path)

    fund_path: Optional[Path] = None
    for p in options.funds_dir.glob(f"*-{options.code_id}.csv"):
        fund_path = p
        break
    if not fund_path:
        raise FileNotFoundError(f"fund file not found for code_id={options.code_id}")

    name, code = path2name(fund_path)
    fund_rows = _read_fund_rows(fund_path)
    latest_date, latest_value = fund_rows[-1]
    first_date, _ = fund_rows[0]
    values = [v for _, v in fund_rows]

    data_points = len(values)
    history_days = (latest_date - first_date).days
    min_value = min(values)
    max_value = max(values)
    latest_delta_percent = None
    if data_points > 1:
        latest_delta_percent = _percent_change(values[-1], values[-2])

    period_returns: Dict[str, Optional[float]] = {}
    for label, window in PERIOD_WINDOWS.items():
        if data_points > window:
            prev = values[-1 - window]
            period_returns[label] = _percent_change(values[-1], prev)
        else:
            period_returns[label] = None

    trace_path = options.trace_dir / f"{name}-{code}.csv"
    trace_rows = _read_trace_rows(trace_path)

    report_path = options.analysis_reports_dir / f"{name}-{code}.txt"
    technical_values = _parse_analysis_report(report_path)

    track_report_path = options.trace_dir / "reports" / f"{name}-{code}.txt"
    track_report = _parse_track_report(track_report_path)

    finance_report_path = options.trace_dir / "reports" / "finance.txt"
    finance_report = _parse_finance_report(finance_report_path)

    buy_fee_map = config.get("buy_fee", {})
    buy_fee = float(buy_fee_map.get(code, 0.0015))

    config_summary = {
        "buy_fee": buy_fee,
        "buy_fee_default": 0.0015,
    }
    summary: Dict[str, Any] = {
        "fund": {
            "code": code,
            "name": name,
            "latest_date": latest_date.date().isoformat(),
            "latest_value": latest_value,
            "data_points": data_points,
            "history_days": history_days,
            "min_value": min_value,
            "max_value": max_value,
            "latest_delta_percent": latest_delta_percent,
            "period_returns": period_returns,
        },
        "trace": {
            "code": code,
            "buy_fee": buy_fee,
            "operations": trace_rows,
            "report": track_report,
        },
        "technical_values": technical_values,
        "finance_report": finance_report,
        "config": config_summary,
    }

    if options.include_values:
        summary["fund"]["all_values"] = [
            {"date": d.date().isoformat(), "value": v} for d, v in fund_rows
        ]

    return summary


def write_summary(options: SummaryOptions) -> Path:
    summary = build_summary(options)
    options.output_dir.mkdir(parents=True, exist_ok=True)
    out_path = options.output_dir / f"{options.code_id}_summary.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    return out_path
