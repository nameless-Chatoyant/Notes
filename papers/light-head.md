11月20日

目标检测



Jian Sun



RCNN->Fast R-CNN -> Faster R-CNN -> R-FCN



2-stage 速度慢，准确率高

2-stage方法概述

Light Head RCNN 

RCNN

CNN + SVM

Fast RCNN

ROI pooling：统一大小

ResNets

共享propersal的RCNN计算

Faster RCNN

RCNN Subnet

local

classification

RPN

分类起，对无穷多个框，样本比例不均衡

propersal

IoU

# 训练

好几百个propersal，每一个propersal都要过后续的网络



YOLOv2没有

降低propersal ->



R-FCN把RCNN subnet极大地简化了。

PSRoI

$$3*3*(C+1)$$

每一个channel针对某个位置

位移不变性



-> C+1维向量

light-head R-CNN

->FC层

降channel数的方式：1*1卷积->large kernel separable convolution

$h*w*c_{in}$ 1*k 

k*1

k*1

$c_in$





RoI pooling的做法

RoI pooling

RoI warping:

RoI alignment