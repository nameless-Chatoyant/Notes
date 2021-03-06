# 知识点
## 缩写与简称
SDU: 服务数据单元
PDU: 协议数据单元
MSC: Message Sequence Chart
SDL: Specification and Description Language

## SDL Suite
- Editor: 图形化的SDL编辑。
- Simulator: 仿真
- Validator: 验证
- Translator: 自动生成SDL代码和C代码

### 仿真过程
Full Make后，使用Simulator
- Execute域: 可以单步执行，全部执行，执行一个状态转移，执行到某一定时器位置。
- Send Signal域: 信号模拟，可以指定接收方、信道，或是自发输入。
- Examine域: 可以查看各种变量的值以及变化情况
- Trace域: 可以跟踪查看MSC图和SDL图

### 验证过程
- 验证静态语法错误：使用语法分析器
    使用Analyze
- 验证运行时动态错误：Full Make后，使用Validator
    在Validator中，整个SDL系统以行为树的结构表示，每个节点代表一个状态，所有状态的集合称为状态空间。通过遍历状态空间，可以验证运行时动态错误。除了验证SDL错误，使用Verify-MSC遍历的信息报告中还会显示该SDL系统中是否有可执行的路径来满足载入的MSC图。

# MSC
## 概述
### MSC和HMSC
简单MSC图: 描述一个系统中若干组件之间的通信行为和组件与系统外部环境之间的通信行为。
高级MSC图: 描述简单MSC图的连接关系和结构关系。
引用关系: 简单MSC图**可能**引用其他MSC图，**不引用**高级MSC图。高级MSC图**一定引用**简单MSC图。


文本文法和图形文法
## 图形文法
### MSC图
### 实例
实例: 可以是系统、功能块、进程。
实例头部、实例轴、实例终止符
### 消息
### 条件
### 定时器
启动定时器符号
再启动定时器符号
定时器终止符
定时器超时符
### 动作
### 创建进程和进程终止
### 方法调用与回复
### 环境与通道
### 并发
### 引用
### 线内表达式
- alt: 二选一。相当于`if ... else ...`.
- opt: alt的特殊情况。相当于`if ...`.
- exc: 表示异常。当exc内的事件发生后，该MSC图就结束了。否则继续exc下面的过程。
- loop: 循环.`loop<n,m>`表示至少循环n次，至多循环m次。
- par: 并行

## 高级MSC
### 开始符
### 结束符
### MSC引用符
### 条件符
### 连接点
### 并行框

# SDL
## 概述

系统可以划分成若干功能块，功能块可以划分功能块，也可以划分成若干进程。

## 图形文法
### SDL图
### package
定义
```
package 包名

```
### 进程


### 开始域
### 状态域
### 输入符
### 优先输入符
### 连续信号符
### 保存符
### 输出符
### 实例创建符
### 动作
### 分支操作
### 连接
### 过程
### 远端过程
信号:进程之间通信的基本单位
信道:实体与实体之间或实体与环境之间传递信号的通道，用带箭头的连线表示。需列出信道名、信号。
## 定时器
设置定时器: `set(<时间表达式>, <timer>)`
复位定时器: `reset(<timer>)`
定时器超时: 用包含定时器名的输入符

## 定义变量
```
dcl 变量名 数据类型;
```
内置类型:
- Boolean:布尔型
- Character:字符型
- Charstring:字符串型
- Integer:整型
- Natural:自然数型
- Real:实数型
- Pid:进程标识型
- Duration:时长类型
## 定义新数据类型
- 定义串类型
    ```
    newtype 串类型名
        string(串元素类型, 空串标识)
    endnewtype;
    ```
- 定义数组类型
    ```
    newtype 数组类型名
        array(数组索引项类型, 数组元素类型)
    endnewtype;
    ```
- 定义结构类型
    ```
    newtype 结构类型名 struct
        字段1名 字段1类型;
        字段2名 字段2类型;
        ...
    endnewtype;
    ```
    访问结构变量的子段: `结构变量!子段`
- 定义字面量类型
    ```
    newtype 字面量类型名
        literals 字面量名1, 字面量名2, ..., 字面量名n
    endnewtype;
    ```
