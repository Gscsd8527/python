# 输出10000以内的回文数
for i in range(1,10000):
    if i<10:
        print(i,end=' ')
    if i>=10 and i<100:
        a=i//10
        b=i%10
        if a==b:
            print(i,end=' ')
    if i>=100 and i<1000:
        c=i//100
        d=i//10%10
        e=i%100%10
        if c==e:
            print(i,end=' ')
    if i>=1000 and i<10000:
        f=i//1000
        g=i//100%10
        h=i%100//10
        j=i%10
        if f==j and g==h:
            print(i,end=' ')