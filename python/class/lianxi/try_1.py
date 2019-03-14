#请用户输入除数被除数，然后计算相处的结果
try:
    num1=int(input('输入被除数：'))
except ValueError:
    print('输入的类型错误')
try:
    num2=int(input('输入除数：'))
except ValueError:
    print('输入的类型错误')
try:
    n=num1/num2
    print(n)
except ZeroDivisionError:
    print('除数不能为0')
