
# 安装
## 安装依赖项
### boost
```bash
sudo apt-get install libboost-dev
```
### BZip2
```bash
sudo apt-get install libbz2-dev
```
### Eigen3
```bash
export EIGEN3_ROOT=$path/to/eigen
wget -o - https://bitbucket.org/eigen/eigen/get/3.2.8.tar.bz2 |tar xj
```

```bash
~/.bashrc中添加
export PYTHONPATH=$PYTHONPATH:`readlink -f /path/to/your/module`
```