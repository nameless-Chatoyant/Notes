`cv2.VideoCapture(video_path)`创建实例
调用这个实例的`read()`方法
1. 从硬盘上的视频文件读取帧(I/O)
2. 解码帧并返回(计算)
瓶颈
`read()`是一个阻塞操作