# ipython

IPython 是一种基于 Python 的交互式解释器，提供了强大的编辑和交互功能。

IPython 的优点：

- 满足你各种需求的交互式 shell
- 火爆数据科学社区的 Jupyter 内核（供Jupyter Notebook使用）
- 对交互式数据可视化和 GUI 工具的完美支持
- 简单易用的高性能并行计算工具

## Usage

```python
? : 内省的帮助命令
object ?: 对象属性内审
object ??: 对象源码内省
history: 查看历史输入
hist
! shell_command: 执行shell命令
```

Tab 自动补全

魔法命令

```python
%: 魔法命令 单行有效
%%: 魔法命令 单元 cell 有效
%run script.py: 执行脚本, 相当于 cell 运行该脚本
%run -d: 交互式执行脚本
%timeit
%%timeit
%pwd
%matplotlib inline: 将图表直接嵌入到 notebook 中，方便查看
%conda install pkgs: 在 IPython 中安装 python 第三方库
%pylab: 使 numpy 和 matplotlib 中的科学计算功能生效，这些功能被称为基于向量和矩阵的高效操作，交互可视化特性。它能够让我们在控制台进行交互式计算和动态绘图。 
%quickref: 查看 IPython 的特定语法和魔法命令参考
%ls: 显示目录内容
pd.*Da*?
%cd
_: 打印前一个输出的结果
f();: 抑制输出结果
%debug: 报错之后的一个 cell 启动
%pdb: 报错之前需要开启
%pycat: 高亮脚本
%env： 显示环境变量
%load script.py: 载入代码到下一个 cell
%macro taskname n1 n2 n3-n4 ..: 用来定义宏，并给宏命名，执行指定的代码行。
%notebook mynotebook.ipynb: 导出当前 notebook 内容到指定 ipynb 文件中。
%pdef: 打印构造信息
%pdoc: 命令用来打印对象的文档字符串。 
%who: 显示当前变量
%who int: 显示当前 int 类型变量
%whos: 详细显示当前变量
%save sample.py n1-n7: 保存 cell 到 python 文件
%reset -f: 命令用于删除定义的所有变量
%%html: 渲染 HTML
%%javascript: 运行 JavaScript
%%latex: 渲染 LaTeX
%%markdown: 渲染 markdown
%%writefile: 写入 cell 到文件 文件格式可为 txt、py 等
%magic: 获取魔法命令列表
```

## links

- [50 个关于 IPython 的使用技巧，get 起来！](https://zhuanlan.zhihu.com/p/104524108)