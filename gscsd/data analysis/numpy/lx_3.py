import numpy as np


# 花式索引
x = np.arange(32).reshape((8, 4))
print(x)
print()
print(x[[4, 2, 1, 7]])  # 取行

print('============')
#  倒序索引数组
x=np.arange(32).reshape((8,4))
print(x[[-4,-2,-1,-7]])

#传入多个索引数组（要使用np.ix_）
x=np.arange(32).reshape((8,4))
print(x[np.ix_([1,5,7,2],[0,3,1,2])])   #  组合坐标，第一个列表中的第一个元素和第二个列表中所有元素组合