---
title: OCR-2-test
date: 2017-07-21 14:57:21
tags:
---

以下图作为输入
<img src="http://imglf.nosdn.127.net/img/elBJbXQxRXFVUVEybTRiakhuMFJERDhnM2pocUpSYUhPVWFad21oMFdDYUZNOHJMdjlOOW53PT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg" width="300"/>
最终的预测图使用连通域的方法，对所有连通域作最小外接矩形
<table>
<tr><th>mask图</th><th>结果</th>
</tr>
<tr>
	<td>
	<img src="http://imglf0.nosdn.127.net/img/elBJbXQxRXFVUVEybTRiakhuMFJETzYyMTVZVFhsV2E5YzJqY1pYVDJCQVlreWZ1SW9IY0h3PT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg" width="300"/>
	</td>
	<td>
	<img src="http://imglf.nosdn.127.net/img/elBJbXQxRXFVUVEybTRiakhuMFJER3FOTnhXRzROWWtYVDBRdWFLdXBGcEt6S2FNTnplZGxBPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg" width="300"/>
	</td>
	</tr>
</table>

可见噪声非常严重，既然是连通域的方法，这里使用膨胀(Dilation)与腐蚀(Erosion)对mask图(输入需是二值化的图)进行操作。


<table>
<tr><th>mask图</th><th>结果</th>
</tr>
<tr>
	<td>
	<img src="http://imglf.nosdn.127.net/img/elBJbXQxRXFVUVEybTRiakhuMFJEQmtsck54ZERrUTlaWUUvTjhqeXpIZFpNY0I3by90OUJRPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg" width="300"/>
	</td>
	<td>
	<img src="http://imglf0.nosdn.127.net/img/elBJbXQxRXFVUVEybTRiakhuMFJEQ0htSjlWUHpZUDRIa24yZFVINzQ1SURxUkI2V3c1ZGlnPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg" width="300"/>
	</td>
	</tr>
</table>
膨胀操作后，连通域面积缩小，原本无用的小块标注缩没了，对减小噪声起到了一定作用。

<table>
<tr><th>mask图</th><th>结果</th>
</tr>
<tr>
	<td>
	<img src="http://imglf2.nosdn.127.net/img/elBJbXQxRXFVUVEybTRiakhuMFJES2VnMDAxK0lROFF3S0UrOTRvMnVmRlErRUdzckhEaU5BPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg" width="300"/>
	</td>
	<td>
	<img src="http://imglf2.nosdn.127.net/img/elBJbXQxRXFVUVEybTRiakhuMFJETHllSmxrWC83ZGJkL2RmWkhUYWdNNGVhL1VubHFnT2lnPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg" width="300"/>
	</td>
	</tr>
</table>
腐蚀操作后，连通域面积扩大，原本因极小间隙导致同一行产生的多个连通域现在连在了一起，同样减小了噪声。

在未进行膨胀／腐蚀操作前，原结果图已经表现出的缺点。腐蚀操作降低了粒度，

还记得之前而导致的边缘不标注问题么？这个历史遗留问题在这里却起到了很关键的作用。首先这个问题在腐蚀操作后已经被解决了，而在膨胀操作后，原先的藕断丝连完全地被分割成了多个小区域。这样一来，通过结合腐蚀与膨胀的结果，我们就在单行内有了每m个像素为一片段的细粒度。通过对这些片段作变换，来解决这个问题。也是这部分工作的重头戏。

# 结合两种粒度的结果
首先通过粗粒度图定位，得到了该区域轮廓信息。
用什么办法来找到这片区域里的细粒度区域呢？从定义来说，两种粒度的共同点就是覆盖区域了。求得

拆分得到多个小区域。


将参差不齐的矩形在高度上作padding，得到最后结果。