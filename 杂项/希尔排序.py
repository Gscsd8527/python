lst=[7,2,3,8,11,22,5,1]
length=len(lst)
inc=0
while inc<=length/3:
    inc=inc*3+1
while inc>=1:
    for i in range(inc,length):
        tmp=lst[i]
        for j in range(i,0,-inc):
            if tmp<=lst[j-inc]:
                lst[j]=lst[j-inc]
            else:
                j+=inc
                break
        lst[j-inc]=tmp
    inc//=3
print(lst)