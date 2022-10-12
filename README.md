
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

### 快速入手

```bash
bash pipeline.sh
```

### 基本操作

```bash
python crawl.py  # 爬取基金的信息
python analysis.py  # 基金分析
python track.py  # 基金跟踪
python predict.py  # 基金预测
python strtegy.py  # 制定策略
```