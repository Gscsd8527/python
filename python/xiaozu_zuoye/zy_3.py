#输入三个整数x,y,z，请把这三个数由小到大输出。
import  math
def MAX(a,b):
    if a>=b:
        return a
    else:
        return b

a=int(input('输入第一个整数：'))
b=int(input('输入第二个整数：'))
c=int(input('输入第三个整数：'))
print('max is :',MAX(a,MAX(b,c)))