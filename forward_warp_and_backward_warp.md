# Forward Warp
以最简单的warp举例，下移0.5个像素，右移0.5个像素
```python
for y_src in range(H_src):
    for x_src in range(W_src):
        y_dst, x_dst = mapping(y_src, x_src)
        dst(y_dst, x_dst) = src(y_src, x_src)
```
根据算法，遍历$I_{src}$(图中黑点)，可见第一个像素并不在网格上(非整数坐标)，需要把这个像素的值分摊到它周围的四个整数坐标
# Backward Warp
```python
for y_dst in range(H_dst):
    for x_dst in range(W_dst):
        y_src, x_src = transposed_mapping(y_dst, x_dst)
        dst(y_dst, x_dst) = src(y_src, x_src)
```
根据算法，遍历$I_{dst}$(图中白点)，可见对于像素(1,1)，它的值受原图中(1)四个像素影响，需要把这四个像素的值综合起来赋给这个点
mapping中位于($y_{src}$, $x_{src}$)的像素将移动到($y_{dst}$, $x_{dst}$)位置

# Code
支持`numpy.ndarray`, `torch.autograd.Variable`, `tf.placeholder`, `tf.`
