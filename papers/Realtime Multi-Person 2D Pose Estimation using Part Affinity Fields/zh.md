
The mask is used to avoid penalizing the true positive predictions during training.



# Pipeline

## 0. Data Preparing

## 1. Simultaneous Detection and Association
同时做检测(detection)和关联(association), 
模型应接手一张图片(h × w)作为输入，输出:
- Part Confidence Maps: h × w × num_parts, 表示
- Part Affinity Fields: h × w × 2num_parts
## 2. Confidence Maps for Part Detection
需要从2D的keypoints标注中生成groundtruth confidence maps, 每一个onfidence map是一个2D表示

测试时，预测出confidence map后通过NMS得到part candidates

## 3. Part Affinity Fields for Part Association
通过Detection得到了一堆parts, 接下来要将通过PAF把这些parts整合成人
PAF是一个二维的向量场（每个limb都会有一个二维的向量场，从一个点指向另一part

## 4. Multi-Person Parsing using PAFs
使用NMS(Non-Maximum Suppression, 非极大值抑制)来获取互不相关的集合。
对每一个part, 都可能有多个candidates, 表示part属于哪一个人或者是false positive
这种 candidates 导致了很大的集合


# Data Preparing
讲完了模型的原理，开始工程上的细节。模型需要groundtruth confidence maps和groundtruth part affinity vector field

$$L^*_{c,k} = $$
即，key

图(graph), 图中点(node)代表part candidates, 边(edge)代表着part candidates之间可能的联系, 边是带有权重的, 通过求积分可以得出。

如此一来, 判断parts分别属于谁的问题, 就抽象成了带权二分图的最大匹配问题. 我们需要找到完全图的子图, 满足
- 不能有两条边共享同一个结点
- 所有边的权的和最大.
> If we consider a single pair of parts j1 and j2 (e.g., neck and right hip) for the c-th limb, finding the optimal associ- ation reduces to a maximum weight bipartite graph match- ing problem.

论文使用的算法是Hungarian algorithm. 这部分算法放到独立的章节去讲
