作为`os`和`os.path`的替代，哪些方面推动了我们去承担新的学习成本?
(均为个人感受)

- 对遍历的好处
    使用`os.listdir('target/path')`，会得到相对于`target/path`下的路径(list)，而使用`Path('target/path').iterdir()`，一方面可以直接得到绝对路径，另一方面得到的是`generator`，性能更优
    ```
    os.listdir('target/path')
    ```

