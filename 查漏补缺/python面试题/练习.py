import copy
lst1=[1,2,3,4,5]
lst2=lst1.copy()
lst3=lst1
lst4=copy.deepcopy(lst1)
lst1.append(6)
print('lst1的地址：',id(lst1),lst1)
print('lst2的地址：',id(lst2),lst2)
print('lst3的地址：',id(lst3),lst3)
print('lst4的地址：',id(lst4),lst4)