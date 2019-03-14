# 请尽量用简洁的方法二维数组转换成一维数组
li=[[1,2],[3,4],[5,6]]
print([j for i in li for j in i] )

t=[]
[t.extend(i) for i in li]
print (t)