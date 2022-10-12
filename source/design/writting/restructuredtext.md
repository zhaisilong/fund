# reStructuredText

`reStructuredText` 标记语言，相对 Markdown 来说，在写书方面更有优势:

-   使用 `sphnix` 能够自动生成目录和索引文件，方便查询和检索；
-   有大量漂亮的HTML书籍主题模版，可为书籍轻松换肤（类似`Wordpress` 的网站模版）；
-   对于参考手册类书籍的编写在语法上更为便利（`python`官方帮助文档的使用者）；

```rst
# 下划线及上划线表示 部分
* 划线及上划线表示 章节
= 下划线表示 小章节
- 下划线表示 子章节
^ 下划线表示 子章节的子章节
" 下划线表示 段落
```

```rst
*emphasis*
**emphasis**
`interpreted text`
``inline literal``
:sub:`xxx`
:sup:`xxx`
:guilabel:`Action`
:kbd:`Ctrl+Shift`
:menuselection:`A-->B-->C`
```

## 列表

```rst
- 无序
1. 有序
#. 自动编号
```

### 定义列表

术语的定义

```rst
term
    术语定义必须缩进

    可以包含多个段落

next term
    术语描述
```

分块

```rst
| These lines are
| broken exactly like in
| the source file.
```

## 源代码

注意大多数时候，空格代替一个换行符。所有有些时候换行是必要的。比如 `.. code-block::` 下面接了一句普通的话。块和半句是不能放在一起的。

标记符号 `::` 紧接一空白行（这个空行是必要的）, 然后紧跟代码, 整个代码文本块必须缩进 这里的如:

```rst
::

    some codes
    some codes
    some codes

此行上面的空行也是必要的
```

显式标记块的第一行是以 `..` 开始，接着是紧随着空格，被结束于同样层级缩进的下一段落。（显式标记和正常的段落之间需要有一个空行。当你写它的时候，可能听起来有点复杂，但它是直观的。）

高级的代码高亮功能

```rst
此行下面的空行也是必要的

.. code-block:: python
   :caption: Code Blocks can have captions.
   :linenos:
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'
```

快速定义代码块

```rst
.. highlight:: sh
	此指令后如下的“::”定义的块都会以 sh 语法进行高亮，直到遇到下一条 highlight 指令。

::
	# 此命令在主机执行
	sudo apt install python
	echo "helloworld,this is a script test!"
```

`literalinclude` 直接嵌入本地文件并高亮

```rst
.. literalinclude:: ../../base_code/hello.c
	:caption: ../../base_code/hello.c
	:language: c
	:emphasize-lines: 5,7-12
	:linenos:
	:name: hello.c
```

嵌入文件的某部分

```rst
.. literalinclude:: ../../base_code/hello.c
	:caption: ../../base_code/hello.c
	:language: c
	:linenos:
	:lines: 1,3,5-8,20-
```

python 模块的include。他有选择性的选取 timer.start

```rst
.. literalinclude:: example.py
   :pyobject: Timer.start
```

文件对比

```rst
.. literalinclude:: ../../base_code/hello.c
	:diff: ../../base_code/hello_diff.c
```

## 侧边栏 (Sidebar)

```rst
.. sidebar:: 这是一个侧边栏

	这是一个侧边栏, 可以放入代码, 也可以放入图像代码等等, 它下面可以是文字, 图像, 代码等等, 如本例中下面是一段文字.

冬日，在暖暖的午后，泡上一杯茶，随便拿起一本书，凑到阳光跟前，是何等的惬意与享受……

风虽然不大，但走在路上，鼻子冷的刺骨的疼；而阳光却那么地温热，温热地忍不住想和她亲吻。

我泡上一杯碧螺春，从书架上随便拿起一本书，走向靠窗的位置，凑到阳光面前，任由她吻着我的脸，就像吻着自己的情人，这感觉美好的让你忘却了所有的烦恼。

也许是身边暖气的缘故，空气的影子，映衬到桌子上、书纸上。影影绰绰如月下之花影，飘飘忽忽如山间之云气，生生腾腾如村落之炊烟，荡荡漾漾如湖面之微波，似乎在这图书馆的这一隅便可看尽天地间的朴素与祥和。
```

## 表格

```rst
.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"
```

```rst
=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======
```

```rst
.. table:: Grid Table Demo
   :name: table-gridtable

   +------------------------+----------+----------+----------+
   | Header row, column 1   | Header 2 | Header 3 | Header 4 |
   | (header rows optional) |          |          |          |
   +========================+==========+==========+==========+
   | body row 1, column 1   | column 2 | column 3 | column 4 |
   +------------------------+----------+----------+----------+
   | body row 2             | ...      | ...      |          |
   +------------------------+----------+----------+----------+
```

## 直接标记 (Explicit Markup)

```rst
.. 这是一个注释, 你只能在源码中看到我, 我不会被渲染出来.
```

注意：`..` 与评论块不能有空格

```rst
..
   这整个缩进块都是
   一个注释.
   你只能在源码中看到我们, 我们不会被渲染出来

   仍是一个评论.
```

```rst
.. |image_name| image:: picture.jpeg
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: 对于不能显示图片的时候, 显示这些文字
   :align: right
```

