# 5.请定义一个函数 ’quadratic(a,b,c)‘，接收三个参数，返回一元二次方程:
# ax² + bx + c = 0 的两个解。（提示：计算平方根可以调用math.sqrt()函数）
import math
def quadratic(a,b,c):
    x=b**2-4*a*c
    x1=(-b+math.sqrt(x))/(2*a)
    x2=(-b-math.sqrt(x))/(2*a)
    print('x1的值为：%0.2f'%x1)
    print('x2的值为：%0.2f'%x2)
quadratic(2,5,3)
