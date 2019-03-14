def test(list1,list2):
    if len(list1) == 0:
        return None
    root_note = list1[0]
    root_index = list2.index(root_note)
    left = test(list1[1:root_index+1],list2[:root_index])
    right = test(list1[1+root_index:],list2[root_index+1:])
    return (root_note,left,right)
list_a = [1, 2, 4, 7, 3, 5, 6, 8]
list_b = [4, 7, 2, 1, 5, 3, 8, 6]
Root = test(list_a,list_b)
print(Root[0])
