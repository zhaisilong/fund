# Latex 教程

Latex 的学习并不简单，想要入门的朋友们要有心理准备。
你可以看那些半小时入门 Latex 的书，但一定要仔仔细细阅读一本正统的书。
他能帮助你解答很多疑惑，让你少走弯路。
下面推介一个简单的入门路径。

1. 阅读各类关于 Latex 学习的帖子：初步了解 Latex。
2. 学习使用模板，一般官方正规的模板会有详细的模板使用指南，这就涉及到一些边边角角的知识了。推荐几个模板
   1. 清华和浙大的毕业论文模板，可以在 GitHub 上找到
   2. ACS 期刊的模板
3. 最后必须要回归正统，也就是读一些专业的，系统的书，这里推介一下刘海洋的 《Latex 入门》

## Installation

### 安装 texlive

```shell
sudo apt-get install texlive-latex-base
sudo apt-get install texlive-fonts-recommended
sudo apt-get install texlive-fonts-extra
sudo apt-get install texlive-latex-extra

# 或者简单一点
sudo apt-get install texlive-full

# 中文支持
sudo apt-get install texlive-lang-chinese
sudo apt-get install texlive-xetex  # 编译引擎
```

### 编译

这里只展示 xetex 编译含有中文字符的文档。

```shell
xelatex example.tex
bibtex example.aux
xelatex example.tex
xelatex example.tex
```

## Tutorial

空行不是必要的，但它可以让长的文档更易读。

### 简单的例子

```latex
\documentclass{article}

\begin{document}

\title{AI in Drug}
\author{Zhai Silong}
\date{\today}
\maketitle

\pagenumbering{roman}
\tableofcontents
\newpage
\pagenumbering{arabic}

hello, world
\end{document}
```

### 文档以及导言

```latex
\documentclass[a4paper, 12pt]{article}
```

article 文档类型适合较短的文章，比如期刊文章和短篇报告。
report（适用于更长的多章节的文档，比如博士生论文）。
proc（会议论文集）book 和 beamer。

#### 日期

```latex
\data{November 2013}
\date{\today}
```

### 章节与段落

```latex
\documentclass{article}
\title{Hello World}
\begin{document}
\maketitle

\section{Hello China} China is in East Asia.
\subsection{Hello Beijing} Beijing is the capital of China.
\subsubsection{Hello Dongcheng District}

\paragraph{Tian'anmen Square}is in the center of Beijing
\subparagraph{Chairman Mao} is in the center of Tian'anmen Square

\subsection{Hello Guangzhou}
\paragraph{Sun Yat-sen University} is the best university in Guangzhou.
\end{document}
```

对于 `report` 和 `book` 类型的文档我们还支持 `\chapter{...}` 的命令 

#### 段落缩进

LaTeX 默认每个章节第一段首行顶格，之后的段落首行缩进。
如果想要段落顶格，在要顶格的段落前加 `\noindent` 命令即可。
如果希望全局所有段落都顶格，在文档的某一位置使用 `\setlength{\parindent}{0pt}` 命令，之后的所有段落都会顶格。

#### 标签

标签只能给章节创建，只能显示且无法链接

```latex
\section{Methods}

\subsection{Stage 1}
\label{sec1}
The first part of the methods.

\ref{sec1}  % show labelname
\pageref{sec1}  % show page number
```

### 目录

```latex
\documentclass{article}
\begin{document}
\tableofcontents  % show words of Contents
\section{Hello China} China is in East Asia.
\subsection{Hello Beijing} Beijing is the capital of China.
\subsubsection{Hello Dongcheng District}
\paragraph{Hello Tian'anmen Square}is in the center of Beijing
\subparagraph{Hello Chairman Mao} is in the center of Tian'anmen Square
\end{document}
```

### 参考文献

注意：参考文献有两个拓展的宏包，一个是 natbib 一个是 biblatex，他们是不兼容的。

#### BibTeX 文件类型

文献类型（reference type)
- @article
- @book
- @incollection: 表示一个章节
- @inproceedings: 会议论文

不引包，简单地插入文献列表。

```latex
\bibliographystyle{plain}
\bibliography{references}
```

#### 参考文献标注

使用 `\cite{citationkey}` 来在你想要引用文献的地方插入一个标注。
如果你不希望在正文中插入一个引用标注，但仍想要在文献列表中显示这次引用，使用 `\nocite{citationkey}` 命令。
想要在引用中插入页码信息，使用方括号：`\cite[p. 215]{citationkay}`
要引用多个文献，使用逗号分隔：`\cite{citation01,citation02,citation03}`

#### 引用格式

Plain 方括号包裹数字的形式，如 `[1]`。文献列表按照第一作者的字母表顺序排列。每一个作者的名字是全称。
Abbrv 与 plain 是相同的，但作者的名字是缩写。
Unsrt 与 plain 是相同的，但文献列表的排序按照在文中引用的先后顺序排列。
Alpha 与 plain 一样，但引用的标注是作者的名字与年份组合在一起，不是数字，如 [Kop10]。

### 注释和空格

% 代表评论，之后同一行的字都不会被输出
通常来说，LaTeX 忽略空行和其他空白字符，两个反斜杠（`\\`）可以被用来换行。
如果你想要在你的文档中添加空格，你可以使用 `\vaspace{...}` 的命令。
如 `\vspace{12pt}` 会产生一个空格，高度等于 12pt 的文字的高度。

