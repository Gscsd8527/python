n=int(input("请输入要输出的行数："))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=' ')
    for k in range(1,1+i):
        print("*",end=' ')
    print()