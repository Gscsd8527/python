# Python 列表综合练习
# 使用 python 语言创建空列表 score，按学号顺序（由小到大）保存多个学生
# 一门课程的考试成绩。调用列表操作的常用函数实现以下功能：
# 1）创建一个空列表 score；
score=[]
# 2）调用 append()函数在 score 列表中依次追加 10 个数值 （68,87,92,100,76,88,54,89,76,61）；
for i in [68,87,92,100,76,88,54,89,76,61]:
    score.append(i)
print(score)
# 3）输出 score 列表中第 3 个元素的数值；
print(score[2])
# 4）输出 score 列表中第 1~6 个元素的值；
print(score[0:6])
# 5）调用 insert()函数，在 score 列表第 3 个元素之前添加数值 59；
score.insert(2,59)
print(score)
# 6）利用变量 num 保存数值 76,调用 count()函数，查询 num 变量值在 score 列表 中出现的次数；
num=76
print(score.count(num))
# 7）使用 in 查询 score 列表中是否有 num 变量值的考试成绩；
if num in score:
    print('存在')
else:
    print('不存在')
# 8）调用 index()函数，查询 score 列表中成绩是满分的学生学号；
print(score.index(100))
# 9）score 列表中将 59 分加 1 分；
a=score.index(59)
score[a]+=1
print(a,score)
# 10）调用 del()函数删除 score 列表中第 1 个元素；
del score[0]
print(score)
# 11）调用 len()函数获得 score 列表中元素的个数；
b=len(score)
print(b)
# 12）调用 sort()函数，对列表中所有元素进行排序，输出考试的最高分和最低分；
score.sort()
print('最高分：{0}，最低分：{1}'.format(score[-1],score[0]))
# 13）调用 reverse()函数，颠倒 score 列表中元素的顺序；
score.reverse()
print(score)
# 14）调用 pop()函数删除 score 列表中尾部的元素，返回删除的元素；
c=score.pop()
print(c)
# 15）score 列表中追加数值 88，并输出。调用 remove()函数删除 score 列表中第一个数值 88；
score.append(88)
score.remove(88)
print(score)
# 16）创建 2 个列表 score1 和 score2，score1 中包含数值 2 个元素值：80,61，score2中包含 3 个元素值：71,95，82，合并这两个列表，并输出全部元素；
score1=[80,61]
score2=[71,95,82]
score1.extend(score2)
print(score1)
# 17）创建 score1 列表，其中包含数值 2 个元素值：80,61，将 score1 中元素复制5 遍保存在 score2 列表中，输出 score2 列表中全部元素。
score1=[80,61]
score2=score1*5
print(score2)