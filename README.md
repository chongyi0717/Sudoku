本文发表于简书：<https://www.jianshu.com/p/966001a0769c>

也同步更新于我的知乎专栏：<https://zhuanlan.zhihu.com/p/59742512>

源代码请移步GitHub：<https://github.com/nickwu96/Sudoku>

------

过年放假在家，偶然看到老妈在玩数独（Sudoku），想着这完全可以写个程序解决数独问题呀，上网搜了一下大家的思路，发现代码最简单的还是递归算法，不过感觉递归算法有些无脑，运算量又大，想着自己能不能模拟一下人玩数独的思路，让计算机以相对聪明一点点的方式去计算数独的结果呢？

基本思路：对每一行，每一列和每一小九宫格作为一个单元进行分析，共有9*3=27个单元。对于这每一个单元来说，写一个函数need_what来计算一下1-9中还有哪几个数字没有用到，并找出没有填数字的位置坐标。对于每一个没有填数字的位置来说，用剩余的几个数字试着去填，当这个位置有且只有一个数字可以填入时，那么将数字填入此处，否则暂不处理。将对行、列、九宫格填数的过程放入while循环中，结束条件为九宫格全部完成。

部分代码截图如下：

![img](https://blog.nickwu.cn/wp-content/uploads/2019/02/image-6-1024x840.png)

运行截图如下：

![img](https://blog.nickwu.cn/wp-content/uploads/2019/02/image-8.png)

![img](https://blog.nickwu.cn/wp-content/uploads/2019/02/image-7.png)
