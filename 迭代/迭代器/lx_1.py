# 生成器创建方式1
it=(i for i in range(100) if i%2==0)
print(it)#这是一个迭代器
# for t in it:
#     print(t)
print(type(it))
# 一步步读取迭代器里面的数据
print(next(it))