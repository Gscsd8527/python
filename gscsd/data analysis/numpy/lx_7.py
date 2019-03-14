import numpy as np

# 统计函数
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(a)
print(np.amin(a))  # 最大值
print(np.amax(a))  # 最小值
print('==============')
print(np.amax(a, 1))
print(np.amax(a, 0))
print(np.amax(a, axis=0))


