# def mysum(x):
#     for i in range(x):
#         yield i
# for item in mysum(5):
#     print(item)
    # print('gg')

lst=[1,2,3,4,5,6]
lst_iter=iter(lst)
for i in range(0,6):
    print(next(lst_iter))
# print(next(lst_iter))

# 将一个可迭代的序列装换为迭代器：有以下两种方法：
# (1) lst.__iter__()
# (2)  iter(lst)
# 然后将这个迭代器赋值给一个新列表，然后使用
# next(新列表输出)
