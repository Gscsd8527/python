import numpy as np
# 转换数据的顺序
a = np.arange(30).reshape(5, 6)
print('a的值为\n', a)
print('转置后的a的值为\n', a.T)


print(a[..., ::-1])
print('=============')
print(a[::-1, ::-1])
