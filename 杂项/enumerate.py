# range可在非完备遍历中用于生成索引偏移，而非偏移处的元素
# 如果同时需要偏移索引和偏移元素，则可以使用enumerate（）函数
# 此内置函数返回一个生成器对象
Mystring='大风起兮云飞扬'
my_enum=enumerate(Mystring)
print(my_enum.__next__())
print(my_enum.__next__())
# 因为输出的是一个元组，可以尝试将其赋值
a,b=my_enum.__next__()
print(a)
print(b)