# 大小驼峰
mystr = 'ab-cd-ef-gh'
mylist = mystr.split('-')
print(mylist)
mylist1 = []
mylist1.append(mylist[0])
for i in mylist[1:]:
    first_upper = i.title()
    mylist1.append(first_upper)
print(mylist1)
end_str = ''.join(mylist1)
print(end_str)
