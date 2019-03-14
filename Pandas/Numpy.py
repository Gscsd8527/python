from numpy import *
a=arange(24).reshape(4,6)
print(a)
# 不管行，输出2到4列
print(a[:,2:4])
# 不管列，输出2到3行
print(a[2:3,:])
# 输出1到三行与2到4列的交集
print(a[1:3,2:4])

# 精确输出
# 1表示行，2表示列索引
print(a[[1,3],[2,4]])
print(a[1,2],a[3,4])

# 布尔数组作为索引
print(a>10)
idx = a>10
print(idx)
# 或者
b=a[a>10]
print(b)

# 选取偶数元素
c = a[a%2==0]
print(c)

# 数学运算
x=arange(1,5).reshape(2,2)
y=arange(5,9).reshape(2,2)
print('x=',x)
print('y=',y)
print('x+y=',x+y)
print('x-y=',x-y)
print('x*y=',dot(x,y))
print('x/y=',x/y)

#转置矩阵
# 行变列，列变行
print(a.T)

#指定范围
d=linspace(1,10)
#指定范围，化成100等份,num=可写可不写
e = linspace(1,10,num=100)
print(d)
print(e)
