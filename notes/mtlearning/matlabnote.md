<!-- 这是我的Matlab学习笔记 -->

1.format affects only thd display of numbers,not the way Matlab computes or saves them.

2.".*"是对应元素相乘，".^"是矩阵自乘几次。*"是矩阵相乘，使用逗号可以水平连接矩阵，分号垂直连接。

3.magic(n),生成n阶幻方矩阵。幻方矩阵：它的行、列、对角线之和相同。
magic(4)

ans =

    16     2     3    13
     5    11    10     8
     9     7     6    12
     4    14    15     1
ans(8) = 14或者 ans(4,2) = 14	矩阵是按列存储。可以类似R语言取出矩阵中的元素，不过逗号,后面要跟一个冒号: