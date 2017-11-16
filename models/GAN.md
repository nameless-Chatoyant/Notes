---
title: GAN
date: 2017-09-15 17:34:50
tags:
---

# 相关论文
- GAN([Generative Adversarial Networks](https://arxiv.org/abs/1406.2661))
- CGAN([Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784))
- DCGAN([Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434))

# 概述
正如开山之作[Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)中的第一句话所言，GAN是一个评估generative models的框架。它的提出解决了生成模型难以确定优化目标的问题。回归机器学习的一个定义：

> 对于某类任务T和性能度量P,如果一个计算机程序在T上以P衡量的性能随着经验E而自我完善,那么我们称这个计算机程序从经验E中学习。

生成模型一直没能像判别模型一样硕果累累的原因之一就是其中的P难以衡量。举例说明，如果是一个区分图片包不包含猫的模型，cost的计算都很简单而且符合直觉，然而对于一个生成猫的图片的模型，如何衡量模型的输出像不像猫？对于人类而言，“猫”之所以为“猫”大体是因为有：。然而这些直觉上的认知却很难转化为规则，即便写出这样的规则，模型按照这样的规则，大概最终会生成一张逐像素计算非常符合“猫”，实际上是一团糟的图片。

GAN的有趣之处。

稍稍跑偏一点，GAN的设计不管是从竞争的角度还是二分心智的角度来说都美感十足，虽然Hinton刚呼吁过深度学习应该另起炉灶，私以为对抗式网络和增强学习可以说是目前人工智能成果里最能引发人们对General AI的遐想的成果了。

# 发展

2014年，开山之作GAN([Generative Adversarial Networks](https://arxiv.org/abs/1406.2661))发表。



## 初版GAN

概括一下初版GAN的一系列问题：
unhealthy competition

###variation缺失
GANs have a tendency to capture only a subset of the vatiation found in training data

### high-resolution问题
[AC-GAN](https://arxiv.org/abs/1610.09585)


## WGAN

## Progressive Growing of GANs



# 数学证明
