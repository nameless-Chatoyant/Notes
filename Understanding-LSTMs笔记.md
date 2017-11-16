---
title: Understanding LSTMs笔记
date: 2017-07-10 09:31:25
tags:
---

# RNN

人类在思考的过程中是依赖于记忆的，RNN在一般神经网络的基础上增加了记忆的功能。所谓“记忆”，即模型在生成输出的时候不光依赖当前输入，也依赖于先前的输入，看了[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)后可以知道，RNN的记忆是短期的，只能记住一定大小的记忆窗口。LSTM是一种增加了长期记忆功能的RNN，这体现在RNN的`step()`步骤上。

# LSTM



# 拓展资料

- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)：RNN的讲解，也以LSTM为重
- [Hochreiter (1991) \[German\]](http://people.idsia.ch/~juergen/SeppHochreiter1991ThesisAdvisorSchmidhuber.pdf)：
- [Bengio, et al. (1994)](http://www-dsi.ing.unifi.it/~paolo/ps/tnn-94-gradient.pdf)
- [Hochreiter & Schmidhuber (1997)](http://deeplearning.cs.cmu.edu/pdfs/Hochreiter97_lstm.pdf)
- [Cho, et al. (2014)](http://arxiv.org/pdf/1406.1078v3.pdf)
- [Yao, et al. (2015)](http://arxiv.org/pdf/1508.03790v2.pdf)
- [Gers & Schmidhuber (2000)](ftp://ftp.idsia.ch/pub/juergen/TimeCount-IJCNN2000.pdf)：LSTM变体，peephole connections
- [Koutnik, et al. (2014)](http://arxiv.org/pdf/1402.3511v1.pdf)：Clockwork RNNs