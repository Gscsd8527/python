a = ['tan', 'zhen', 'hua']
# a.sort()
# print(a)
# ['hua', 'tan', 'zhen']

a.sort(key=lambda x: x[2])
print(a)
a.reverse()
