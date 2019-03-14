def funX(x):
    def funY(y):
        return x*y
    return funY
x=funX(3)
print(x(4))
# 以下方法也可以
# result=funX(3,4)
# print(result)