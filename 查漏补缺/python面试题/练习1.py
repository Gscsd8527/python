import copy
lst1=[3,4]
lst2=[1,2,lst1,5]
lst3=lst2.copy()
lst4=copy.deepcopy(lst2)
print('lst1的地址：',id(lst1),lst1)
print('lst2的地址：',id(lst2),lst2)
print('lst3的地址：',id(lst3),lst3)
print('lst4的地址：',id(lst4),lst4)
print('----------------------')
lst1.append(4)
print('lst1:',lst1)
print('lst1:',lst2)
print('lst1:',lst3)
print('lst1:',lst4)