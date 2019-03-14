from numpy import *

# 矩阵相乘
# 1分别乘以1,0,3，得到的值相加
# 0分别乘以0,5,0，得到的值相加
a=array([[1,0,3],[2,0,4]])
b=array([[1,0],[0,5],[3,0]])
print(a)
print(b)

print('>>>>>>>>>>>>>>>')
# a乘以b
print(dot(a,b))