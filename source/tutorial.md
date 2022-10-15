# 教程

## 基金爬取

```bash
python crawl.py
```

信息保存在 `data/funds`

## 基金分析

```bash
python analysis.py
```

- 可以得到基金的走势图
- 横轴分界线为: 3,7 分界线
- 纵轴分界线为: 周月年分界线
- 报告信息: 值的周期信息(年月周)
- 信息保存在 `data/funds`

## 基金跟踪

```bash
python track.py
```

- 你需要根据模板写入你的买入卖出信息到 `data/trace/` 下
- 名字命名与 `data/funds` 中的基金保持一致
- 可以得到基金跟踪的走势图
- 以及一些收益分析信息报告

## 基金预测

```bash
python predict.py
```

- 基于 prophet 的机器学习预测