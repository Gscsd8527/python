import pandas as pd
import numpy as np

# Series对象的性质
#  类ndarray对象
#  类dict对象
#  标签对齐操作


s = pd.Series(np.random.randn(5), index=list('ABCDE'))
print(s)
print(s.index)

s = pd.Series(np.random.randn(5))  # 也可不分配索引，自动创建数字索引
print(s)

d = {'a': 0, 'b': 1, 'd': 3}
s = pd.Series(d, index=list('abcd'))
print(s)


s = pd.Series(5, index=list('abcd'))   # 也可用标量来创建索引
print(s)

#  类ndarray对象
print('-------类ndarray对象---------')
s = pd.Series(np.random.randn(5))
print(s)
print('s[0]=\n', s[0])
print('s[:3]=\n', s[:3])
print('s[2:5]=\n', s[2:5])

print('s[2:5]=\n', s[[1, 3, 4]])

# 类字典对象
print('-----------类字典对象----------')
s = pd.Series(np.random.randn(5), index=list('abcde'))
print("s['a']=\n", s['a'])  # 取值
s['b'] = 3  # 赋值
print('赋值\n', s)
s['g'] = 100  # 增加元素
print('增加元素=\n', s)
print(s.get('f', 0))  # 查看该值，如果不在，返回0

# 标签对齐
print('----------------标签对齐------------------')
s1 = pd.Series(np.random.randn(3), index=list('ace'))
s2 = pd.Series(np.random.randn(3), index=list('ade'))
print('{0}\n\n{1}'.format(s1, s2))

print('s1 + s2=\n', s1 + s2)

# DataFrame







