# 列表中数值出现次数
mylist = ['a', 'a', 'b', 'b', 'c', 'e', '+']
test = []
mydict = {}
for i in mylist:
    if i not in test:
        test.append(i)
        index = mylist.count(i)
        mydict[i] = index
print(mydict)
