import pandas as pd
import numpy as np
dates = pd.date_range('20181207', periods=6)
data = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# 查看
print('-----------查看-----------')
print(data.head(2))  # 查看开头n行数据
print(data.tail(2))  # 查看尾部n行数据
print(data.values)   # 查看值
print(data.describe())  # 查看df详细信息
print(data.T.shape)  # 转置，行变成列，列变成行
print(data.sort_index(axis=1))  # 根据列排序，默认升序
print(data.sort_index(axis=1, ascending=False))  # 根据列排序， 降序
print(data.sort_index(axis=0))  # 根据行排序，默认升序
print(data.sort_index(axis=0, ascending=False))  # 根据行排序， 降序
print(data.sort_values(by="A"))  # 根据值排序
print(data.A)  # 查看某一列  或者
print(data['A'])  # 查看某一列
print(data['2018-12-07':'2018-12-10'])  # 查看某一行
# 根据相应函数来选择
print(data.loc['2018-12-07':'2018-12-10'])  # 效率很高，不用判断值
print(data.loc[:, ['A', 'C']])  # 效率很高，不用判断值
print(data.loc['2018-12-07':'2018-12-10', ['A', 'C']])  # 效率很高，不用判断值
print(data.iloc[2:4])  # iloc只用于数字选取
print(data.iloc[2:4, 0:3])
print(data.iloc[2:4, [0, 3]])
#  根据条件值查询
print('--------根据条件值查询-------')
print(data[data.A > 0])
print(data[data > 0])

data2 = data.copy()
data2['TAG'] = ['a'] * 2 + ['b'] * 2 + ['c'] * 2  # 增加一列
print(data2)
print(data2[data2.TAG.isin(['a', 'c'])])  # 判断该a,c值是否存在的行

# 修改数据
print('----------修改数据------------')
data.iloc[1, 1] = 100  # 修改某一条数据
print(data)
data.A = range(6)  # 修改某一列
print(data)
# 或者
data.A = 100  # 修改某一列
print(data)
data.loc['2018-12-07'] = 88
print(data)
# 或者
data.iloc[1] = 99
print(data)
data.iloc[:, 2:5] = 1000
print(data)

