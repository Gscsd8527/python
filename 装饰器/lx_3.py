# 闭包
def funX(x):
    print('-----------开始------------')
    def funY(y):
        return x*y
    print('-----------结束-------------')
    return funY
x=funX(4)
print(x(5))
# 或下面这种都可以
# x=funX(4)(5)
# print(x)
