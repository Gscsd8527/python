# 结合两个列表的元素，如果元素之间不相等的话
lst=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(lst)
# 两个for循环后面那个是嵌套在前面那个里面