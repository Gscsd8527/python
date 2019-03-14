#输入三个整数x,y,z，请把这三个数由小到大输出。
a=int(input('输入第一个整数：'))
b=int(input('输入第二个整数：'))
c=int(input('输入第三个整数：'))
if a>=b:
    if a>=c:
        if b>=c:
            print('三个数由小到大输出:',a,b,c)
        else:
            print('三个数由小到大输出:', a, c, b)
    else:
        print('三个数由小到大输出:', c, a, b)
else:
    if a>=c:
        print('三个数由小到大输出:', b, a, c)
    else:
        if b>=c:
            print('三个数由小到大输出:', b,c,a)
        else:
            print('三个数由小到大输出:', c,b,a)