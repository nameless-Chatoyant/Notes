---
title: Detail-revealing Deep Video Super-resolution
---

[](https://arxiv.org/abs/1611.05250)

backword warping: tf.gather_nd更好(tensorpack用的tf.gather)
forward warping: tf.scatter_nd

forward warping:

# 概述
[Super Resolution]()
在训练阶段，如果以end-to-end的方式训练整个网络（随机初始化）会导致运动估计的zero flow，从而使得最终结果近似于single-image SR
F_i\shortrightarrow 0

会做一次resize

源图像a
目标图像b
$F_a\shortrightarrow b$
warping分两种forward warping和backward warping
forward warping 源图像到目标图像
backward warping 目标图像到源图像

Motion Estimation(ME) Module得optical flow
SPMC layer根据optical flow warp原图并resize
Detail Fusion Net从多张LR的大图中还原细节得到HR的结果
# 模型
## Motion Estimation
ME模块继续沿用了[VESPCN]()的STN结构，
F_i\rightarrow j = Net_ME (I^L_i, I^L_j;\theta_ME)
![](imgs/me.png)
两张图I_t和I_t+1叠加成(1, H, W, 2)的Tensor作为网络的输入，经过Coarse flow estimation后得到(1, H, W, 2)的\delta, I_t+1与\delta做back warping得到对齐后的I_t+1
I_t, I_t+1, delta_x, delta_y, I_t+1叠加成(1, H, W, 5)的Tensor，经过Fine flow estimation得到\delta^f
\delta^f和\delta^c做加法，I_i+1与\delta做back warping，得I'_t+1，可通过肉眼判断l

其中的warp, 是给定F_i\rightarrow j和I_j，得I_i，即backend warping
是可选的，既可以得到F_i\rightarrow j也可以得到F_j\rightarrow i

sub-pixel upscale
PyTorch有nn.PixelShuffle或nn.functional.pixel_shuffle

原论文中的loss
改进loss:$$L_ME = \sigma^T_i=-T||I^L_i - I^L_0\rightarrowi||_1 + \lambda_1 ||||_1$$

## SPMC Layer
$J^H=Layer_SPMC(J^L,F;\alpha)$
