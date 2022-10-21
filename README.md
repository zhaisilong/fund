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

全局跟踪
--------

```{=rst}
投资总金额：132.00元
卖出收益(扣税后)：0.00
基金价值：131.85元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：-0.11%

```
中欧互联网先锋混合A-010213
--------------------------

```{=rst}
投资总金额：16.00元
股份数：23.96份
当前每股单价：0.65元/份
卖出收益(扣税后)：0.00
基金价值：15.62元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：-2.38%
池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-14  23.962802    7 days    0.5  0.6667  -2.234888
按低值出售的池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-14  23.962802    7 days    0.5  0.6667  -2.234888

```
![010213](data/trace/imgs/中欧互联网先锋混合A-010213.png)

广发医药健康混合A-010110
------------------------

```{=rst}
投资总金额：16.00元
股份数：30.34份
当前每股单价：0.58元/份
卖出收益(扣税后)：0.00
基金价值：17.57元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：9.82%
池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-11  30.338017   10 days    0.5  0.5266   9.988606
按低值出售的池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-11  30.338017   10 days    0.5  0.5266   9.988606

```
![010110](data/trace/imgs/广发医药健康混合A-010110.png)

招商中证白酒指数(LOF)A-161725
-----------------------------

```{=rst}
投资总金额：72.00元
股份数：68.67份
当前每股单价：1.03元/份
卖出收益(扣税后)：0.00
基金价值：70.70元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：-1.81%
池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-12  18.646757    9 days    0.5  1.0715  -3.910406
1 2022-10-13  13.236797    8 days    0.5  1.0566  -2.555366
2 2022-10-18  13.275748    3 days    1.5  1.0535  -2.268628
3 2022-10-19  23.508187    2 days    1.5  1.0199   0.951074
按低值出售的池子:
        date      stock day_delta  fee/%   value  improve/%
0 2022-10-12  18.646757    9 days    0.5  1.0715  -3.910406
1 2022-10-13  13.236797    8 days    0.5  1.0566  -2.555366
2 2022-10-18  13.275748    3 days    1.5  1.0535  -2.268628
3 2022-10-19  23.508187    2 days    1.5  1.0199   0.951074

```
![161725](data/trace/imgs/招商中证白酒指数(LOF)A-161725.png)

汇添富上证综合指数-470007
-------------------------

```{=rst}
投资总金额：28.00元
股份数：28.85份
当前每股单价：0.97元/份
卖出收益(扣税后)：0.00
基金价值：27.96元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：-0.15%
池子:
        date      stock day_delta  fee/%  value  improve/%
0 2022-10-13  14.418557    8 days    0.5  0.970  -0.103093
1 2022-10-20  14.433437    1 days    1.5  0.969   0.000000
按低值出售的池子:
        date      stock day_delta  fee/%  value  improve/%
0 2022-10-13  14.418557    8 days    0.5  0.970  -0.103093
1 2022-10-20  14.433437    1 days    1.5  0.969   0.000000

```
![470007](data/trace/imgs/汇添富上证综合指数-470007.png)
