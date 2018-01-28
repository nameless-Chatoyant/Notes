
├─ cfgs

├─ modules
├─ utils
├─ frame_seq_data
├─ video_data

├─ predict.py
└─ train.py



- [ ] 数据相关
    - [x] flow可视化
    - [x] 读写`.flo`文件
    - [ ] 数据集制作

- [x] ME
    - [x] 网络结构
    - [x] ForwardWarping和BackwardWarping
    - [x] Stage1

- [x] SPMC
    - [x] 网络结构

- [ ] Detail Fusion Net
    - [ ] ConvLSTM
    - [ ] 对ConvLSTM的GradientClipping
    - [ ] freeze ME, Stage2
    - [ ] joint training, Stage3

- [ ] inference
    - [ ] @split_and_stitch
    - [ ] predict_sr代码
    - [ ] test_flow代码
    - [ ] 在测试集上test
