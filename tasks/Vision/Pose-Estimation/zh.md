2D Pose
Human Pose Estimation指定位解剖学中的关键点(keypoints)或部位(parts)

面临的挑战
- 一张图中包含的人数是不确定的，他们的位置/大小也是不确定的
- 人与人之间互动会使得空间关系异常复杂，比如很多连人类也会第一眼看错的图，这种看错，可以是把不同人的parts归为了同一个人
- 计算上的复杂性，使得实时性不能保证（比如先目标检测分离出每个人，再做Pose Estimation，计算复杂度就与图像中Human的个数线性相关，肯定是做不到实时了）

## Top-down
先分离出individuals，再对每个individual找keypoints/parts
人形检测 + 单人pose estimation
- early commitment: 如果人挨得很近甚至在图像里重叠，目标检测很容易把两个人划在一个bounding box里，然后就没的补救了。
- 计算上的复杂性，人形个数直接影响到性能，处理大场景是肯定不适用的。
## Bottom-Up
先找keypoints/parts, 再把它们关联到individuals上
# Datasets
## 建立统一dataset的方案
使用COCO, MPII 建立一个统一的dataset, 要点
- COCO有19种keypoints, MPII有16种, 且顺序不一样
- COCO是不完整标注, 需要binary mask, 区分有标注和无标注
- 
## COCO
共有19种parts
OpenPose中的映射
```cpp
const std::map<unsigned int, std::string> POSE_COCO_BODY_PARTS {
        {0,  "Nose"},
        {1,  "Neck"},
        {2,  "RShoulder"},
        {3,  "RElbow"},
        {4,  "RWrist"},
        {5,  "LShoulder"},
        {6,  "LElbow"},
        {7,  "LWrist"},
        {8,  "RHip"},
        {9,  "RKnee"},
        {10, "RAnkle"},
        {11, "LHip"},
        {12, "LKnee"},
        {13, "LAnkle"},
        {14, "REye"},
        {15, "LEye"},
        {16, "REar"},
        {17, "LEar"},
        {18, "Background"}
};
```
pose_map_index
```cpp
std::vector<unsigned int>{
    31,32, 39,40, 33,34, 35,36, 41,42, 43,44, 19,20, 21,22, 23,24, 25,26, 27,28, 29,30, 47,48, 49,50, 53,54, 51,52, 55,56, 37,38, 45,46
}
```


## MPII
共有16种parts
OpenPose中的映射
```cpp
const std::map<unsigned int, std::string> POSE_MPI_BODY_PARTS {
    {0,  "Head"},
    {1,  "Neck"},
    {2,  "RShoulder"},
    {3,  "RElbow"},
    {4,  "RWrist"},
    {5,  "LShoulder"},
    {6,  "LElbow"},
    {7,  "LWrist"},
    {8,  "RHip"},
    {9,  "RKnee"},
    {10, "RAnkle"},
    {11, "LHip"},
    {12, "LKnee"},
    {13, "LAnkle"},
    {14, "Chest"},
    {15, "Background"}
};
```
pose_map_index
```cpp
std::vector<unsigned int>{
    16,17, 18,19, 20,21, 22,23, 24,25, 26,27, 28,29, 30,31, 32,33, 34,35, 36,37, 38,39, 40,41, 42,43
}
```

# 论文整理
- CVPR 2017 | Zhe Cao *et al.* **"Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields"** [arXiv](https://arxiv.org/abs/1611.08050) [Repo](https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation)
