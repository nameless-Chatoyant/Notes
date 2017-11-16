---
title: R-CNN
date: 2017-08-08 11:20:49
tags:
---

# 相关论文
从上到下分别是R-CNN, Fast R-CNN, Faster R-CNN
- [[1311.2524] Rich feature hierarchies for accurate object detection and semantic segmentation](https://arxiv.org/abs/1311.2524)
- [[1504.08083] Fast R-CNN](https://arxiv.org/abs/1504.08083)
- [[1506.01497] Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/abs/1506.01497)

# 模型概述

detection被当作分类问题来处理还是比较直观好理解的，naive solution大概是遍历像素，结合周围的像素对该像素进行分类，这样的解决方案自然会有难以顾及全局信息、重复计算、性能低下等问题。一系列R-CNN
R-CNN使用selective search来得到region proposals，使用一个CNN实现来提取每个region proposal的features，使用SVM来分类。


# 模型详解
面对数据匮乏的问题，在大容量的辅助数据集上做预训练，然后在特定领域的数据集上做fine tuneing

# 代码实践