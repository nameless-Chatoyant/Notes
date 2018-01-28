---

---
怎样去恢复 high perceptual quality and high frequency details

# Developing

#
# Video Super Resolution

连续帧之间。
微小的动作可以帮助保留更多的细节。
光流(optical flow)估计
block-matching

# Single Image
## edge-based

# Multiple Images / Video
利用spatial correlations来获取信息
motion estimation

# 附录

## 论文整理
- TPAMI 2015 | Chao Dong *et al.* **"Image Super-Resolution Using Deep Convolutional Networks"** [arXiv](https://arxiv.org/abs/1501.00092)
    > 引入CNN

- CVPR 2016 | Jiwon Kim *et al.* **"Accurate Image Super-Resolution Using Very Deep Convolutional Networks"** [arXiv](https://arxiv.org/abs/1511.04587)

- CVPR 2016 | Wenzhe Shi *et al.* **"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network"** [arXiv](https://arxiv.org/abs/1609.05158)
    > ESPCN。之前的Super Resolution都是基于经过bicubic插值得到的HR图提取feature，这篇论文认为基于HR图的计算增加了复杂度，从而提出Sub-Pixel Convolution，实现了从LR图提取feature

- CVPR 2017 | Jose Caballero *et al.* **"Real-Time Video Super-Resolution with Spatio-Temporal Networks and Motion Compensation"** [arXiv](https://arxiv.org/abs/1611.05250) [code]()
    > 引入STN，提出Motion Estimation，沿用了Sub-Pixel Convolution

- 2016-12-23 | Mehdi S. M. Sajjadi *et al.* **"EnhanceNet: Single Image Super-Resolution Through Automated Texture Synthesis"** [arXiv](https://arxiv.org/abs/1612.07919)

- ICCV 2017 | Xin Tao *et al.* **“Detail-revealing Deep Video Super-resolution”** [arXiv](https://arxiv.org/abs/xxxx) [code](https://github.com/jiangsutx/SPMC_VideoSR)
    > 沿用Motion Estimation，提出了SPMC layer(没有要学习的参数)，实现了End-to-End，第三部分Deep Fusion Net用了ConvLSTM

- 2017-12-16 | Bingzhe Wu *et al.* **"SRPGAN: Perceptual Generative Adversarial Network for Single Image Super Resolution"** [arXIv](https://arxiv.org/abs/1712.05927)
    > 之前普遍使用的pixel wise loss function，尽管可以让PSNR更高，但会让模型倾向于生成模糊且over-smoothing的图片，这篇论文引入GAN来，从而让生成的图片拥有更清晰的边缘和更丰富的细节

- 2017-12-17 | Assaf Shocher *et al.* **""Zero-Shot" Super-Resolution using Deep Internal Learning"** [arXiv](https://arxiv.org/abs/1712.06087) [PyTorch]()