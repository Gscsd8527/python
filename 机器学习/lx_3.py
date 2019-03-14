from numpy import *
a=arange(12).reshape(3,4)
print(a)
print(type(a))
print(a.ndim)
print(a.T) #矩阵转置，原来的行变成列，原来的列变成行
# 未转置之前的行列
print(a.shape)
print(a.shape[0])