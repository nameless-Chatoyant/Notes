# 概述
软件工程: 是一门工程学科，不仅涉及软件开发，也涉及软件项目管理、支持软件生产的工具、方法和理论的开发等活动。

# 3. 软件开发过程
## 软件开发模型
### 瀑布式模型
需求分析 体系结构设计 编码 测试 项目交付
### 增量式模型
每次迭代以**增量**为单位，指需求明确、可以很好量化的部分。
比如开发一个图像处理库
1. dataflow + operation的框架
2. 各种图像处理函数，比如各种resize, warp, crop ...
增量就是这些在开发前就很明确，开发起来也很舒服的features。有了框架，以后不停地填坑就好了。
随着开发的进行，一开始不怎么明确的需求也会逐渐清晰。
### 渐进式模型
每次迭代不是填坑，而是探索。
比如那款OCR软件……从demo到交付产品，没什么“增量”可言，但确实更成熟了。

问题
- 缺乏过程的可见性
- 系统通常不能够很好的结构化
- 可能需要特殊技巧 (例如，快速原型语言)
应用
- 中小规模的交互式系统
- 大系统的一部分（例如，用户接口）
- 生命周期较短的系统

### 螺旋式模型
在渐进式模型的基础上加上了对商业风险的考量，把每次迭代过程分成了具体的步骤，以保证迭代的效率，从而适应快速变动的市场。
计划下个阶段 确定目标、可选方案、约束条件 评估可选方案，识别和解决风险 开发验证下一代产品



# 5. 可依赖性
计算可用性：
MTTF / (MTTF + MTTR) * 100%
其中
- MTTF: 平均失效时间
- MTTR: 平均维修时间
# 8. 需求工程
分为功能需求和非功能需求
结构化语言描述需求


# 9. 建模与图示化表达
周境图、数据流图、流程图、泳道图、消息顺序图

# 12. 代码工程
代码复杂度度量
McCabe
$$V(G) = e - n + p$$
其中
- e: 边数
- n: 结点数
- p: 连通部件数

# 13. 软件测试理论与技术
测试只能证明程序有错。

白盒测试: 根据**程序内部逻辑**和**覆盖标准**确定测试数据, 测试内部操作和对外表现
黑盒测试: 根据**功能设计规格**，测试对外表现

- 完全路径覆盖: 完全路径指从程序的开始结点到终结点的一个路径。如果完成了完全路径充分覆盖，说明代码的各种可能组合都被测试。
- 语句覆盖: 语句覆盖率 = 执行过语句 / 总语句数
- 分支覆盖: 分支覆盖率 = 执行过分支 / 总分支数
- 多条件分支覆盖: 分支的判定是多条件时，所有条件的可能组合。如`a==0 && b==0`，测试用例就是00,01,10,11四种
- MC/DC覆盖: 在判定中，每个条件都要独立的影响判定结果一次（独立影响：其他条件不变，只改一个条件）。如`a==0 && b==0`，分支充分覆盖的用例是`a=0, b=0`和`a=1, b=1`，MC/DC充分覆盖还需加一个`a=0, b=1`

# 14. 软件测试工程

# 16. 质量管理与控制

质量控制

代码错误率
质量区间

# 18. 敏捷开发

XP(eXtreme)
Scrum