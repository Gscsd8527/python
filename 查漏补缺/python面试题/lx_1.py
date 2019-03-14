a='aAsmr3idd4bgs7Dlsf9eAF'
# 1 请将a字符串的大写改为小写，小写改为大写。
print(a.swapcase())
# 2 请将a字符串的数字取出，并输出成一个新的字符串。
b=a
lst=[]
for i in a:
    if i.isdigit():
        lst.append(i)
b=''.join(lst)
# print(b)
# 3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母）
# ，并输出成一个字典。 例 {'a':4,'b':2}
dit={}
for i in a:
    if i not in dit.keys():
        dit[i]=a.count(i)
print(dit)
# 4 请去除a字符串多次出现的字母，仅留最先出现的一个。
# 例 'abcabb'，经过去除后，输出 'abc'
c=a
c=list(c)
c.reverse()
for i in c:
    if c.count(i)>1:
        c.remove(i)
c.reverse()
d=''.join(c)
print(d)
# 5 请将a字符串反转并输出。例：'abc'的反转是'cba'
e=list(a)
print(e)
e.reverse()
e=''.join(e)
print(e)
# 6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），
# 并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
f=list(a)
for i in f:
    if i.isdigit():
        f.remove(i)
f.sort()
f=''.join(f)
print(f)
# 7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。
# 如果出现，则输出True，否则，则输 出False
boy='boy'
for i in boy:
    if i not in a:
        print('Flase')
        break
    else:
        print('True')
        break
# 8 要求如1.7，此时的单词判断，由'boy'改为四个，
# 分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，
# 是否都出现在a字符串里。
g=['boy','girl','bird','dirty']
def test(mystr):
    for i in mystr:
        if i not in a:
            print('Flase')
            break
        else:
            print('True')
            break
for i in g:
    test(i)

