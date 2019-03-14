# 求m,n矩阵和元素的乘积
m=[[1,2,3],[4,5,6],[7,8,9]]
n=[[2,2,2],[3,3,3],[4,4,4]]
t=[(m[x][y]*n[x][y]) for x in range(len(m)) for y in range(len(n))]
print(t)
# for x in (len(for y in m)):