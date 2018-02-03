# 从标准库中学习优雅的设计模式

- 创建文件夹
    ```python
    from pathlib import Path
    p = Path()
    p.mkdir()
    # 如果不存在，会出FileNotFoundError: [Errno 2] No such file or directory
    p.mkdir(parents = True) # 如果父文件夹不存在，创建它
    ```
