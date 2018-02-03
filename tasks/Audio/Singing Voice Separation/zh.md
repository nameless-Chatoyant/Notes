---
title: Singing Voice Separation
tags:
mathjax: true
---
# 目录
- [概述](#概述)
- [前置技能点](#前置技能点)
  - [STFT & ISTFT](#前置技能点-STFT&ISTFT)
- [方法](#方法)
- [总结](#总结)
- [附录](#附录)
  - [论文整理](#附录-论文整理)
  - [参考](#附录-参考)

Music Source Separation

# Overview
Singing Voice Separation, 顾名思义从音乐中分离人声和伴奏。在信号处理学科，属于Blind Source Separation, 即不从信号混合过程获得额外信息，从一组混合后的信号分离出源信号来。一组混合信号到多组源信号，从信息量来说是一个由少到多的过程，所以又与Music Information Retrieval挂钩。

不同于深度学习在视觉领域的火热，Singing Voice Separation的算法都还相当依赖于传统算法，模型复杂效果不尽如人意，留给深度学习的进步空间还很大。

由于扒伴奏已经投入到日常应用当中了，所以不太可能想到这项任务的艰辛。到目前为止还没有效果满意的自动声伴分离应用，原因如下：
- 无中生有。需要生成原先不存在（在混音过程中丢失）的信息。
- 目标不明确。何为人声何为伴奏？举一个最典型的例子，阿卡贝拉的伴奏同样是人声制造的，人声和伴奏之间的差别其实是很难定义的。
- 如果利用有监督学习的方法。数据量小。获取训练数据的成本高。

应用：
- 自动校音(automatic pitch correction)
- 自唱评分(singing skill evaluation for Karaoke)
- 哼唱查询(query-by-humming)
- 歌唱合成(singing synthesis)，例如V家

## References
- ICASSP
  > As ranked by Google Scholar's h-index metric in 2016, ICASSP has the highest h-index of any conference in Signal Processing field.
    2019.3.12 ~ 2019.3.17, DDL未定
- ISMIR & MIREX

## 相关论文

[Vocal Activity Informed Singing Voice Separation With the iKala Dataset](https://pdfs.semanticscholar.org/cde4/791e5da32f8c26c02f4828943325e8471dc0.pdf)
[Informed Group-Sparse Representation for Singing Voice Separation](http://mac.citi.sinica.edu.tw/ikala/chan17spl.pdf)
[Melody Extraction from Polyphonic Music Signals using Pitch Contour Characteristics](http://mtg.upf.edu/system/files/publications/SalamonGomezMelodyTASLP2012.pdf)

## Scoring Metrics
作为一项生成任务，以下是MIREX等比赛使用过的。

均越高越好
全局正则信号失真比 GNSDR = Global Normalized Signal-to-Distortion Ratio 
正则信号失真比 NSDR = Normalized Signal-to-Distortion Ratio

|  缩写  |              全称               |                    公式                    |
| :--: | :---------------------------: | :--------------------------------------: |
| SDR  |  Source to Distortion Ratio   | $$SDR = 10log_{10}\frac{\parallel s_{target}\parallel^2}{\parallel e_{interf} + e_{noise} + e_{artif}\parallel^2}$$ |
| SIR  | Source to Interferences Ratio | $$SIR = 10log_{10}\frac{\parallel s_{starget}\parallel^2}{\parallel e_{interf}\parallel^2}$$ |
| SNR  |    Sources to Noise Ratio     | $$SNR = 10log_{10}\frac{\parallel s_{starget} + e_{interf}\parallel ^2}{\parallel e_{noise}\parallel ^2}$$ |
| SAR  |  Sources to Artifacts Ratio   | $$SAR = 10log_{10}\frac{\parallel s_{starget} + e_{interf} + e_{noise}\parallel ^2}{\parallel e_{actif}\parallel ^2}$$ |

$$NSDR(S_e, S_r, S_m) = SDR(S_e, S_r) - SDR(S_m, S_r)$$

可以使用[BSS Eval](http://bass-db.gforge.inria.fr/bss_eval/)

## Datasets
|                   数据集                    |  说明  |
| :--------------------------------------: | :--: |
| [MIR-1K](https://sites.google.com/site/unvoicedsoundseparation/mir-1k) |      |
| [iKala](http://mac.citi.sinica.edu.tw/ikala/) |  主役  |
| [MedleyDB](http://medleydb.weebly.com/)  |      |

# 前置技能点
## STFT & ISTFT
STFT的全称是short-term Fourier transform，即短时傅里叶变换。
ISTFT则是inverse short-term Fourier transform，反短时傅里叶变换。

# 方法

IdBM(Ideal Binary Mask)
Masking-based: learn to predict the ideal binary or soft mask
Mapping-based: learn a regression function from a mixed signal to clean source signals directly
基于低秩(low-rank based)：
基于蒙版(Masking-based)：预测一个IdBM或IdSM
基于映射(Mapping-based)：从混合信号学习一个回归函数来清理出源信号
## 基于低秩(low-rank based)
基于低秩方法指的是，假设音乐中伴奏是低秩的而人声是离散的，从而提出的基于前／背景分离模型。
![](imgs/low-rank_assumption.png)
[Singing-Voice Separation from Monaural Recordings using Robust Principal Component Analysis](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.294.6722&rep=rep1&type=pdf)
中提出了第一个完整的离散声音(前景)+低秩音乐(背景)的模型
![](imgs/rpca_for_singing_voice_separation.png)
### PCA(Principal Component Analysis)
主成分分析法
### RPCA(Robust Principal Component Analysis)
![](imgs/rpca_for_foreground/background_separation)

缺点：
- 无监督
- 假设太强，比如鼓点就是离散的
- 没有考虑音调、结构等信息
  [Low-rank Representation of both Singing Voice and Music Accompaniment via Learned Dictionaries](http://www.ppgia.pucpr.br/ismir2013/wp-content/uploads/2013/09/17_Paper.pdf)提出了多种低秩表示
  RPCA(low-rank music + sparse voice)
  $$||L||_* + \lambda||M-L||_1$$
  LRR(low-rank music over a dictionary + sparse voice)
  $$||Z_L||_* + \lambda||S||_1 + \gamma||M - D_LZ_L - S||^2_F$$
  MLRR(low-rank music + low-rank voice over separate dictionaries)
  $$||Z_L||_* + \beta||Z_S||_* + \lambda||M - D_LZ_L - D_SZ_S||_1$$

## REPET(REpeat Pattern Extraction Technique)
假设存在阶段性重复的模式(periodically repeating patterns)
识别重复元素，得到重复模型，抽取重复模式
![REPET](imgs/repet.png)

![Adaptive REPET](imgs/adaptive_repet.png)
假设的错误：
这些重复也有可能是间断的，或者without a global (or local) period


## 基于蒙版(masking-based)
时频掩码(Time-Frequency Mask)
离不开generalized Wiener filtering的后操作
单声道：[Monaural Singing Voice Separation with Skip-Filtering Connections and Recurrent Inference of Time-Frequency Mask](https://arxiv.org/abs/1711.01437)提出

## 基于映射(mapping-based)
non-negative matrix factorization
贝叶斯

ISMIR 2014上，[Singing-Voice Separation From Monaural Recordings Using Deep Recurrent Neural Networks](http://paris.cs.illinois.edu/pubs/huang-ismir2014.pdf)

[Singing Voice Separation and Vocal F0 Estimation based on Mutual Combination of Robust Principal Component Analysis and Subharmonic Summation](https://arxiv.org/abs/1604.00192)

[A Deep Ensemble Learning Method for Monaural Speech Separation](http://www.xiaolei-zhang.net/papers/Zhang,%20Wang%20-%202016%20-%20A%20Deep%20Ensemble%20Learning%20Method%20for%20Monaural%20Speech%20Separation.pdf)

### SVSGAN
[SVSGAN: Singing Voice Separation via Generative Adversarial Network](https://arxiv.org/abs/1710.11428)
![](imgs/SVSGAN.png)
使用CGAN
### U-Net
[Singing Voice Separation with Deep U-Net Convolutional Networks](https://ismir2017.smcnus.org/wp-content/uploads/2017/10/171_Paper.pdf)
![](imgs/u-net.png)
U-Net架构: 
作为比较先进的尝试，性能上GAN架构目前是落后U-Net架构的。引入了在CV界成功的模型从而摒弃了之前繁复的计算，具有探索价值。
### Skip-Filtering Connections
[Monaural Singing Voice Separation with Skip-Filtering Connections and Recurrent Inference of Time-Frequency Mask](https://arxiv.org/abs/1711.01437)
![](imgs/mss.png)
# 总结
2012年，第一次引入
2017年，基于GAN和U-Net的模型出现，开始摒弃之前繁复的计算。

基于低秩、基于重复模式等强假设方法只能
我们可以预见到，理想中的方法有以下特点
- 基于源
  low-rank based, 

baselines: Chimera
Bayes
# 深度学习总结
Encoder-Decoder架构：
GAN架构
优点在于发现global patterns，缺点是丢失了local features

在图像生成任务，一个像素的位移是无关紧要的，而在频域生成，即使是频谱图的微小线性变化也会让听感由于频率的对数感知，这在音乐信号中特别重要;此外，时间维度的变化可能会变成听觉抖动和其他伪影。

instrumental版本比较少

时间维度的变化上：

mask



# 附录
## 论文整理

- 2015-04-17 | Andrew J.R. Simpson *et al.* **“Deep Karaoke: Extracting Vocals from Musical Mixtures Using a Convolutional Deep Neural Network”** [arXiv](https://arxiv.org/abs/1504.04658) [code](https://github.com/jaidevd/deep_kareoke_source_separation)
  > 有监督NMF和CNN对比

- ISMIR2014 | Po-Sen Huang *et al.* **"Singing-Voice Separation From Monaural Recordings Using Deep Recurrent Neural Networks"** [pdf](http://paris.cs.illinois.edu/pubs/huang-ismir2014.pdf)

- 2016-11-18 | Yi Luo, Zhuo Chen *et al.* **”Deep Clustering and Conventional Networks for Music Separation: Stronger Together“** [arXiv](https://arxiv.org/abs/1611.06265) [demo](http://danetapi.com/chimera)
  > chimera，后续论文经常拿来做baseline

- 2017-10-31 | Zhe-Cheng Fan *et al.* **"SVSGAN: Singing Voice Separation via Generative Adversarial Network"** [arXiv](https://arxiv.org/abs/1710.11428) [demo](http://mirlab.org:8080/demo/SVSGAN/) [static](http://mirlab.org:8080/demo/SVSGAN/svsgan_paper_result.html)

- 2017-11-04 | Stylianos Ioannis Mimilakis *et al.* **"Monaural Singing Voice Separation with Skip-Filtering Connections and Recurrent Inference of Time-Frequency Mask"** [arXiv](https://arxiv.org/abs/1711.01437) [code](https://github.com/Js-Mim/mss_pytorch)
  > 后处理中把generalized Wiener filtering改进成可学习的filtering

- ISMIR 2017 | Andreas Jansson *et al.* **"Singing Voice Separation with Deep U-Net Convolutional Networks"** [pdf](https://ismir2017.smcnus.org/wp-content/uploads/2017/10/171_Paper.pdf) [demo](http://mirg.city.ac.uk/codeapps/vocal-source-separation-ismir2017)
  > vocal和non-vocal分别训练

- ICASSP2018 | Hyeong-seok Choi *et al.* **"Singing Voice Separation using Generative Adversarial Networks"** [pdf](http://media.aau.dk/smc/wp-content/uploads/2017/12/ML4AudioNIPS17_paper_21.pdf) [demo](https://kkp15.github.io/)
  > GAN, G用U-Net, D用全卷积

## 参考
- [Performance measurement in blind audio source separation](https://hal.inria.fr/inria-00544230/document): Evaluation Metrics部分
- [音樂資訊檢索](http://mac.citi.sinica.edu.tw/~yang/teaching/lecture11_separation.pdf): 中央研究所的lecture slide
- [陈德成](https://www.citi.sinica.edu.tw/pages/takshingchan/index_zh.html)博士(Tak-Shing T. Chan)