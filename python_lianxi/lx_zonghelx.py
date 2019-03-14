# 使用 python 语言创建空元组 score，按学号顺序（由小到大）保存多个学生一门课程的考试成绩。调用元组操作的常用函数实现以下功能：
#
# 1）创建 score 元组，其中包含 10 个数值（68,87,92,100,76,88,54,89,76,61）；
score=(68,87,92,100,76,88,54,89,76,61)
#
# 2）输出 score 元组中第 3 个元素的数值；
print(score[2])
# 3）输出 score 元组中第 1~6 个元素的值；
print(score[0:6])
# 4）调用 count()函数，查询数值 76 在 score 元组中出现的次数；
print(score.count(76))
# 5）调用 index()函数，查询 score 元组中成绩是满分的学生学号；
print(score.index(100))
# 6）调用 len()函数获得 score 元组中元素的个数；
print(len(score))
# 7）调用 list()函数将 score 元组转换为 lstScore 列表；
lstScore=list(score)
print(lstScore)
# 8）调用 tuple()函数将 lstScore 列表转换为 tpScore 元组；
tpScore=tuple(lstScore)
print(tpScore)
# 9）创建 2 个元组 score1 和 score2，score1 中包含数值 2 个元素值：80,61，score2 中包含 3
# 个元素值：71,95，82，合并这两个元组，并输出。
score1=(80,61)
score2=(71,95,82)
sum_tp=score1+score2
print(sum_tp)