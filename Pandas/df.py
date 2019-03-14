import pandas as pd
import numpy as np
# 创建一个日期
dates = pd.date_range('20180515',periods=6)
print(dates)
#index代表行标签，columns代表列标签
# randn表示生成6行4列的数据（随机数）
dates = pd.DataFrame(np.random.randn(6, 4),index=dates,columns=list('ABCD'))
print(dates)

# 查询
# head默认返回前五行
print(dates.head())
# 返回前两行
print(dates.head(2))
# 默认返回最后五行的数据
print(dates.tail())
# 返回最后两行的数据
print(dates.tail(2))
# 返回行标签
print('返回行标签')
print(dates.index)
#返回列标签
print(dates.columns)
#返回dates中的值
print(dates.values)
# 查看基本数据整体情况
# count：表示有几个有效的数据
# mean：平均值
# std:方差
# min:这一列的最小值
# 25%：四分位
# 50%：二分位
# 75%：三分位
# max:这一列的最大值
print(dates.describe())

print('-'*50)
#按照行标签进行排序
print('按照行标签进行排序')
# 根据列标签排序，还是ABCD
print(dates.sort_index(axis=1))
# 列标签降序
print(dates.sort_index(axis=1,ascending=False))

#按照行标签排序，降序
print(dates.sort_index(axis=0,ascending=False))

print('通过值的列标签进行排序')
# 通过值的列标签进行排序
# 通过A列进行排序，默认升序
print(dates.sort_index(by='A'))
#查看某列
print(dates['A'])
# 也可
print(dates.A)
# 也可查看指定行
print(dates[2:4])
print('也可通过行标签选择')
# 也可通过行标签选择
print(dates['20180516':'20180518'])
#loc效率比上面这个要高，因为loc不需要判断标签是位置的参数还是索引标签参数
# 不能dates.loc[2,4]
print(dates.loc['20180516':'20180518'])
# 通过数字索引
print(dates.iloc[2:4])
# 获取某列数据
print(dates.loc[:,['B','C']])

# 获取某个区间内的数据
#获取20180516到20180518日期之间的A和B的数据
print(dates.loc['20180516':'20180518',['A','B']])

#访问到特定的值
print(dates.loc['20180516','A'])

#这种方法比上面那种快，但这种访问的是原生数据结构
print(dates.at[pd.Timestamp('20180516'),'B'])

# 内置方式访问数据
print(dates.iloc[1])
print(dates.iloc[1:3])
# 也可选择指定的列
print(dates.iloc[:,1:3])
# 获取指定的数据
print(dates.iloc[1,1])
print(dates.iat[1,1])

print('判断')
print(dates[dates.A>0])
print(dates[dates>0])

ta= dates.copy()
tag=['a']*2+['b']*2+['c']*2
print(tag)
ta['TAG']=tag
print(ta)

# 过滤数据
print(ta[ta.TAG.isin(['a','b'])])

# 修改数据
dates.A=range(6)
print(dates)
# 也可用标量改
dates.B=200
print(dates)