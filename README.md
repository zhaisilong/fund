[![docs](https://readthedocs.org/projects/fund/badge/?version=latest)](https://fund.readthedocs.io/zh_CN/latest/)
[![stars](https://shields.io/github/stars/zhaisilong/fund?style=social)](https://github.com/zhaisilong/fund)

前言
====

-   基于 Python 的量化投资基金的仓库.
-   本仓库所有的信息均不构成投资建议.
-   如果你对次项目感兴趣,欢迎右上角点赞.

安装
====

``` {.bash}
conda create -nfund python=3.8
# 深度学习 pytorch 套装
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

使用
====

快速入手
--------

``` {.bash}
bash pipeline.sh
```

基本操作
--------

``` {.bash}
python crawl.py  # 爬取基金的信息
python analysis.py  # 基金分析
python track.py  # 基金跟踪
python predict.py  # 基金预测
python strtegy.py  # 制定策略
```

跟踪情况
========

中欧互联网先锋混合A-010213
--------------------------

```{=rst}
投资总金额：16.00元
股份数：23.96份
当前每股单价：0.67元/份
卖出收益(扣税后)：0.00元
基金价值：15.99元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：-0.06%
池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-14  23.962802    4 days    1.5  0.6667   0.089996
按低值出售的池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-14  23.962802    4 days    1.5  0.6667   0.089996

```
![010213](data/trace/imgs/中欧互联网先锋混合A-010213.png)

广发医药健康混合A-010110
------------------------

```{=rst}
投资总金额：16.00元
股份数：30.34份
当前每股单价：0.59元/份
卖出收益(扣税后)：0.00元
基金价值：17.77元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：11.06%
池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-11  30.338017    7 days    0.5  0.5266   11.22294
按低值出售的池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-11  30.338017    7 days    0.5  0.5266   11.22294

```
![010110](data/trace/imgs/广发医药健康混合A-010110.png)

招商中证白酒指数(LOF)A-161725
-----------------------------

```{=rst}
投资总金额：34.00元
股份数：31.88份
当前每股单价：1.05元/份
卖出收益(扣税后)：0.00元
基金价值：33.59元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：-1.21%
池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-12  18.646757    6 days    1.5  1.0715  -1.679888
1 2022-10-13  13.236797    5 days    1.5  1.0566  -0.293394
按低值出售的池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-12  18.646757    6 days    1.5  1.0715  -1.679888
1 2022-10-13  13.236797    5 days    1.5  1.0566  -0.293394

```
![161725](data/trace/imgs/招商中证白酒指数(LOF)A-161725.png)

汇添富上证综合指数-470007
-------------------------

```{=rst}
投资总金额：14.00元
股份数：14.42份
当前每股单价：0.99元/份
卖出收益(扣税后)：0.00元
基金价值：14.22元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：1.55%
池子:
        date      stock day_delta  fee/%  value  improve/%
0 2022-10-13  14.418557    5 days    1.5   0.97   1.649485
按低值出售的池子:
        date      stock day_delta  fee/%  value  improve/%
0 2022-10-13  14.418557    5 days    1.5   0.97   1.649485

```
![470007](data/trace/imgs/汇添富上证综合指数-470007.png)
