
代码实现：
[U-Net_for_singing_voice_separation-pytorch]()
# 概述




经过mask的spectrogram和目标spectrogram的距离
dasd
$$L(X, Y; \theta) = || f(X,0) X - Y||$$
L(X, Y ; Θ) = ||f (X, Θ) ⊙ X − Y ||1,1 (1)

会带来细节上的失真，这种失真在图像，但对于时域信息来说是致命的。

基于mask的方法，naturally combine source


# 改进空间

loss