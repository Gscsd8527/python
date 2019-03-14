# import numpy as np
from numpy import *

# 核心类ndarray
a = ndarray((3,2))
print(a)
print(type(a))
# 进行reshape转换
b=a.reshape(6,1)
print(b)
print(b.ndim) #数轴的个数，即几维
print(b.size)  #数组元素的总个数
print(b.dtype)  #元素数据类型，64位浮点数
print(b.itemsize)  #元素大小

x=[(1,4,7),(2,5,8),(3,6,9)]
a=array(x)
print(a)