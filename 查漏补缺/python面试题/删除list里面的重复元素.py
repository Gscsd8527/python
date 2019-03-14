lst=[1,1,2,2,3,3,4,4,5,5,6,6]
# 方法1：
# lst2=[]
# for i in lst:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)

# 方法2：
# 这种if else方法有个大bug，我们第一次取到i=1时，计数到1有两个，那么它会删除掉前面那个，而这时候i就应该会取后面那个1，
# 但实际却不是如此，因为lst删掉一个后，for i in lst 里面的lst重新刷新了，其结果是[1,2,2,3,3,4,4,5,5,6,6]了，这时候i的值为2了
lst2=[]
for i in lst:
    if lst.count(i)>1:
        lst.remove(i)
    # else:
    #     print('i:',i)
    #     lst2.append(i)
print(lst)
