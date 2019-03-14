# 用Python语言写一个函数，输入一个字符串，返回倒序排列的结果：
# 如：string_reverse('abcdefg')，返回'gfedcba'
def test(mystr):
    lst=[]
    for i in mystr:
        lst.insert(0,i)
    mystr=''.join(lst)
    return mystr
tan=test('tanzhenhua')
print(tan)
