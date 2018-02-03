label是极稀疏的矩阵，
label是"Hello", 对应的token序列可能为(5, 6, 7, 7, 8), 而预测字符集的容量是10000，那么"Hello"对应的label将是5*10000的矩阵，其中只有5个元素的值为1

直接表示的话
`tf.SparseTensor`