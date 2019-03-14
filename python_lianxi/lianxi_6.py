# 将 str='1,1,10'转换（1,1,10）元组
str='1,1,10'
lst=str.replace(',',' ')
tp=lst.split(' ')
tep=tuple(tp)
print(tep)

# lst=str.split(',')
# print(lst)
# tp=tuple(lst)
# print(tp)
# tup=tuple(lst)
# print(tup)