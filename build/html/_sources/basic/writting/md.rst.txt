Markdown
========

-  `Markdown
   教程 <https://zhaisilong.com/index.php/archives/markdown.html>`__

GFM
---

GitHub Flavored Markdown

GitHub 在 Markdown 的基础上引入了一些新特性

.. code:: markdown

   删除
   ~~我是被删除的内容~~

   自动链接
   在 GFM 中只要是合法的 HTTP 网址就可以自动被解析成一个有效的链接，可以省略标准 Markdown 中的尖括号（<>） 
   我的博客是 https://zhaisilong.com

   任务列表
   - [ ] 待办事项1
   - [ ] 待办事项2
   - [x] 待办事项3
   - [x] 待办事项4

   表格
   姓名 | 年龄 | 性别
   ----|-----|----
   小明 | 18 | 男
   小刚 | 29 | 女
   李三 | 20 | 男

   Emoji表情支持
   :grinning:
   :heart_eyes:
   :speech_balloon:
   :peach:
   ![](https://cdn.jsdelivr.net/gh/xxzhai123/img/imgv2-6c8c3b801b1e79cafa0a8642b430e271_720w.jpg)
   ![](https://cdn.jsdelivr.net/gh/xxzhai123/img/imgv2-6d6b1fe9e1ba08a7191fbf3e64617ae8_r.jpg)

   禁止了一些特殊的原生HTML标签
   GFM 中会对这些特殊标签的左尖号 `<` 进行转义成 `&lt;`，从而让这些标签不起作用。

   单词内部的下划线
   在 GFM 语法中会忽略掉单词内部的下划线
   为了避免混淆，尽量不要去使用下划线尽量去使用`*`

   + 你好
   - 你不好

.. role:: raw-latex(raw)
   :format: latex
..

Latex
=====

展示
----

1. :math:`\quad` 空格
2. :math:`\text{if n is odd}` 文本
3. ``&`` 错位的对齐制表符
4.

   .. math::


      f(n) =
      \begin{cases}
       2n,  & \text{if $n$ is even} \\\\
       3n, & \text{if $n$ is odd}
      \end{cases}

5. :math:`\sim`

插入公式
--------

行内公式
~~~~~~~~

   :math:`y=x+1`

独立公式
~~~~~~~~

   .. math:: y=x+1

上下标
------

.. math::  x^{y^z}=(1+e_1)^{xy^w}

括号
----

``(``\ 、\ ``)``\ 、\ ``[``\ 、\ ``]`` 和 ``|`` 表示符号本身，使用
``\\{``\ 来表示 ``{``\ ，\ ``\\}`` 来表示 ``}``

.. math::  {f}'(x) = ( \frac{df}{dx} )

通过将 :raw-latex:`\left与`( ,:raw-latex:`\right与`)
结合使用，可以将括号大小随着其内容变化。其他括号同理。

.. math::  {f}'(x) = \left( \frac{df}{dx} \right)

.. math::  {f}'(0)=\left.\frac{df}{dx}\right|\_{x=0}

分段函数
--------

.. math::


   f(n) =
   \begin{cases}
   2n,  & \text{if $n$ is even} \\\\
   3n, & \text{if $n$ is odd}
   \end{cases}

运算表达式
----------

分数
~~~~

.. math:: \frac{a}{b}

根号
~~~~

.. math:: \sqrt[a]{b}

求和
~~~~

.. math:: \sum_{a}^{b}

.. math:: \prod_{a}^{b}

省略号
~~~~~~

.. math:: {a+}\ldots{+b}

.. math:: {a+}\cdots{+b}

极限
~~~~

.. math:: lim_{{a} \to {\infty}}

求导
~~~~

.. math:: {f}'(x)

积分
~~~~

.. math:: \int_{a}^{b}{x}\,dx

希腊字母
--------

1. :math:`\alpha`
2. :math:`\beta`
3. :math:`\epsilon`

运算符
------

二元运算符
~~~~~~~~~~

1.  :math:`+`
2.  :math:`\ast`
3.  :math:`-`
4.  :math:`\times`
5.  :math:`\div`
6.  :math:`\pm`
7.  :math:`\mp`
8.  :math:`\setminus`
9.  :math:`\approx`
10. :math:`\odot`
11. :math:`\geq`
12. :math:`\leq`
13. :math:`\%`
14. :math:`\neq`
15. :math:`30^\circ`

对数运算符
~~~~~~~~~~

1. :math:`\log`
2. :math:`\lg`
3. :math:`\ln`

逻辑运算符
~~~~~~~~~~

1. :math:`\because`
2. :math:`\therefore`
3. :math:`\forall`
4. :math:`\exists`
5. :math:`\not\subset`

箭头
----

1.  :math:`\Leftarrow`
2.  :math:`\Longleftarrow`
3.  :math:`\Rightarrow`
4.  :math:`\Longrightarrow`
5.  :math:`\Longleftrightarrow`
6.  :math:`\leftarrow`
7.  :math:`\longleftarrow`
8.  :math:`\rightarrow`
9.  :math:`\longrightarrow`
10. :math:`\longleftrightarrow`
11. :math:`\iff`

向量
----

1. :math:`\boldsymbol{x}`
2. :math:`\mathbf{x}`
3. :math:`\vec{x}`
4. :math:`x`
5. :math:`\overrightarrow{AB}`

其他
----

1. :math:`\quad` 空格
2. :math:`\qquad` 两个空格
3. :math:`\diamondsuit` 表重要
4. :math:`\dots`
5. :math:`\emptyset`
6. :math:`\bot`
7. :math:`\top`

源码
----

.. code::  markdown

    1. $\quad$ 空格
    2. $\text{if n is odd}$ 文本
    3. `&` 错位的对齐制表符
    4. $$
       f(n) =
       \begin{cases}
        2n,  & \text{if $n$ is even} \\\\
        3n, & \text{if $n$ is odd}
       \end{cases}
       $$
    5. $\sim$

    ## 插入公式

    ### 行内公式

    > $y=x+1$

    ### 独立公式

    > $$y=x+1$$

    ## 上下标

    $$ x^{y^z}=(1+e_1)^{xy^w} $$

    ## 括号

    `(`、`)`、`[`、`]` 和 `|` 表示符号本身，使用 `\\{`来表示 `{`，`\\}` 来表示 `}`
    $$ {f}'(x) = ( \frac{df}{dx} ) $$
    通过将 \left与( ,\right与) 结合使用，可以将括号大小随着其内容变化。其他括号同理。
    $$ {f}'(x) = \left( \frac{df}{dx} \right) $$

    $$ {f}'(0)=\left.\frac{df}{dx}\right|\_{x=0} $$

    ## 分段函数

    $$
    f(n) =
    \begin{cases}
    2n,  & \text{if $n$ is even} \\\\
    3n, & \text{if $n$ is odd}
    \end{cases}
    $$

    ## 运算表达式

    ### 分数

    $$\frac{a}{b}$$

    ### 根号

    $$\sqrt[a]{b}$$

    ### 求和

    $$\sum_{a}^{b}$$

    $$\prod_{a}^{b}$$

    ### 省略号

    $${a+}\ldots{+b}$$
    $${a+}\cdots{+b}$$

    ### 极限

    $$lim_{{a} \to {\infty}}$$

    ### 求导

    $${f}'(x)$$

    ### 积分

    $$\int_{a}^{b}{x}\,dx$$

    ## 希腊字母

    1. $\alpha$
    2. $\beta$
    3. $\epsilon$

    ## 运算符

    ### 二元运算符

    1. $+$
    2. $\ast$
    3. $-$
    4. $\times$
    5. $\div$
    6. $\pm$
    7. $\mp$
    8. $\setminus$
    9. $\approx$
    10. $\odot$
    11. $\geq$
    12. $\leq$
    13. $\%$
    14. $\neq$
    15. $30^\circ$

    ### 对数运算符

    1. $\log$
    2. $\lg$
    3. $\ln$

    ### 逻辑运算符

    1. $\because$
    2. $\therefore$
    3. $\forall$
    4. $\exists$
    5. $\not\subset$

    ## 箭头

    1. $\Leftarrow$
    2. $\Longleftarrow$
    3. $\Rightarrow$
    4. $\Longrightarrow$
    5. $\Longleftrightarrow$
    6. $\leftarrow$
    7. $\longleftarrow$
    8. $\rightarrow$
    9. $\longrightarrow$
    10. $\longleftrightarrow$
    11. $\iff$

    ## 向量

    1. $\boldsymbol{x}$
    2. $\mathbf{x}$
    3. $\vec{x}$
    4. $x$
    5. $\overrightarrow{AB}$

    ## 其他

    1. $\quad$ 空格
    2. $\qquad$ 两个空格
    3. $\diamondsuit$ 表重要
    4. $\dots$
    5. $\emptyset$
    6. $\bot$
    7. $\top$


