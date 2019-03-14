a = [1, 5, 8, 9, 3, 2, 4]
list1 = []
list2 = []
for i in a:
    if i % 2 == 0:
        list2.append(i)
    elif i % 2 == 1:
        list1.append(i)
print(list1)
print(list2)
list1.sort()
list2.sort()
mylist = list1 + list2
print(mylist)