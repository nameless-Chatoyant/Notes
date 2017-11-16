---
title: 【经典模型】ResNets
date: 2017-08-08 11:20:49
tags:
---

# 相关论文
- [[1512.03385] Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
- [[1603.05027] Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027)

# 模型概述
ResNets是为了解决过深网络难以训练的问题而提出的CNN变体，对应的baseline应该是Plain Network，即简单地堆叠卷积层，ResNets在Plain Network的基础上加入了Shortcut Connections，把Plain Network的每一层看作接受上一层的输入x，向下一层输出F(x)，而Shortcut Connection可以看作每一层接受输入x，向下一层输出F(x)+x。
![](http://upload-images.jianshu.io/upload_images/3197118-c8748560a7a329f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 为什么过深网络难以训练？其实就是梯度消失／梯度爆炸问题，详见[]()。



# 模型详解
## Deeper Bottleneck Architectures
bottleneck是作者出于计算效率的考虑而魔改的结构，被用在了50层及以上的网络结构中
。其中涉及到一个1*1卷积的黑科技，此处的作用是降维。
![](http://upload-images.jianshu.io/upload_images/3197118-4f6cf50e2b5ad513.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
还是网络整体结构的图片，

因为在CNN这种基础设施上取得了显著进步，classification, detection, localization, segmentation，当年计算机视觉的任务基本被碾压个遍……
在Object Detection问题上，作者选用了Faster RCNN作为baseline，并用ResNet-101替代了其中的VGG-16（只有这一项魔改），单是学习表示的改进就让整体结果有了显著提高。所以至少是本人接触过的FasterRCNN实现，已经把VGG Net换成ResNets了。

# 代码实践
> 参考：
- [Identity Mapping]()

# 更新情况
整理ResNets相关的更新.
## [Super-Convergence: Very Fast Training of Residual Networks Using Large Learning Rates](https://arxiv.org/abs/1708.07120)
顾名思义，用