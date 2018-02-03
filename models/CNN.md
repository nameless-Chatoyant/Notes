# 附录
## 论文整理
- ICCV 2017 | Dai, Jifeng *et al.* "Deformable Convolutional Networks" [arXiv](http://arxiv.org/abs/1703.06211) [PyTorch](https://github.com/oeway/pytorch-deform-conv)
    > 加入了学习offset，卷积核可变



目前Convolution Layer已经变成了神经网络中一个基本的模块，基于CNN的变种中也有一些被广泛应用。学习CNN最好追根溯源从其发明伊始说起。

理论上，层的全连接网络。而且DNN到CNN，网络的参数量是变少了的。那么为什么要发明CNN呢？

以计算机视觉举例，参数量将达到足足30亿

1. 如此高的参数量，却没有相应数量的训练样本，很容易过拟合
2. 如此大体量的网络，在计算上是不可接受的

# 计算过程
直观过程
[comment]: # (加那个眼熟的动图)

# padding

1. 保持size
2. 不同位置的点，权重不同


1. 当f为偶数是，padding就是不对称的
2. 奇数维的filter，中心点

在数学和信号处理中的卷积，在计算前会翻转卷积核，但在深度学习中翻转并不需要，因为卷积核是学习的