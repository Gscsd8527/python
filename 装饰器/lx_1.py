# 什么是柯里化
# 指的是将原来接受两个参数的函数变成新的接受一个参数的函数的过程
# 新的函数返回一个以原有第二个参数为参数的函数
def add(x,y):
    return x+y
print(add(4,5))
def new_add(x):
    def inner(y):
        return x+y
    # 返回的是inner函数的引用
    return inner
foo=new_add(4)(5)
print(foo)