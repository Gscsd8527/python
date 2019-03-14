a = [1, 2, 3]
b = [1, 2, 3]
b = a
print(id(a))
print(id(b))
b.append(4)
print(id(a))
print(id(b))
