import numpy as np
# np 算法，加减乘除

# 乘法
print('乘法')
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b
print(c)


# 加法
print('加法')
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
print(a + b)
print('或者')
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
bb = np.tile(b, (4, 1))
print(a + bb)


# 除法
print('除法')
a = np.arange(20).reshape(5, 4)
b = np.array([10, 10, 10, 10])
c = a / b
print(c)
print('或者')
c = np.divide(a, b)
print(c)