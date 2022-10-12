# YAML

YAML 是专门用来写配置文件的语言，非常简洁和强大，远比 JSON 格式方便

发音 /ˈjæməl/

## 语法特点

- 大小写敏感
- 使用缩进表示层级关系
- 缩进时不允许使用Tab键，只允许使用空格。
- 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
- 注释：`#`
- 数据结构
  - 对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
  - 数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
  - 纯量（scalars）：单个的、不可再分的值

```yaml
# 纯量
number: 12.30
isSet: true # 注意是小写
parent: ~ # null
date: 1976-07-31
e: !!str 123 # 强制类型转换
f: !!str true
str: 这是一行字符串
# 换行符会被转为空格
str: 这是一段
  多行
  字符串
# 多行字符串可以使用|保留换行符，也可以使用>折叠换行
this: |
  Foo
  Bar
that: >
  Foo
  Bar
# +表示保留文字块末尾的换行，-表示删除字符串末尾的换行
s1: |
  Foo
s2: |+
  Foo
s3: |-
  Foo
# 表示分文
---
```

## 参考

- [YAML 语言教程](https://www.ruanyifeng.com/blog/2016/07/yaml.html)
