import numpy as np

a = np.arange(32).reshape(8, 4)
print('a的值为\n', a)

# 取任意行
print('取任意行')
print(a[[1, 5], ...])
# 或者
print('或者')
print(a[[1, 5]])
print('或者')
print(a[1:5])

# 取任意列
print('取任意列')
print(a[..., [1, 3]])
print('或者')
print(a[:, 1:3])
print('或者')
print(a[..., 1:3])


print('=================')
print('取任意位置')
print(a[[4, 2, 6, 7], [0, 1, 2, 3]])  # 两个列表对应坐标
print('或者')
print(a[1:3, 2:3])  # 按范围取
print('或者')
print(a[[1, 3], 2:3])  # 按位置取
