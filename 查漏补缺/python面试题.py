import copy
a=[1,2,3]
b=[1,a,4]
print(a)
print(b)
print(id(a))
print(id(b))
print(id(b[1]))
# a.append(7)
# print(a)
print(b[1])
print('----------')
c=copy.deepcopy(b)
print(id(c))
print(c[1])
print(id(c[1]))
a.append(7)
print(b[1])
print(c[1])
print(id(a))
print(id(b[1]))
print(id(c[1]))

