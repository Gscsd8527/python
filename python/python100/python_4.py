# 以下实例为通过用户输入三角形三边长度，并计算三角形的面积：
import math
num1=int(input('请输入第一条边：'))
num2=int(input('请输入第二条边：'))
num3=int(input('请输入第三条边：'))
while 1:
    if num3>num1+num2:
        print('第三条边不正确，请重新输入：')
        num3=int(input('请输入第三条边：'))
    else:
        break
# 用海伦公式算，求出半周长
s=(num1+num2+num3)/2
area=(s*(s-num1)*(s-num2)*(s-num3))**0.5
print('该三角形面积为：%0.2f'%area)
