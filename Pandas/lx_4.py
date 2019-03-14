from numpy import *
a= array([1,3,4,8])
print(a.reshape(2,2))
print('--------------')
print(a.reshape(1,4))
b=a.reshape(2,2)
print(b[1][1])
b[1][1]=100
print(b)