## 数学公式

注意：尽管 `.. math::` 与公式之间可以不需要空行，但是仍然非常建议加上。

```rst
行内公式 :math:`\alpha > \beta` :

Display 公式:

.. math::

    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

带标签公式:

.. math::
   :label: This is a label

    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

多行公式:

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

对齐多行公式:

.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2
```

## 提示警告类

注意：尽管 `.. something::` 之间不需要空行。

```rst
.. tip:: This is a tip

.. note:: This is a note

.. hint:: This is a hint

.. danger:: This is a danger

.. error:: This is an error

.. warning:: This is a warning

.. caution:: This is a caution

.. attention:: This is an attention

.. important:: This is an important

.. seealso:: This is seealso
```

## 超链接

```rst
This is a paragraph that contains `a link`_.

.. _a link: http://example.com/
```

### 内部链接

```rst
.. _figure-datangfurongyuan:

.. figure:: ../_static/figs/mkdocs/insertfigure.png
...
```

### 图片

Sphinx将会自动将图像文件拷贝到输出目录中（例如HTML格式输出，会拷贝到 `_static` 目录中。）

- Sphinx扩展了标准的docutils的功能，允许文件扩展名为星号:

```rst
.. image:: gnu.png
   (options)
   
.. image:: gnu.*
   (options)
```

## 引用

### 引用文档

```rst
自定义引用文字
:doc:`引用本地的其它 rst 文档,rst 后缀要省略，如 about_us <../about_us>`

使用标题文字
:doc:`../about_us`
```

### 使用标签引用文档

```rst
:ref:`about_embedfire <about_embedfire>`

:ref:`about_embedfire`
```

### 引文

所有的文件可以使用所有的引文。

引文用法是类似的脚注的用法，但带标签不是数字，或以``#``开始。

```rst
Lorem ipsum [Ref]_ dolor sit amet.
.. [Ref] Book or article reference, URL or whatever.
```

### 脚注

```rst
Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.
```

### 下载

```rst
:download:`引用非 rst 的本地文档 <../requirements.txt>`.
```

## html
```rst
.. raw:: html
<iframe src="//player.bilibili.com/player.html?aid=70961112&cid=122951107&page=1" crolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
```

## Sphinx标记结构

### toctree

由于reST不便于多个文件相互关联或者分割文件到多个输出文件中，Sphinx通过使用自定义的指令（标识符）来处理构成文档的单个文件的关系，这同样使用与内容表。`toctree` 指令（标识符）就是核心要素。

推荐阅读：

- [Toctree的Sphinx 使用手册](https://zh-sphinx-doc.readthedocs.io/en/latest/index.html)

- [TOC树](http://www.pythondoc.com/sphinx/markup/toctree.html#toctree-directive)

几个重要的附加选项

```rst
:maxdepth:2             设置最大深度
:numbered:              自动编号
:name:                  名字
:titlesonly:            仅显示在树中的文件的标题，而不是其他的同级别的标题
:glob:                  通配符，这样写文件条目简单写
:reversed:              反向编号
:hidden:                隐藏，如果想要从toctree生成”sitemap”的话，这是非常有用的
```

特殊的文件名

```rst
genindex 总索引
modindex Python模块索引
search 搜索页
```

案例

- 所有这些文件的内容表被加入，最大的深度为2，这意味着一个嵌套标题。在这些文件中的 `toctree` 指令（标识符）也会被考虑到（识别）。
- `All about strings <strings>`，`index.rst`中显示`All about strings`，点击时索引到 `string.rst`（可以换成`<https://www,baidu.com>`）
- `glob`使得`docdir2/*`和 `*`的星号能被替换

```rst
.. toctree::
    :glob:
    :reversed:
    :numbered:
    :maxdepth:2  
    :caption: test

    intro
    docdir2/*
    *
    All about strings <strings>
    Go to Baidu <https://www,baidu.com>
```

### 内联标记 Inline markup

Sphinx使用经过解释的 text role 将语义标记插入文档。

#### 交叉引用语法

```rst
:role:`target`

使用下面的可以链接
:role:`title <target>`

下面不会创建链接
:role:`!target`

下面创建的是路径
:role:`~target`
```

#### 交叉引用 objects

python 的交叉引用

```rst
:py:mod:
:py:func:
:py:data:
:py:const:
:py:class:
:py:meth:
:py:attr:
:py:exc:
:py:obj:
```

### 替换

```rst
|release|

|version|

|today|
```

### 段落级标记

这些指令（标识符）创建简短的段落，可用于内部信息的单位以及普通的文本

```rst
.. note:: 这是note

.. note::
    这也是 note，推荐这么写。

.. warning:: 这是warning

.. versionadded:: 2.5
	The *spam* parameter.

.. versionchanged:: 2.6
	The reason why you changed the version.

.. deprecated:: 1.0
	说明了什么场合功能不推荐使用。
	Use :func:`spam` instead.
	
.. seealso:: 这是seealso

.. rubric:: title

该指令（标识符）创建一个段落，标题，不使用节点创建一个表的内容。

.. centered:: LICENSE AGREEMENT

创建一个居中粗体显示的文本行。

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally
```
