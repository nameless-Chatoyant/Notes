
# @property
用来简化传统OOP中的getters/setters

## Usage


## Details

```python
class A:
    pass
a = A()
a.x = 1     # 为a添加属性x，并赋值为1，OK
a.x = 2     # 改变a.x的值，OK
print(a.x)  # 获取a.x的值，OK
```

```python
class A:
    def __init__(self):
        _x = 1
    @property
    def x(self):
        return self._x
```

此时调用`a.x`
- 函数的特性
如果在getter中添加一些副作用，依旧会被执行
```python
class A:
    _x = 1
    @property
    def x(self):
        print('calling x')
        return self._x

a = A()
a.x     # calling x
```
添加了`@property`装饰器的函数，将作为`getter`

如何在定义了getter之后再去修改这个函数呢?

对一个成员函数添加`@property`装饰器后，该函数将变成同名的成员变量，但此时是只读的

```python
type(a.x)   # int, 而非method
```
`._<类名>_<方法/属性名>`



- `__add__`: 加法`+`
- `__radd__`: 右侧加法
- `__iadd__`: 自增运算`+=`

- `__sub__`:



- `__isub__`: 自减运算`-=`
- `__ior__`: 自或运算`|=`
- `__iand__`: 自与运算`&=`


