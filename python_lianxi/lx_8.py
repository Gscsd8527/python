# 计算器的实现+-*/
def add(*lst):
    for i in lst:
        i+=i
    print(i)
def jian(*lst):
    for i in lst:
        i-=i
    print(i)
def chen(*lst):
    for i in lst:
        i*=i
    print(i)
def chu(*lst):
    for i in lst:
        i/=i
    print(i)
while 1:
    a=int(input('请输入第一个数：'))
    b=int(input('输入第二个数：'))
    c= int(input('输入第二个数：'))
    xz=int(input("请输入选择的序号：1.'+'2.'-'3.'*'4.'/': "))
    lst=[a,b,c]
    if xz==1:
        add(*lst)
    elif xz==2:
        jian(*lst)
    elif xz==3:
        chen(*lst)
    elif xz==4:
        chu(*lst)
    else:
        print('输入错误，请重新输入！')

