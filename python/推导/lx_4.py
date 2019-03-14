# 求m中斜线1,5,9组成的列表
# m=[[1,2,3],[4,5,6],[7,8,9]]
# x=[m[x][x] for x in range(len(m))]
# print(x)

# for i in m:
a=[1,2,3,4,5,6]
# lst=[sum(x+3) for x in a[::2]]
# print(lst)
sun=sum(map(lambda x:x+3,a[::2]))
print(sun)

