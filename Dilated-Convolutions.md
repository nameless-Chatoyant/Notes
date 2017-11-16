---
title: Dilated Convolution
tags:
---

# 相关论文
- [[1511.07122] Multi-Scale Context Aggregation by Dilated Convolutions](https://arxiv.org/abs/1511.07122)
- [[1606.00915] DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs](https://arxiv.org/abs/1606.00915)
- [[1706.05587] Rethinking Atrous Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1706.05587)

# 概述
Dilated Convolution又名Atrous Convolution，是为了解决Image Segmentation问题而诞生的CNN变体。

在FCN出现之前，分割任务所用的方法主要是Patch Classification，以顺应技术进步的角度来看是很符合直觉的一种方法。利用像素周围的图像块对每一个像素进行独立的分类，而当时参与。
2014年，FCN的诞生将端对端卷积网络引入到Segmentation的任务中。该作
2015年，带孔卷积被提出
DeepLabv1在Arxiv上被提交是在2014年12月，当时还没有带孔卷积。2016年，DeepLab从v2开始使用带孔卷积来进行图像分割任务。


# 模型详解


# 代码实践
> 参考：
- [Identity Mapping]()
