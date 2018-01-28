
SGD -> SGDM -> NAG ->AdaGrad -> AdaDelta -> Adam -> Nadam

SGD

SGDM: SGD with Momentum

NAG: SGD with Nesterov Acceleration

AdaGrad

AdaDelta

Adam

Nadam

# 附录
## 论文整理
- Nitish Shirish Keskar *et al.* **"Improving Generalization Performance by Switching from Adam to SGD"** []()
    > 提出公式把前人有在用的Adam转SGD的训练方法傻瓜化
- ICLR 2018 | **"On the Convergence of Adam and Beyond"** []()
- **"The Marginal Value of Adaptive Gradient Methods in Machine Learning"**

# Adam
- Anonymous authors **"On the Convergence of Adam and Beyond"** [pdf](https://openreview.net/pdf?id=ryQu7f-RZ)
    > 证明Adam即使在一个convex problem上也会不收敛，并给出改进算法
- Ashia C. Wilson *et al.* **"The Marginal Value of Adaptive Gradient Methods in Machine Learning"** [arXiv](https://arxiv.org/abs/1705.08292)
    > 指出像Adam这样的自适应算法，和SGD相比，虽然训练误差可能更低，但测试误差却更高



min_\theta()
SGD
梯度下降:
\theta_{t+1} = \theta_t - \alpha f


Momentum: 给梯度加惯性
\theta_{t+1} = \theta_t - \alpha * g