### 特殊字符

下列字符在 LaTeX 中属于特殊字符，可以用 `\` 进行转义：

```text
# $ % ^ & _ { } ~ \
```

反斜杠不能通过反斜杠转义（换行），使用 \textbackslash 命令代替。

### 字体

#### 中文支持

推荐方法：改变布局和文中字

```latex
% UTF8 可带可不带
\documentclass[UTF8]{ctexart}
```

或者

```latex
\usepackage[UTF8]{ctex}
```

其他方法：不改变布局，只显示中文文字

```latex
\documentclass{article}
\usepackage{xeCJK}

\begin{document}
hello,你好
\end{document}
```

#### 字体效果

```latex
\textit{words in italics}
\textsl{words slanted}
\textsc{words in smallcaps}
\textbf{words in bold}
\texttt{words in teletype}
\textsf{sans serif words}
\textrm{roman words}
\underline{underlined words}
```

#### 彩色字体

```latex
\usepackage{color}
% green red blue cyan magenta yellow white
{\color{colorname}text}
\colorbox{colorname}{text}
```

#### 字体大小

```latex
normal size words
{\tiny tiny words}
{\scriptsize scriptsize words}
{\footnotesize footnotesize words}
{\small small words}
{\large large words}
{\Large Large words}
{\LARGE LARGE words}
{\huge huge words}
```

### 列表与表格

LaTeX 支持两种类型的列表：有序列表（enumerate）和无序列表（itemize）。

```latex
\begin{enumerate}
\item First thing
\item Second thing
\begin{itemize}
\item A sub-thing
\item Another sub-thing
\end{itemize}
\item Third thing
\end{enumerate}

% 修改头
\begin{itemize}
\item[+] A sub-thing
\item[-] Another sub-thing
\end{itemize}
```

```latex
\begin{table}
\caption{The Number of Iterations}
\centering 
% Each element in the tabular is left aligned
\begin{tabular}{l l}  % fist and second line aligned to left
\hline
iter1 & iter2  \\
\hline
31 & 25  \\
20 & 17  \\
45 & 37  \\
23 & 19  \\
\hline
\end{tabular}
\end{table}
```

表格（tabular）命令用于排版表格。LaTeX 默认表格是没有横向和竖向的分割线的——如果你需要，你得手动设定。LaTeX 会根据内容自动设置表格的宽度。l 表示一个左对齐的列.r 表示一个右对齐的列.c 表示一个向中对齐的列.| 表示一个列的竖线.
& 用于分割列.`\\` 用于换行.`\hline` 表示插入一个贯穿所有列的横着的分割线.`\cline{1-2}` 会在第一列和第二列插入一个横着的分割线


```latex
\begin{tabular}{|l|l|}
Apples & Green \\
Strawberries & Red \\
Orange & Orange\\
\end{tabular}

\begin{tabular}{rc}
Apples & Green\\
\hline 
Strawberries & Red \\
\cline{1-1}
Oranges & Orange \\
\end{tabular}

\begin{tabular}{|r|l|}
\hline
8 & here's \\
\cline{2-2}
86 & stuff\\
\hline \hline 
2008 & now \\
\hline 
\end{tabular}
```

### 符号和公式

数学公式, 希腊字母，以及特殊符号都需要在数学环境中使用。
如果是在同一行，使用`$表达式$`。 如果是另起一行, 使用`\[表达式\]` 或者 `$$表达式$$`。 

#### 矩阵

矩阵需要使用 package amsmath。
`$$` 之内不能有空行。

```latex
\documentclass{article}
\usepackage{amsmath}

\begin{document}
$$
\begin{bmatrix}  % bracket []
0 & 0 & 1 \\
1 & 0 & 0 \\
\end{bmatrix}
\begin{pmatrix}  % parentheses ()
1 & 4 & 0 \\
2 & 5 & 8 \\
\end{pmatrix}
\begin{vmatrix}  $ vertical ||
1 & 4 & 0 \\
2 & 5 & 8 \\
\end{vmatrix}
$$
\end{document}
```

#### 公式对齐

```latex
\begin{align}
53(4+x)+2x &= 212 + 53x + 2x \\ 
&= 212 + 55x  
\end{align}
```

### 插图

```latex
\usepackage{graphicx}
\begin{figure}
\includegraphics[scale=.5]{tmp.png}
\caption{fig: tmp}
\end{figure}
```

```latex
% others
\includegraphics[width=4.00in,height=3.00in]{figure1.eps}
```

### Markdown 与 Latex

- [以 Markdown 撰写文稿，以 LaTeX 排版 ](https://liam.page/2020/03/30/writing-manuscript-in-Markdown-and-typesetting-with-LaTeX/)

使用 markdown + pycharm 命令要带 `--shell-escape`

### latex 模板推荐

- [优雅： 书 论文 还有笔记](https://github.com/ElegantLaTeX)
- [ElegantPaper](https://coder.social/ElegantLaTeX/ElegantPaper)
- [清华论文 Latex 模板](https://github.com/tuna/thuthesis/)

## Links

- [LATEX 教程](https://zilutian.github.io/latex-tutorial-chinese/)
- [LaTeX 入门](https://oi-wiki.org/tools/latex/)
