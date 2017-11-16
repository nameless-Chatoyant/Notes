---
title: 【任务综述】Image Caption
tags:
---
Image Caption，或者是Image Description。

# 概述
## 应用设想
1. 图片检索
2. 自动新闻报道
## 数据集
[Flickr8k](http://nlp.cs.illinois.edu/HockenmaierGroup/8k-pictures.html)
[Flickr30k](http://shannon.cs.illinois.edu/DenotationGraph/)
[COCO](http://cocodataset.org/)
COCO 2014数据集提供了100W的captions和16W以上的images
## loss
Image Caption作为一种生成式的任务，模型的结果好坏和其他生成式模型一样是难以定义的。
L(I,S)=-\sigmalogpt(S_t)
# 发展流程
## Other Ways
[From Captions to Visual Concepts and Back](https://arxiv.org/abs/1411.4952)
## Encoder-Decoder
[Show and Tell: A Neural Image Caption Generator](https://arxiv.org/abs/1411.4555)
[Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](https://arxiv.org/abs/1502.03044)
[What value do explicit high level concepts have in vision to language problems?](https://arxiv.org/abs/1506.01144)
[Mind’s Eye: A Recurrent Visual Representation for Image Caption Generation](https://www.cs.cmu.edu/~xinleic/papers/cvpr15_rnn.pdf)
[NeuralTalk](https://github.com/karpathy/neuraltalk)
[NeuralTalk2](https://github.com/karpathy/neuraltalk2)
[Deep Visual-Semantic Alignments for Generating Image Descriptions](https://arxiv.org/abs/1412.2306)
## GAN
[Generative Adversarial Text to Image Synthesis](https://arxiv.org/abs/1605.05396)
100多
[StackGAN- Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks](https://arxiv.org/abs/1612.03242)
100多
[Towards Diverse and Natural Image Descriptions via a Conditional GAN](https://arxiv.org/abs/1703.06029)

## 未分类


# 