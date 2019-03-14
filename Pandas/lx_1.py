from pandas import *
# import Pandas
# Series
# DataFrame
# Panel
# 可以做计算，也可做绘图

# Series 一维数据，创建带有索引的数据
a= Series(1,2,3)
# # 二维数据
b = DataFrame([1,2,3],[1,2,3],[1,2,3])
c = Panel([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(a)
print(b)
print(c)