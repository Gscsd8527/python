import pandas as pd
import numpy as np

data = [(1, 2.2, 'hello'), (2, 3., 'world')]
df = pd.DataFrame(data)
print(df)

# 行标签和列标签都是自动生成的，当然我们也可以指定
print('----------行标签和列标签都是自动生成的，当然我们也可以指定----------')
data = [(1, 2.2, 'hello'), (2, 3., 'world')]
df = pd.DataFrame(data, index=['a', 'b'], columns=list('ABC'))
print(df)

# 标签对齐操作
print('===========标签对齐操作===========')
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# 只会创建a和b两个数据，如果指定不存在的，则为NaN值
df = pd.DataFrame(data, index=['A', 'B'], columns=['a', 'b'])
print(df)

# 列的增加选择与删除
print('--------列的增加选择与删除--------')
df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three', 'four'])
print(df)
print('选择一列\n', df['one'])
print('或者也可以这样选择一列\n', df.one)
print('选择一行\n', df.iloc[1])

# 赋值
print('=============赋值============')
df['three'] = df['one'] + df['two']  # 第三行等于第一行和第二行相加
print(df)

# 删除
print('-----------删除-----------')
del df['three']
print(df)

# 增加
print('==========增加==========')
df['flag'] = df['one'] > 0.2
print(df)

# 直接添加一个新列
df['five'] = 5
print(df)

# 弹出
s = df.pop('five')
print(s)

# 插入 1表示为第二列
df.insert(1, 'bar', df['one'] + df['two'])
print(df)

# 插入  assign 特性，能直接使用函数
print('--------------assign 特性，能直接使用函数--------------')
print(df.assign(Ratio=lambda x: x.one - x.two))

print(df.assign(ABRatio=df.one / df.two).assign(BarValue=lambda x: x.ABRatio * x.bar))

print('----------')
print(df[3:5])



