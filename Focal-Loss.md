---
title: Focal Loss
tags:
---

# 相关论文
- [[1708.02002] Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002)

# 概述
Focal Loss是为了解决样本不平衡问题而被提出的，可以说Focal Loss是一种思想，因为在论文里也有提到，并非只有论文主要探讨的一种公式可以达到论文的目的。
![](http://upload-images.jianshu.io/upload_images/3197118-6442f8bb87076cbf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
整篇论文的思想可以由这张论文开头的图表来概括。用置信度(confidence)来衡量一个样本的难易程度，根据置信度来为这个样本的loss乘以一个weight，最终使得较难的样本(低置信度)的loss占更大的权重，而较易得样本(高置信度)loss的权重就小一些。
训练模型的过程就是降低的过程，
> 关于样本不平衡可以看[]()


# 详解
Cross Entropy作为loss
balanced loss
## 不平衡样本
论文以一种新奇的方式解读了先前1-stage与2-stage性能上产生显著差异(例如，YOLOv2的mAP是Faster R-CNN的%)的原因，那就是处理不平衡样本的能力不同。
先前的2-stage方法已经起到了一定的样本规范化的作用：
1. 选取proposal的过程中，
2. 
反观1-stage方法
1. 没有类似选取proposal这样压缩样本容量的过程，需要直接处理远超过的样本。
2. 
如此一来，。


##
> 谁控制了loss，就掌控了梯度下降的方向。 ——赤木刚宪

## Focal Loss与Softmax结合
Focal Loss是基于CE(Cross Entropy)公式的改进，

# 效果

既然Focal Loss是为了解决样本不平衡问题，所以把手头几个存在样本不平衡问题的模型魔改到Focal Loss版本，来观察性能的变化。

- 原论文所述，
- [marvis/pytorch-yolo2: Convert https://pjreddie.com/darknet/yolo/ into pytorch](https://github.com/marvis/pytorch-yolo2)在RegionLosss部分用FocalLoss替代CrossEntropyLoss，得到了大概1%的mAP提升




## 其他细节
论文还讲述了许多关于样本不平衡的细节，整理到专门讨论Class Imbalance的文章当中。
# 代码实践
> 收集了一下github上的实现：
- Tensorflow：一篇PR[Pull Request #12257](https://github.com/tensorflow/tensorflow/pull/12257/commits/832e3dab4349a0095ab6a5e16d43355db07343e0)
- PyTorch 
[pytorch_workplace/focalloss](https://github.com/DingKe/pytorch_workplace/tree/master/focalloss)

[]()
接着就是具体问题的代码了