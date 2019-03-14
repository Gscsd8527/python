# 求m中3,6,9组成的列表
m=[[1,2,3],[4,5,6],[7,8,9]]
numlist=[x[2] for x in m ]
# 或者
# [m[row][2] for row in (0,1,2)]
print(numlist)
