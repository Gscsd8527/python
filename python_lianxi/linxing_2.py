# 求100内的质数
for i in range(2,100):
    tag = True
    for j in range(2,i):
        if i%j==0:
            tag=False
            break
    if tag==True:
        print(i,end='\t')
    print(type(tag))