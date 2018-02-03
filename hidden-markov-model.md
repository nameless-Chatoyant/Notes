理解HMM: [如何用简单易懂的例子解释隐马尔可夫模型？ - 王蒟蒻的回答 - 知乎](https://www.zhihu.com/question/20962240/answer/33614574)

三大基本问题
1. 对于一个观察序列匹配最可能的系统——评估，使用前向算法（forward algorithm）解决；
2. 对于已生成的一个观察序列，确定最可能的隐藏状态序列——解码，使用维特比算法（Viterbi algorithm）解决；
3. 对于已生成的观察序列，决定最可能的模型参数——学习，使用前向-后向算法（forward-backward algorithm）解决。

# 应用

- Evaluation
- Decoding
词性标注
- Learning