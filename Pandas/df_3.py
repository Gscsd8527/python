import pandas as pd
import numpy as np
s=np.arange(24).reshape(4,6)
print(s)
# 行标签
dates=pd.date_range('20180518',periods=6)
dates=pd.DataFrame(np.random.rand(6,4),index=dates,columns=list('ABCD'))
print(dates)
# 查看DataFrame对象的前n行
print(dates.head(3))
# 查看DataFrame对象的最后n行
print(dates.tail(2))
# 查看行数和列数
print(dates.shape)
print(dates.shape[0])
# 查看索引、数据类型和内存信息
print(dates.info())
# 查看数值型列的汇总统计
print(dates.describe())
# 根据列名，并以Series的形式返回列
print(dates['A'])
print(dates.A)
# df[[col1, col2]]：以DataFrame形式返回多列
print('df[[col1, col2]]：以DataFrame形式返回多列')
print(dates[['A','C']])
print(dates['20180518':'20180520'])
# s.loc['index_one']：按索引选取数据
print(dates.loc['20180518':'20180520'])
print(dates.loc['20180518','A'])
print(dates.loc['20180518':'20180520',['A','C']])
# s.iloc[0]：按位置选取数据
print('iloc')
print(dates.iloc[0])
# 返回第一行
print(dates.iloc[0,:])
print(dates.iloc[0:3])
print(dates.iloc[1:3,2:4])
# print(dates.iloc)

# 数据清理
# df.columns = ['a','b','c']：重命名列名
dates.columns=['T','A','N','H']
print(dates)

# pd.isnull()：检查DataFrame对象中的空值，并返回一个Boolean数组
print('--------------')
print(dates.isnull)

# pd.notnull()：检查DataFrame对象中的非空值，并返回一个Boolean数组
print(dates.notnull)

print('========================')
print(dates.sort_values(by='A'))

print(dates.groupby(by='T'))

print('-----------------')
print(dates.max())
print(dates.min)
print(dates.mean)
print(dates.count())
print(dates.std)
print(dates.median)