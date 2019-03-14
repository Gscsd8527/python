# 8、写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。
def my_fbnq():
    a,b=1,1
    lst=[a,b]
    while 1:
        a=a+b
        b=b+a
        lst.extend([a,b])
        if len(lst)==10:
            print(lst)
            return lst[-1]

my_num=my_fbnq()
print(my_num)
