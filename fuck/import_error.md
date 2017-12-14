# 路径不对
当前路径下有同名的文件夹，典型例子是：
1. 运行`python3 setup.py install`，会在当前目录中建
2. 运行`python3`进入交互式运行环境，路径为当前目录
3. 尝试`import module_name`，会尝试从当前目录的与模块同名文件夹导入这个库