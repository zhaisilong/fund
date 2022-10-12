# jupyter notebook

## 快捷键

Ctrl+Enter 执行单元格

Shift-Enter 执行单元格 进一格

DD 删除

B（Below）键，在单元格下方新建单元格。可以按 ESC 退出编辑

A 在上方插入

M 转化为 Markdown

Y 转化为代码

Tab 代码补全或缩进

Shift-Tab 代码提示

## 魔法命令

magic 函数主要包含两大类

行魔法（Line magic）前缀为 %
单元魔法(Cell magic)前缀为 %%；

## Jupyter

```py
%lsmagic # 查看所有魔法
%lsmagic? # 查看魔法的帮助
%matplotlib inline #使用matplotlib画图时，图片嵌入在jupyter notebook里面，不以单独窗口显示
%pwd # 和linux一样，查找当前目录
%cd ../
%cp test_peace.py test_load.py
%whos # 查看当前变量,类型，信息
%reset # 清除变量
%load test_peace.py # 加载一个文件里面的内容

%timeit %%timeit #为代码执行计时
import numpy as np
%timeit np.sin(24)

%%timeit
x=np.sin(20)
np.cos(-x)
```

%%writefile # 后面紧接着一个 file_name.py,表示在 jupyter notebook 里面创建一个 py 文件，后面 cell 里面的内容为 py 文件内容

```sh
%%writefile test_peace.py
import numpy as np
print(np.random.randint(1,5))
```

%run #后面紧接着一个相对地址的 file_name.py，表示运行一个 py 文件

```sh
%run test_peace.py
```

## Jupyter 修改主题

```python
# 安装
pip install --upgrade jupyterthemes
# 加载可用主题列表
jt -l
# selecting a particular theme
jt -t <name of the theme>
# 恢复到最初主题
jt -r
# 其中 -f(字体) -fs(字体大小) -cellw(占屏比或宽度) -ofs(输出段的字号) -T(显示工具栏) -N(显示自己主机名)
jt -t grade3 -f fira -fs 13 -cellw 90% -ofs 11 -dfs 11 -T -N
```

- [如何优雅地使用 Jupyter？](https://www.zhihu.com/question/59392251)

- [jupyter notebook 如何打开 md 文件](https://blog.csdn.net/handsomeandge/article/details/110052319)

## jupyter lab

```sh
# 激活已经创建好的虚拟环境
conda activate myenv

# 在虚拟环境中安装 ipykernel
conda install ipykernel
pip install ipywidgets

# 安装 kernel，--name 自定义名称
ipython kernel install --user --name myenv

# 不需要该 kernel 时可以删除
jupyter kernelspec remove myenv

```

## Links

- [前置机器学习（二）：30 分钟掌握常用 Jupyter Notebook 用法](https://mp.weixin.qq.com/s?__biz=MzUxMjU4NjI4MQ==&mid=2247484027&idx=1&sn=16a6dbd4ca1c64d51adbd67b17d300c7&chksm=f963653dce14ec2bffd81274be5c5151ca7a949e0d2ca745f9502946130668fe9bd263fa5b3c&scene=178&cur_album_id=1627166768236412929#rd)