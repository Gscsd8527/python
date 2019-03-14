import numpy as np

a = np.arange(10)  # 生成一个np列表 [0 1 2 3 4 5 6 7 8 9]
print(a)

b = np.array([[1, 2], [3, 4]])
print(b.ndim)  # 数组维度
print(b.shape)  # 数据的维度，n行n列，值是一个元组
print(b.size)  # 元素的总个数
print(b.dtype)  # 对象的元素类型
print(b.itemsize)  # ndarray 对象中每个元素的大小，以字节为单位
print(b.flags)  # 对象的内存信息
print(b.real)  # 元素的实部
print(b.imag)  # 元素的虚部
print(b.data)  # 	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性
print('--------------')
# c = a.reshape(4,1)
# print(c)
x = np.empty([3, 2], dtype=int)
print(x)
print('---------')
y = np.ones((5, 2))
print(y)

z = np.array([1, 2, 3, 4, 5])
print(z)
print(type(z))

print('=================')

t = np.linspace(1, 10, 20)
print(t)
print(len(t))
print(t[0])
print(t[-1])
print('------------------------')
t = np.logspace(1, 10, 20)
print(t)
print(len(t))
print(t[0])
print(t[-1])
print('------------')
# 切片
a = np.arange(10)
s = slice(2,7,2)
print(a[s])
print(a[2:7:2])

# ...表示全部，全部的行或者列
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[..., 1])   # 第2列元素  #a[行，列]
print(a[1, ...])   # 第2行元素
print(a[..., 1:])  # 第2列及剩下的所有元素