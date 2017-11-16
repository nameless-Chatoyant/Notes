---
title: 【论文笔记】Convolutional Neural Networks for Sentence Classification
date: 2017-07-12 17:42:57
tags:
mathjax: true
---

将句子表示为词的序列

$$
x_{1:n} = x_1 \oplus x_2 \oplus \ldots\oplus x_n
$$

$$
w \in \mathbb{R}^{hk}
$$
选用大小的filter，即时域卷积，对于图像处理领域，filter大小可以直观地看作在图像上采集特征的格子，这个格子的长和宽决定了它采集的范围；而在自然语言处理上，卷积操作已经是针对word embedding之后的vectors了，选取小于k宽度的filter相当于把成形的词向量再分割提取特征，没什么实际的意义也没有好的效果。

$$
\sqrt{3x-1}+(1+x)^2
$$

$$
c_i = f(w · x_{i:i+h−1} + b)
$$

$$
{x_{1:h}, x_{2:h+1}, \ldots , x_{n−h+1:n}}
$$

$$
c = [c_1, c_2, \ldots , c_{n−h+1}]
$$

$$
c \in \mathbb{R}^{n−h+1}
$$


$$
\sqrt{3x-1}+(1+x)^2
$$

用了以下模型
- CNN-rand:
- CNN-static:
- CNN-non-static:
- CNN-multichannel:



预训练的word embedding对于深度学习进行NLP任务非常关键。