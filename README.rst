|docs| |stars|

前言
----

-  基于 Python 的量化投资基金的仓库.
-  本仓库所有的信息均不构成投资建议.
-  如果你对次项目感兴趣,欢迎右上角点赞.

安装
----

.. code:: bash

   conda create -nfund python=3.8
   # 深度学习 pytorch 套装
   conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

安装 `java runtime`

.. code:: bash

    brew install java
    brew install node

安装 `pandoc`

.. code:: bash

    brew install pandoc  # for Darwin
    sudo apt install pandoc  # for Ubuntu

使用
----

快速入手
~~~~~~~~

.. code:: bash

   bash pipeline.sh

基本操作
~~~~~~~~

.. code:: bash

   python crawl.py  # 爬取基金的信息
   python analysis.py  # 基金分析
   python track.py  # 基金跟踪
   python predict.py  # 基金预测
   python strtegy.py  # 制定策略

跟踪情况
--------

全局跟踪
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: data/trace/reports/finance.txt
   :literal:

中欧互联网先锋混合A-010213
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: data/trace/reports/中欧互联网先锋混合A-010213.txt
   :literal:

|010213|

广发医药健康混合A-010110
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: data/trace/reports/广发医药健康混合A-010110.txt
   :literal:

|010110|

招商中证白酒指数(LOF)A-161725
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: data/trace/reports/招商中证白酒指数(LOF)A-161725.txt
   :literal:

|161725|


汇添富上证综合指数-470007
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: data/trace/reports/汇添富上证综合指数-470007.txt
   :literal:

|470007|


工银金融地产混合A-000251
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: data/trace/reports/工银金融地产混合A-000251.txt
   :literal:

|000251|

交银创业板50指数A-007464
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: data/trace/reports/交银创业板50指数A-007464.txt
   :literal:

|007464|

.. |docs| image:: https://readthedocs.org/projects/fund/badge/?version=latest
   :target: https://fund.readthedocs.io/zh_CN/latest/
.. |stars| image:: https://shields.io/github/stars/zhaisilong/fund?style=social
   :target: https://github.com/zhaisilong/fund
.. |010213| image:: data/trace/imgs/中欧互联网先锋混合A-010213.png
.. |010110| image:: data/trace/imgs/广发医药健康混合A-010110.png
.. |161725| image:: data/trace/imgs/招商中证白酒指数(LOF)A-161725.png
.. |470007| image:: data/trace/imgs/汇添富上证综合指数-470007.png
.. |000251| image:: data/trace/imgs/工银金融地产混合A-000251.png
.. |007464| image:: data/trace/imgs/交银创业板50指数A-007464.png
