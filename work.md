- `cost = loss_sr`，可以
- 

- 只做freeze ME，训练DF Net，可以
```python
flow_i0 = tf.stop_gradient(flow_i0)
cost = loss_sr
```

# Troubeshooting
## 第二阶段，模型输出偏亮
## 第三阶段(jointly tuning)，预测的flow和SR output都直接飞了
It's mentioned in paper 
> Training the whole system in an end-to-end fashion with random initialization would result in zero flow in motion estimation, making the final results similar to those of single-image SR.

再波动也不应该第一个epoch就跑飞。

**可能是`loss_me`和`loss_sr`的数量级的原因**
In practice,
论文中提到，直接训练整个网络会让ME输出zero flow，让模型性能退化成Single-Image SR
而实际测试，不管是load第二阶段训练好的模型，还是直接train，都会让预测出的flow接近最大值，进而导致warp后的图像基本全是自动fill的黑色，最终导致SR是一张雪花图


k