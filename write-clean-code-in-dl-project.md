---
title: Write Clean Code in Deep Learning Project
tags:
---



- 项目
    project/
        Model1/
        Model2/
        ...
        demo.py
    workbench/

    demo只需要模型文件夹中的一部分，甚至是网络的一部分。但在开发过程中直接使用开发版的模型，免去每次更改都要改动两个地方的麻烦。

- 逻辑不仅关乎算法性能，也关乎业务代码的复杂度。如果业务代码一团糟，想一想是不是有简单的逻辑可以选择。

- 多读代码，同一类工具每个实现都有不同的设计模式，思考这样设计的好处是什么，取其精华。