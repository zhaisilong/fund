[![docs](https://readthedocs.org/projects/fund/badge/?version=latest)](https://fund.readthedocs.io/zh_CN/latest/)
[![stars](https://shields.io/github/stars/zhaisilong/fund?style=social)](https://github.com/zhaisilong/fund)

# 前言

-   基于 Python 的量化投资基金的仓库.
-   本仓库所有的信息均不构成投资建议.
-   如果你对次项目感兴趣,欢迎右上角点赞.

# 安装

``` bash
conda create -nfund python=3.8
# 深度学习 pytorch 套装
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

安装 [java runtime]{.title-ref}

``` bash
brew install java
brew install node
```

安装 [pandoc]{.title-ref}

``` bash
brew install pandoc  # for Darwin
sudo apt install pandoc  # for Ubuntu
```

# 使用

## 快速入手

``` bash
bash pipeline.sh
```

## 基本操作

``` bash
python crawl.py  # 爬取基金的信息
python analysis.py  # 基金分析
python track.py  # 基金跟踪
python predict.py  # 基金预测
python strtegy.py  # 制定策略
```

# 跟踪情况

## 全局跟踪

``` {literal=""}
投资总金额：3217.00元
卖出收益(扣税后)：207.03
基金价值：3181.20元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：5.32%
```

## 中欧互联网先锋混合A-010213

``` {literal=""}
投资总金额：480.00元
股份数：652.47份
当前每股单价：0.78元/份
卖出收益(扣税后)：0.00
基金价值：508.41元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：5.92%
池子:
         date      stock day_delta  fee/%   value  improve/%
0  2022-10-14  23.962802  185 days    0.5  0.6667  16.874156
1  2022-11-15  22.542684  153 days    0.5  0.7087   9.947792
2  2022-11-18  22.855508  150 days    0.5  0.6990  11.473534
3  2022-11-22  23.319223  146 days    0.5  0.6851  13.735221
4  2022-12-01  22.568159  137 days    0.5  0.7079  10.072044
5  2022-12-09  21.706522  129 days    0.5  0.7360   5.869565
6  2022-12-19  22.266202  119 days    0.5  0.7175   8.599303
7  2022-12-21  22.677076  117 days    0.5  0.7045  10.603265
8  2022-12-29  21.936015  109 days    0.5  0.7283   6.988878
9  2022-12-30  22.026748  108 days    0.5  0.7253   7.431408
10 2023-01-06  21.029354  101 days    0.5  0.7597   2.566803
11 2023-01-09  20.963128   98 days    0.5  0.7621   2.243800
12 2023-01-11  21.140664   96 days    0.5  0.7557   3.109700
13 2023-01-13  21.115517   94 days    0.5  0.7566   2.987047
14 2023-01-16  21.062624   91 days    0.5  0.7585   2.729071
15 2023-01-18  20.965879   89 days    0.5  0.7620   2.257218
16 2023-01-20  20.643494   87 days    0.5  0.7739   0.684843
17 2023-01-30  20.691620   77 days    0.5  0.7721   0.919570
18 2023-02-01  20.627502   75 days    0.5  0.7745   0.606843
19 2023-02-08  21.270137   68 days    0.5  0.7511   3.741180
20 2023-02-10  21.332621   66 days    0.5  0.7489   4.045934
21 2023-02-14  21.157463   62 days    0.5  0.7551   3.191630
22 2023-02-15  21.349726   61 days    0.5  0.7483   4.129360
23 2023-02-17  21.860974   59 days    0.5  0.7308   6.622879
24 2023-02-21  21.574612   55 days    0.5  0.7405   5.226199
25 2023-02-22  21.736054   54 days    0.5  0.7350   6.013605
26 2023-02-22  21.736054   54 days    0.5  0.7350   6.013605
27 2023-02-27  22.090708   49 days    0.5  0.7232   7.743363
28 2023-02-28  22.127424   48 days    0.5  0.7220   7.922438
29 2023-03-07  22.136622   41 days    0.5  0.7217   7.967299
按低值出售的池子:
         date      stock day_delta  fee/%   value  improve/%
0  2022-10-14  23.962802  185 days    0.5  0.6667  16.874156
1  2022-11-15  22.542684  153 days    0.5  0.7087   9.947792
2  2022-11-18  22.855508  150 days    0.5  0.6990  11.473534
3  2022-11-22  23.319223  146 days    0.5  0.6851  13.735221
4  2022-12-01  22.568159  137 days    0.5  0.7079  10.072044
5  2022-12-09  21.706522  129 days    0.5  0.7360   5.869565
6  2022-12-19  22.266202  119 days    0.5  0.7175   8.599303
7  2022-12-21  22.677076  117 days    0.5  0.7045  10.603265
8  2022-12-29  21.936015  109 days    0.5  0.7283   6.988878
9  2022-12-30  22.026748  108 days    0.5  0.7253   7.431408
10 2023-01-06  21.029354  101 days    0.5  0.7597   2.566803
11 2023-01-09  20.963128   98 days    0.5  0.7621   2.243800
12 2023-01-11  21.140664   96 days    0.5  0.7557   3.109700
13 2023-01-13  21.115517   94 days    0.5  0.7566   2.987047
14 2023-01-16  21.062624   91 days    0.5  0.7585   2.729071
15 2023-01-18  20.965879   89 days    0.5  0.7620   2.257218
16 2023-01-20  20.643494   87 days    0.5  0.7739   0.684843
17 2023-01-30  20.691620   77 days    0.5  0.7721   0.919570
18 2023-02-01  20.627502   75 days    0.5  0.7745   0.606843
19 2023-02-08  21.270137   68 days    0.5  0.7511   3.741180
20 2023-02-10  21.332621   66 days    0.5  0.7489   4.045934
21 2023-02-14  21.157463   62 days    0.5  0.7551   3.191630
22 2023-02-15  21.349726   61 days    0.5  0.7483   4.129360
23 2023-02-17  21.860974   59 days    0.5  0.7308   6.622879
24 2023-02-21  21.574612   55 days    0.5  0.7405   5.226199
25 2023-02-22  21.736054   54 days    0.5  0.7350   6.013605
26 2023-02-22  21.736054   54 days    0.5  0.7350   6.013605
27 2023-02-27  22.090708   49 days    0.5  0.7232   7.743363
28 2023-02-28  22.127424   48 days    0.5  0.7220   7.922438
29 2023-03-07  22.136622   41 days    0.5  0.7217   7.967299
```

![010213](data/trace/imgs/中欧互联网先锋混合A-010213.png)

## 广发医药健康混合A-010110

``` {literal=""}
投资总金额：765.00元
股份数：1183.04份
当前每股单价：0.62元/份
卖出收益(扣税后)：55.81
基金价值：735.97元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：3.50%
池子:
         date       stock day_delta  fee/%   value  improve/%
0  2022-11-21    1.880868  147 days    0.5  0.6004   3.614257
1  2022-11-22   27.318741  146 days    0.5  0.5848   6.378249
2  2022-11-23   27.842454  145 days    0.5  0.5738   8.417567
3  2022-11-28   28.416933  140 days    0.5  0.5622  10.654571
4  2022-12-01   27.431319  137 days    0.5  0.5824   6.816621
5  2022-12-02   27.668860  136 days    0.5  0.5774   7.741600
6  2022-12-09   94.277525  129 days    0.5  0.5931   4.889563
7  2022-12-19   27.866736  119 days    0.5  0.5733   8.512123
8  2023-01-06   24.943013  101 days    0.5  0.6405  -2.872756
9  2023-01-13   23.452730   94 days    0.5  0.6812  -8.675866
10 2023-01-16   22.822857   91 days    0.5  0.7000 -11.128571
11 2023-02-01   23.463064   75 days    0.5  0.6809  -8.635629
12 2023-02-08   24.078372   68 days    0.5  0.6635  -6.239638
13 2023-02-10   24.191399   66 days    0.5  0.6604  -5.799515
14 2023-02-13   23.987988   63 days    0.5  0.6660  -6.591592
15 2023-02-14   24.063865   62 days    0.5  0.6639  -6.296129
16 2023-02-15   44.582756   61 days    0.5  0.6495  -4.218630
17 2023-02-16   45.350822   60 days    0.5  0.6385  -2.568520
18 2023-02-17   25.099764   59 days    0.5  0.6365  -2.262372
19 2023-02-21   25.072191   55 days    0.5  0.6372  -2.369743
20 2023-02-27   25.842769   49 days    0.5  0.6182   0.630864
21 2023-02-28   25.533003   48 days    0.5  0.6257  -0.575356
22 2023-03-06   25.647777   42 days    0.5  0.6229  -0.128432
23 2023-03-07   26.074751   41 days    0.5  0.6127   1.534193
24 2023-03-07   26.074751   41 days    0.5  0.6127   1.534193
25 2023-03-22   26.805369   26 days    0.5  0.5960   4.379195
26 2023-03-27   61.049592   21 days    0.5  0.5888   5.655571
27 2023-04-03  237.821366   14 days    0.5  0.5710   8.949212
28 2023-04-04   97.465574   13 days    0.5  0.5737   8.436465
29 2023-04-17   36.916091    0 days    1.5  0.6221   0.000000
按低值出售的池子:
         date       stock day_delta  fee/%   value  improve/%
0  2022-10-18   26.773923  181 days    0.5  0.5967   4.256745
1  2022-11-21   26.608927  147 days    0.5  0.6004   3.614257
2  2022-11-22   27.318741  146 days    0.5  0.5848   6.378249
3  2022-11-23   27.842454  145 days    0.5  0.5738   8.417567
4  2022-12-01   27.431319  137 days    0.5  0.5824   6.816621
5  2022-12-02   27.668860  136 days    0.5  0.5774   7.741600
6  2022-12-09   94.277525  129 days    0.5  0.5931   4.889563
7  2022-12-19    4.781687  119 days    0.5  0.5733   8.512123
8  2023-01-06   24.943013  101 days    0.5  0.6405  -2.872756
9  2023-01-13   23.452730   94 days    0.5  0.6812  -8.675866
10 2023-01-16   22.822857   91 days    0.5  0.7000 -11.128571
11 2023-02-01   23.463064   75 days    0.5  0.6809  -8.635629
12 2023-02-08   24.078372   68 days    0.5  0.6635  -6.239638
13 2023-02-10   24.191399   66 days    0.5  0.6604  -5.799515
14 2023-02-13   23.987988   63 days    0.5  0.6660  -6.591592
15 2023-02-14   24.063865   62 days    0.5  0.6639  -6.296129
16 2023-02-15   44.582756   61 days    0.5  0.6495  -4.218630
17 2023-02-16   45.350822   60 days    0.5  0.6385  -2.568520
18 2023-02-17   25.099764   59 days    0.5  0.6365  -2.262372
19 2023-02-21   25.072191   55 days    0.5  0.6372  -2.369743
20 2023-02-27   25.842769   49 days    0.5  0.6182   0.630864
21 2023-02-28   25.533003   48 days    0.5  0.6257  -0.575356
22 2023-03-06   25.647777   42 days    0.5  0.6229  -0.128432
23 2023-03-07   26.074751   41 days    0.5  0.6127   1.534193
24 2023-03-07   26.074751   41 days    0.5  0.6127   1.534193
25 2023-03-22   26.805369   26 days    0.5  0.5960   4.379195
26 2023-03-27   61.049592   21 days    0.5  0.5888   5.655571
27 2023-04-03  237.821366   14 days    0.5  0.5710   8.949212
28 2023-04-04   97.465574   13 days    0.5  0.5737   8.436465
29 2023-04-17   36.916091    0 days    1.5  0.6221   0.000000
```

![010110](data/trace/imgs/广发医药健康混合A-010110.png)

## 招商中证白酒指数(LOF)A-161725

``` {literal=""}
投资总金额：440.00元
股份数：289.34份
当前每股单价：1.15元/份
卖出收益(扣税后)：146.31
基金价值：331.55元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：8.60%
池子:
         date      stock day_delta  fee/%   value  improve/%
0  2022-10-24  69.361521  175 days    0.5  0.9510  20.494217
1  2022-10-25  14.748497  174 days    0.5  0.9483  20.837288
2  2022-10-27  15.447316  172 days    0.5  0.9054  26.562845
3  2022-11-09  14.475264  159 days    0.5  0.9662  18.598634
4  2022-11-14  13.946949  154 days    0.5  1.0028  14.270044
5  2022-11-21  14.070423  147 days    0.5  0.9940  15.281690
6  2022-11-24  14.264151  144 days    0.5  0.9805  16.868944
7  2022-12-26  12.238362  112 days    0.5  1.1428   0.271264
8  2022-12-29  12.222319  109 days    0.5  1.1443   0.139823
9  2023-01-09  11.398533   98 days    0.5  1.2270  -6.609617
10 2023-02-08  11.655971   68 days    0.5  1.1999  -4.500375
11 2023-02-14  10.947088   62 days    0.5  1.2776 -10.308391
12 2023-02-21  10.928270   55 days    0.5  1.2798 -10.462572
13 2023-02-22  10.969412   54 days    0.5  1.2750 -10.125490
14 2023-03-06  11.170034   42 days    0.5  1.2521  -8.481751
15 2023-03-07  11.366111   41 days    0.5  1.2305  -6.875254
16 2023-04-14  30.125055    3 days    1.5  1.1275   1.631929
按低值出售的池子:
         date      stock day_delta  fee/%   value  improve/%
0  2022-10-12  18.646757  187 days    0.5  1.0715   6.943537
1  2022-10-13  13.236797  186 days    0.5  1.0566   8.451637
2  2022-10-18  13.275748  181 days    0.5  1.0535   8.770764
3  2022-10-19  23.508187  180 days    0.5  1.0199  12.354152
4  2022-10-20  23.286713  179 days    0.5  1.0296  11.295649
5  2022-10-24   7.603132  175 days    0.5  0.9510  20.494217
6  2022-11-09  14.475264  159 days    0.5  0.9662  18.598634
7  2022-11-14  13.946949  154 days    0.5  1.0028  14.270044
8  2022-11-21  14.070423  147 days    0.5  0.9940  15.281690
9  2022-11-24  14.264151  144 days    0.5  0.9805  16.868944
10 2022-12-26  12.238362  112 days    0.5  1.1428   0.271264
11 2022-12-29  12.222319  109 days    0.5  1.1443   0.139823
12 2023-01-09  11.398533   98 days    0.5  1.2270  -6.609617
13 2023-02-08  11.655971   68 days    0.5  1.1999  -4.500375
14 2023-02-14  10.947088   62 days    0.5  1.2776 -10.308391
15 2023-02-21  10.928270   55 days    0.5  1.2798 -10.462572
16 2023-02-22  10.969412   54 days    0.5  1.2750 -10.125490
17 2023-03-06  11.170034   42 days    0.5  1.2521  -8.481751
18 2023-03-07  11.366111   41 days    0.5  1.2305  -6.875254
19 2023-04-14  30.125055    3 days    1.5  1.1275   1.631929
```

![161725](data/trace/imgs/招商中证白酒指数(LOF)A-161725.png)

## 汇添富上证综合指数-470007

``` {literal=""}
投资总金额：154.00元
股份数：155.39份
当前每股单价：1.08元/份
卖出收益(扣税后)：0.00
基金价值：168.60元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：9.48%
池子:
         date      stock day_delta  fee/%  value  improve/%
0  2022-10-13  14.418557  186 days    0.5  0.970  11.855670
1  2022-10-20  14.433437  179 days    0.5  0.969  11.971104
2  2022-11-03  14.706625  165 days    0.5  0.951  14.090431
3  2022-11-07  14.315251  161 days    0.5  0.977  11.054248
4  2022-11-08  14.388889  160 days    0.5  0.972  11.625514
5  2022-11-18  14.170213  150 days    0.5  0.987   9.929078
6  2022-12-19  13.916418  119 days    0.5  1.005   7.960199
7  2022-12-21  14.084592  117 days    0.5  0.993   9.264854
8  2022-12-23  14.127273  115 days    0.5  0.990   9.595960
9  2023-02-10  13.409396   66 days    0.5  1.043   4.026846
10 2023-02-16  13.422265   60 days    0.5  1.042   4.126679
按低值出售的池子:
         date      stock day_delta  fee/%  value  improve/%
0  2022-10-13  14.418557  186 days    0.5  0.970  11.855670
1  2022-10-20  14.433437  179 days    0.5  0.969  11.971104
2  2022-11-03  14.706625  165 days    0.5  0.951  14.090431
3  2022-11-07  14.315251  161 days    0.5  0.977  11.054248
4  2022-11-08  14.388889  160 days    0.5  0.972  11.625514
5  2022-11-18  14.170213  150 days    0.5  0.987   9.929078
6  2022-12-19  13.916418  119 days    0.5  1.005   7.960199
7  2022-12-21  14.084592  117 days    0.5  0.993   9.264854
8  2022-12-23  14.127273  115 days    0.5  0.990   9.595960
9  2023-02-10  13.409396   66 days    0.5  1.043   4.026846
10 2023-02-16  13.422265   60 days    0.5  1.042   4.126679
```

![470007](data/trace/imgs/汇添富上证综合指数-470007.png)

## 工银金融地产混合A-000251

``` {literal=""}
投资总金额：28.00元
股份数：10.06份
当前每股单价：2.41元/份
卖出收益(扣税后)：4.91
基金价值：24.24元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：4.10%
池子:
        date     stock day_delta  fee/%  value  improve/%
0 2022-11-04  4.312783  164 days    0.5  2.163  11.373093
1 2023-02-08  5.747944   68 days    0.5  2.432  -0.945724
按低值出售的池子:
        date     stock day_delta  fee/%  value  improve/%
0 2022-11-04  4.312783  164 days    0.5  2.163  11.373093
1 2023-02-08  5.747944   68 days    0.5  2.432  -0.945724
```

![000251](data/trace/imgs/工银金融地产混合A-000251.png)

## 交银创业板50指数A-007464

``` {literal=""}
投资总金额：431.00元
股份数：266.63份
当前每股单价：1.60元/份
卖出收益(扣税后)：0.00
基金价值：427.70元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：-0.77%
池子:
         date      stock day_delta  fee/%   value  improve/%
0  2022-11-10   7.525437  158 days    0.5  1.5922   0.747394
1  2022-11-14   7.452419  154 days    0.5  1.6078  -0.230128
2  2022-11-17   7.438540  151 days    0.5  1.6108  -0.415942
3  2022-11-25   7.646946  143 days    0.5  1.5669   2.374114
4  2022-11-28   7.687668  140 days    0.5  1.5586   2.919287
5  2022-12-01   7.426092  137 days    0.5  1.6135  -0.582584
6  2022-12-05   7.451956  133 days    0.5  1.6079  -0.236333
7  2022-12-09   7.279023  129 days    0.5  1.6461  -2.551485
8  2022-12-14   7.472870  124 days    0.5  1.6034   0.043657
9  2022-12-19   7.504697  119 days    0.5  1.5966   0.469748
10 2022-12-23   7.710921  115 days    0.5  1.5539   3.230581
11 2022-12-26   7.557714  112 days    0.5  1.5854   1.179513
12 2022-12-29   7.504227  109 days    0.5  1.5967   0.463456
13 2022-12-30   7.522129  108 days    0.5  1.5929   0.703120
14 2023-01-13   7.052384   94 days    0.5  1.6990  -5.585639
15 2023-01-30   6.735245   77 days    0.5  1.7790  -9.831366
16 2023-02-10   6.968305   66 days    0.5  1.7195  -6.711253
17 2023-02-14   6.933225   62 days    0.5  1.7282  -7.180882
18 2023-02-15   6.998014   61 days    0.5  1.7122  -6.313515
19 2023-02-16   7.081560   60 days    0.5  1.6920  -5.195035
20 2023-02-17   7.265341   59 days    0.5  1.6492  -2.734659
21 2023-02-21   7.218072   55 days    0.5  1.6600  -3.367470
22 2023-02-22   7.283891   54 days    0.5  1.6450  -2.486322
23 2023-02-27   7.410477   49 days    0.5  1.6169  -0.791638
24 2023-03-01  17.081933   47 days    0.5  1.6367  -1.991813
25 2023-03-22  65.951969   26 days    0.5  1.5594   2.866487
26 2023-04-17   7.469609    0 days    1.5  1.6041   0.000000
按低值出售的池子:
         date      stock day_delta  fee/%   value  improve/%
0  2022-11-10   7.525437  158 days    0.5  1.5922   0.747394
1  2022-11-14   7.452419  154 days    0.5  1.6078  -0.230128
2  2022-11-17   7.438540  151 days    0.5  1.6108  -0.415942
3  2022-11-25   7.646946  143 days    0.5  1.5669   2.374114
4  2022-11-28   7.687668  140 days    0.5  1.5586   2.919287
5  2022-12-01   7.426092  137 days    0.5  1.6135  -0.582584
6  2022-12-05   7.451956  133 days    0.5  1.6079  -0.236333
7  2022-12-09   7.279023  129 days    0.5  1.6461  -2.551485
8  2022-12-14   7.472870  124 days    0.5  1.6034   0.043657
9  2022-12-19   7.504697  119 days    0.5  1.5966   0.469748
10 2022-12-23   7.710921  115 days    0.5  1.5539   3.230581
11 2022-12-26   7.557714  112 days    0.5  1.5854   1.179513
12 2022-12-29   7.504227  109 days    0.5  1.5967   0.463456
13 2022-12-30   7.522129  108 days    0.5  1.5929   0.703120
14 2023-01-13   7.052384   94 days    0.5  1.6990  -5.585639
15 2023-01-30   6.735245   77 days    0.5  1.7790  -9.831366
16 2023-02-10   6.968305   66 days    0.5  1.7195  -6.711253
17 2023-02-14   6.933225   62 days    0.5  1.7282  -7.180882
18 2023-02-15   6.998014   61 days    0.5  1.7122  -6.313515
19 2023-02-16   7.081560   60 days    0.5  1.6920  -5.195035
20 2023-02-17   7.265341   59 days    0.5  1.6492  -2.734659
21 2023-02-21   7.218072   55 days    0.5  1.6600  -3.367470
22 2023-02-22   7.283891   54 days    0.5  1.6450  -2.486322
23 2023-02-27   7.410477   49 days    0.5  1.6169  -0.791638
24 2023-03-01  17.081933   47 days    0.5  1.6367  -1.991813
25 2023-03-22  65.951969   26 days    0.5  1.5594   2.866487
26 2023-04-17   7.469609    0 days    1.5  1.6041   0.000000
```

![007464](data/trace/imgs/交银创业板50指数A-007464.png)

## 诺安成长混合-320007

``` {literal=""}
投资总金额：504.00元
股份数：374.65份
当前每股单价：1.57元/份
卖出收益(扣税后)：0.00
基金价值：587.83元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：16.63%
池子:
         date      stock day_delta  fee/%  value  improve/%
0  2022-11-11  12.112206  157 days    0.5  1.319  18.953753
1  2022-11-21  11.585207  147 days    0.5  1.379  13.778100
2  2022-11-23  11.807834  145 days    0.5  1.353  15.964523
3  2022-11-24  11.931292  144 days    0.5  1.339  17.176998
4  2022-11-25  11.993994  143 days    0.5  1.332  17.792793
5  2022-11-29  11.940209  139 days    0.5  1.338  17.264574
6  2022-12-02  11.878067  136 days    0.5  1.345  16.654275
7  2022-12-05  11.878067  133 days    0.5  1.345  16.654275
8  2022-12-14  11.773029  124 days    0.5  1.357  15.622697
9  2022-12-19  12.158295  119 days    0.5  1.314  19.406393
10 2022-12-21  12.298691  117 days    0.5  1.299  20.785219
11 2022-12-23  12.801282  115 days    0.5  1.248  25.721154
12 2023-01-09  12.374903   98 days    0.5  1.291  21.533695
13 2023-01-11  12.327160   96 days    0.5  1.296  21.064815
14 2023-01-13  12.308166   94 days    0.5  1.298  20.878274
15 2023-01-18  11.712610   89 days    0.5  1.364  15.029326
16 2023-01-30  11.322466   77 days    0.5  1.411  11.197732
17 2023-02-01  11.526696   75 days    0.5  1.386  13.203463
18 2023-02-08  11.669832   68 days    0.5  1.369  14.609204
19 2023-02-10  11.419585   66 days    0.5  1.399  12.151537
20 2023-02-13  11.403283   63 days    0.5  1.401  11.991435
21 2023-02-14  11.468772   62 days    0.5  1.393  12.634602
22 2023-02-16  11.526696   60 days    0.5  1.386  13.203463
23 2023-02-17  11.842847   59 days    0.5  1.349  16.308377
24 2023-02-21  11.834074   55 days    0.5  1.350  16.222222
25 2023-02-27  12.066465   49 days    0.5  1.324  18.504532
26 2023-02-28  12.021068   48 days    0.5  1.329  18.058691
27 2023-03-01  41.728358   47 days    0.5  1.340  17.089552
28 2023-03-07  11.940209   41 days    0.5  1.338  17.264574
按低值出售的池子:
         date      stock day_delta  fee/%  value  improve/%
0  2022-11-11  12.112206  157 days    0.5  1.319  18.953753
1  2022-11-21  11.585207  147 days    0.5  1.379  13.778100
2  2022-11-23  11.807834  145 days    0.5  1.353  15.964523
3  2022-11-24  11.931292  144 days    0.5  1.339  17.176998
4  2022-11-25  11.993994  143 days    0.5  1.332  17.792793
5  2022-11-29  11.940209  139 days    0.5  1.338  17.264574
6  2022-12-02  11.878067  136 days    0.5  1.345  16.654275
7  2022-12-05  11.878067  133 days    0.5  1.345  16.654275
8  2022-12-14  11.773029  124 days    0.5  1.357  15.622697
9  2022-12-19  12.158295  119 days    0.5  1.314  19.406393
10 2022-12-21  12.298691  117 days    0.5  1.299  20.785219
11 2022-12-23  12.801282  115 days    0.5  1.248  25.721154
12 2023-01-09  12.374903   98 days    0.5  1.291  21.533695
13 2023-01-11  12.327160   96 days    0.5  1.296  21.064815
14 2023-01-13  12.308166   94 days    0.5  1.298  20.878274
15 2023-01-18  11.712610   89 days    0.5  1.364  15.029326
16 2023-01-30  11.322466   77 days    0.5  1.411  11.197732
17 2023-02-01  11.526696   75 days    0.5  1.386  13.203463
18 2023-02-08  11.669832   68 days    0.5  1.369  14.609204
19 2023-02-10  11.419585   66 days    0.5  1.399  12.151537
20 2023-02-13  11.403283   63 days    0.5  1.401  11.991435
21 2023-02-14  11.468772   62 days    0.5  1.393  12.634602
22 2023-02-16  11.526696   60 days    0.5  1.386  13.203463
23 2023-02-17  11.842847   59 days    0.5  1.349  16.308377
24 2023-02-21  11.834074   55 days    0.5  1.350  16.222222
25 2023-02-27  12.066465   49 days    0.5  1.324  18.504532
26 2023-02-28  12.021068   48 days    0.5  1.329  18.058691
27 2023-03-01  41.728358   47 days    0.5  1.340  17.089552
28 2023-03-07  11.940209   41 days    0.5  1.338  17.264574
```

![320007](data/trace/imgs/诺安成长混合-320007.png)

## 富国中证新能源汽车指数(LOF)A-161028

``` {literal=""}
投资总金额：415.00元
股份数：379.45份
当前每股单价：1.05元/份
卖出收益(扣税后)：0.00
基金价值：396.90元
收益率(卖出收益+基金价值/投资总金额,部分扣税)：-4.36%
池子:
         date      stock day_delta  fee/%  value  improve/%
0  2023-01-05  11.036464  102 days    0.5  1.086  -3.683241
1  2023-01-06  10.856522  101 days    0.5  1.104  -5.253623
2  2023-01-09  10.788119   98 days    0.5  1.111  -5.850585
3  2023-01-11  10.817329   96 days    0.5  1.108  -5.595668
4  2023-01-13  10.578641   94 days    0.5  1.133  -7.678729
5  2023-01-16  10.587986   91 days    0.5  1.132  -7.597173
6  2023-01-18  10.532162   89 days    0.5  1.138  -8.084359
7  2023-01-30  10.088889   77 days    0.5  1.188 -11.952862
8  2023-02-01   9.905455   75 days    0.5  1.210 -13.553719
9  2023-02-08  10.252866   68 days    0.5  1.169 -10.521814
10 2023-02-10  17.235548   66 days    0.5  1.159  -9.749784
11 2023-02-13  10.296907   63 days    0.5  1.164 -10.137457
12 2023-02-14  10.332414   62 days    0.5  1.160  -9.827586
13 2023-02-15  10.413206   61 days    0.5  1.151  -9.122502
14 2023-02-16  10.587986   60 days    0.5  1.132  -7.597173
15 2023-02-17  10.807574   59 days    0.5  1.109  -5.680794
16 2023-02-21  10.768733   55 days    0.5  1.113  -6.019766
17 2023-02-22  10.886104   54 days    0.5  1.101  -4.995459
18 2023-02-27  11.046636   49 days    0.5  1.085  -3.594470
19 2023-02-28  10.995963   48 days    0.5  1.090  -4.036697
20 2023-03-06  11.087512   42 days    0.5  1.081  -3.237743
21 2023-03-07  11.264662   41 days    0.5  1.064  -1.691729
22 2023-03-22  99.783123   26 days    0.5  1.031   1.454898
23 2023-04-04  11.762120   13 days    0.5  1.019   2.649657
24 2023-04-17  26.736520    0 days    1.5  1.046   0.000000
按低值出售的池子:
         date      stock day_delta  fee/%  value  improve/%
0  2023-01-05  11.036464  102 days    0.5  1.086  -3.683241
1  2023-01-06  10.856522  101 days    0.5  1.104  -5.253623
2  2023-01-09  10.788119   98 days    0.5  1.111  -5.850585
3  2023-01-11  10.817329   96 days    0.5  1.108  -5.595668
4  2023-01-13  10.578641   94 days    0.5  1.133  -7.678729
5  2023-01-16  10.587986   91 days    0.5  1.132  -7.597173
6  2023-01-18  10.532162   89 days    0.5  1.138  -8.084359
7  2023-01-30  10.088889   77 days    0.5  1.188 -11.952862
8  2023-02-01   9.905455   75 days    0.5  1.210 -13.553719
9  2023-02-08  10.252866   68 days    0.5  1.169 -10.521814
10 2023-02-10  17.235548   66 days    0.5  1.159  -9.749784
11 2023-02-13  10.296907   63 days    0.5  1.164 -10.137457
12 2023-02-14  10.332414   62 days    0.5  1.160  -9.827586
13 2023-02-15  10.413206   61 days    0.5  1.151  -9.122502
14 2023-02-16  10.587986   60 days    0.5  1.132  -7.597173
15 2023-02-17  10.807574   59 days    0.5  1.109  -5.680794
16 2023-02-21  10.768733   55 days    0.5  1.113  -6.019766
17 2023-02-22  10.886104   54 days    0.5  1.101  -4.995459
18 2023-02-27  11.046636   49 days    0.5  1.085  -3.594470
19 2023-02-28  10.995963   48 days    0.5  1.090  -4.036697
20 2023-03-06  11.087512   42 days    0.5  1.081  -3.237743
21 2023-03-07  11.264662   41 days    0.5  1.064  -1.691729
22 2023-03-22  99.783123   26 days    0.5  1.031   1.454898
23 2023-04-04  11.762120   13 days    0.5  1.019   2.649657
24 2023-04-17  26.736520    0 days    1.5  1.046   0.000000
```

![161028](data/trace/imgs/富国中证新能源汽车指数(LOF)A-161028.png)
