
[![](https://readthedocs.org/projects/fund/badge/?version=latest)](https://fund.readthedocs.io/zh_CN/latest/)[![stars](https://shields.io/github/stars/zhaisilong/fund?style=social)](https://github.com/zhaisilong/fund)

## 前言

- 基于 Python 的量化投资基金的仓库.
- 投资需谨慎,本仓库所有的信息均不构成投资建议.
- 如果你对次项目感兴趣,欢迎右上角点赞.

## 安装

```bash
conda create -nfund python=3.8
# 深度学习 pytorch 套装
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

## 使用

### 爬取基金的信息

```bash
python crawl.py
```

信息保存在 `data/funds`

### 基金分析

- 可以得到基金的走势图
- 横轴分界线为: 3,7 分界线
- 纵轴分界线为: 周月年分界线
- 报告信息: 值的周期信息(年月周)
- 信息保存在 `data/funds`

```bash
python analysis.py
```

### 基金跟踪

- 你需要根据模板写入你的买入卖出信息到 `data/trace/` 下
- 名字命名与 `data/funds` 中的基金保持一致
- 可以得到基金跟踪的走势图
- 以及一些收益分析信息报告

```bash
python track.py
```

## 设计思路

- 创建一个可以记录买入,卖出的量化模拟交易的 Python 软件.
- 目前没有找到相关的库和包,所以一切都是从零开始学习,包括基金的一些基础知识.

### 数据库关系建模

- Fund
  - 基金值-时间
- Trace
  - 操作-时间
  - 操作有买入,卖出
  - 时间,操作类型,操作量(金额,股份数)
  - 操作的键是时间 + 操作类型:
    - 这里隐含的假设是,每天只能买入一次,或者卖出一次.
- Gain
  - 收益-操作(Trace)
  - 每次操作都会更新收益值
  - 增加 减少 不变
- Account
  - 账户用于绑定基金,钱包和操作
  - 操作在账户上进行
- Wallet: 投资的观察差窗口
  - 每个用户只能有一个钱包,用于个人总投资的计算
  - 有初始金额
- Fee: 用于基金的手续费计算
  - 申购费: 一般固定
  - 卖出费用: 一般随时间变化

### 数据库实现

- 本仓库个人使用,因此数据量比较少,因此采用简单的文本表示数据.
- 基本确定为 pandas + csv.
- 配置文件使用 yaml.

## 基金分析

### 相似度分析

#### 基于序列特征

#### 基于统计

## 人工智能时序预测

- [这里使用 Meta 的 Kats 包,作为后端引擎](https://github.com/facebookresearch/Kats)

## Updates

### 未来工作

1. 基础的可交互性
2. 基于强化学习的交易策略
3. 引入 AI 时序预测
4. 较为全面的投资策略, latex 成书

### 2022-10-11

- 改善命令框提示（增加日期指示）
- 修复追踪 Pandas 索引错误

### 2022-10-10

- 尝试了 kats，出现了许多的 bug，因此放弃。
- 转用 gitstar 15k 的 [prophet](https://facebook.github.io/prophet/docs/quick_start.html#python-api)
- 先学习一周 prophet

### 2022-10-9

- 完成基本系统,优化代码
  - 信息收集系统
  - 基金分析系统
  - 基金跟踪系统

### 2022-10-7

- 加入日志系统
- 数据库建模 1/3

### 2022-10-5

- 能够爬取基金并分析相关的基金的信息.
- 基金买入以及止盈的策略学习, 写入 latex.

### 2022-9-21

- 创建仓库,完成基本测试

## Debugs

- 中文字体修复: `bin/fix_matplotlib.py`

## 参考

- [一篇文章详细讲解爬虫入门，以爬取基金净值为例｜Python 主题月](https://juejin.cn/post/6986511668289208356)