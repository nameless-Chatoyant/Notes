---
title: 图像分割() 基于CNN的图像分割
date: 2017-07-10 14:41:21
tags:
---

虽然在CNN方向上FCN的成果已经很显著了，但FCN模型是比较复杂的，对于简单的任务CNN就可以胜任了。

[Fully Convolutional Networks for Semantic Segmentation](https://arxiv.org/pdf/1411.4038.pdf)是FCN的开创性论文，其中提到了几篇用CNN解决图像分割的问题：

> Prior approaches have used convnets for semantic segmentation[27, 2, 8, 28, 16, 14, 11], in which each pixel is labeled with the class of its enclosing object or region, but with short-comings that this work addresses.



- [Deep Neural Networks Segment Neuronal Membranes in Electron Microscopy Images](http://people.idsia.ch/~juergen/nips2012.pdf)
- [Learning Hierarchical Features for Scene Labeling](http://yann.lecun.com/exdb/publis/orig/farabet-pami-13.pdf)
- [Recurrent Convolutional Neural Networks for Scene Labeling](http://proceedings.mlr.press/v32/pinheiro14.pdf)

其他资料：

- [Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs](https://arxiv.org/pdf/1412.7062.pdf)
- [One-Shot Video Object Segmentation](https://arxiv.org/pdf/1611.05198.pdf)
- [Shape Guided Object Segmentation](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/Borenstein06.pdf)


CNN常用在图片的分类问题上，把CNN迁移到图片分割问题上通常的做法是这样的：

> 传统的基于CNN的分割方法的做法通常是：为了对一个像素分类，使用该像素周围的一个图像块作为CNN的输入用于训练和预测。这种方法有几个缺点：一是存储开销很大。例如对每个像素使用的图像块的大小为15x15，则所需的存储空间为原来图像的225倍。二是计算效率低下。相邻的像素块基本上是重复的，针对每个像素块逐个计算卷积，这种计算也有很大程度上的重复。三是像素块大小的限制了感知区域的大小。通常像素块的大小比整幅图像的大小小很多，只能提取一些局部的特征，从而导致分类的性能受到限制。
>
> [全卷积网络（FCN）与图像分割](http://blog.csdn.net/taigw/article/details/51401448)

