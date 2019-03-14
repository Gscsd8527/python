a,b=1,1
for i in range(1,100):
    a=a+b
    b=b+a
    print(a,end=' ')
    print(b,end=' ')
    if b>100:
        break