- 定义选择类型
    ```
    newtype 选择类型名 choice
        字段1名 字段1类型;
        字段2名 字段2类型;
        ...
    endnewtype;
    ```
- 继承
    ```
    newtype 类型名 inherits 父类型名
    endnewtype;
    ```
    ```
    newtype 类型名 inherits 父类型名 adding

    endnewtype;
    ```
## 定义同义类型
```
syntype 同义类型名 = 原数据类型名[约束条件]
endsyntype;
```

```
syntype dev_no = Integer constants 0:127
endsyntype;
```

## 模板
- 定义一个有128个元素的PID型数组类型
    ```
    syntype dev_no = Integer constants 0:127
    endsyntype;

    newtype A
        array(dev_no, PID)
    endnewtype;
    ```
SDL定义新变量
SDL系统图：
功能块之间、功能块与环境通信：信号


# 概述
MSC: 描述协议的通信行为, 描述多个实体之间和实体与环境之间消息交互的顺序
SDL: 描述协议的系统结构和系统行为


# 画图题
背图是不可能背图的，记一下场景。

MSC思路: 
- 定时器操作：这个场景下有没有启动过定时器，基于定时器超时的场景
- 该引用的引用
## 微型电话交换机
[comment]: # (拨号过程)
- 摘机拨号
    1. 主叫摘机信号传给系统
    2. 给主叫放播号音，启动定时器
    3. 主叫拨号之后停止播号音，
    4. 每次拨号都会复位并重新启动定时器
- 用户早释
    1. 与**摘机拨号**类似，但在每个拨号循环里，在拨号前有`exc`
    2. `exc`和结尾的内容：主叫挂机，复位定时器，进入*idle*状态
- 久不拨号
    1. 与**摘机拨号**类似，但在每个拨号循环里，在拨号前有`exc`
    2. `exc`和结尾的内容：定时器超时，复位定时器，进入*idle*状态

[comment]: # (建立连接过程)
- 被叫用户空闲
    1. 引用**摘机拨号**过程
    2. 给主叫放回铃音，给被叫放响铃，复位定时器(为了触发久不拨号)，设定定时器(接听时限)，进入*seizure*状态
- 被叫用户忙
    1. 引用**摘机拨号**过程
    2. 给主叫放忙音，复位定时器(为了触发久不拨号)，设定定时器(用于停止忙音)，进入*busy_tone*状态
- 空号
    1. 引用**摘机拨号**过程
    2. 给主叫放空号音，复位定时器(为了触发久不拨号)，设定定时器(用于停止空号音)，进入*null_tone*状态
- 应答
    1. 系统最初处于*serizure*状态
    2. 被叫摘机，复位定时器(接听时限)，停止回铃音和铃声，建立话路
    3. 进入*connected*状态

[comment]: # (求求你快接电话)
- 振铃早释
    1. 系统最初处于*seizure*状态
    2. 主叫挂机，停止回铃音和铃声，复位定时器(接听时限)
    3. 进入*idle*状态
- 久叫不应
    1. 系统最初处于*seizure*状态
    2. 定时器超时(接听时限)，停止回铃音和铃声，主叫播放忙音，设定计时器(用于停止忙音)
    3. 进入*busy_tone*状态，注意这里主叫没挂机的话是不能进入*idle*状态的

[comment]: # (和你聊天真开心，为我们的友谊干杯)
- 释放
    1. 系统最初处于*connected*状态
    2. 用`alt`来表示“不是你先挂，就是我先挂”
        - 一方挂机，系统断开话路，另一方播放忙音
        - 系统进入*busy_tone*状态，因为是主叫先挂机和被叫先挂机两种情况，这里应该是两种*busy_tone*状态

[comment]: # (忙音和空号音)
- 忙音状态挂机
    1. 系统最初处于*busy_tone*状态
    2. 挂机，复位定时器(用于停止忙音)
    3. 进入*idle*状态
- 空号音状态挂机
    1. 系统最初处于*null_tone*状态
    2. 挂机，复位定时器(用于停止空号音)
    3. 进入*idle*状态
## ATM

## 滑动窗口协议