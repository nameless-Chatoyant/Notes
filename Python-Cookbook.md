---
title: Python Cookbook
tags:
mathjax: True
---

***
在类的`__init__()`里常常需要写一些类似`self.a = a`的冗余代码，改用`locals()`
```

```
***
# 减少硬编码与magic number
用`slice()`来创建切片对象
用`namedtuple()`来将大量的magic索引转为用key索引
***
# 学会依赖轮子
计数、统计用`Couter`
迭代、数据结构用`itertools`和`collections`
`chain()`
字符串匹配按量级，string方法 < `fnmatch` < `re`
文件名匹配用`glob`
分数计算用`fractions`
串口通信用`serial`
处理数据，`csv`,`json`,`xml.etree.ElementTree`,`lxml`
定义接口、抽象类用`abc`
***
# 习惯矫正
复杂的筛选用`filter()`
`print()`用`sep`参数，而不是`'\n'.join()`
***
# 变量域
如何写出好的代码？`vars()`, `locals()`, `globals()`



# 常用
***
```
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)): for x in items:
    if isinstance(x, Iterable) and not isinstance(x, ignore_types):
        yield from flatten(x)
    else:
        yield x
```
# 类作数据结构臃肿的__init__()
基类公用`__init__()`
```
class Structure1:
# Class variable that specifies expected fields
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields))) # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```
其他类继承基类
```
class Point(Structure1):
    _fields = ['x', 'y']
```