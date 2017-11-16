---
title: YOLO
date: 2017-08-08 11:20:49
tags:
---
# 相关论文
[[1506.02640] You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640)
[[1612.08242] YOLO9000: Better, Faster, Stronger](https://arxiv.org/abs/1612.08242)

# 概述

## 思路
图片resize后送入模型，通过卷积层得到high resolution和low resolution的特征提取结果，concatenate后再做卷积，最后一次是1x1卷积主要是控制输出维度为预测值的个数，得到prediction
prediction的shape为box数*(5+类数)
将prediction分为x, y, w, h, conf, prob，x, y, w, h确定框的位置，prob做softmax表示每一类的概率
对x, y, conf做sigmoid出最终结果
对w, h直接输出

预测结果是对于resized image的，如何将预测结果用到raw image上？

Non-maximum suppression: reduce num of boxes
IOU即Interaction Over Union，用IOU来衡量两个框的重叠程度

# Differences between YOLO and YOLOv2

# References