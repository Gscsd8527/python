# str1 = " w_e_r_tD84 "
# str2 = " w_e_r_t84D 78d"
# 以下题目都要求打印最后的结果:
# 1.比较这两个字符串是否相同，如果相同，打印“true”，如果不相同，打印“false”
# 2.找出这两个字符串从第几个位置开始不相等的,打印不相等的部分
# 3.把str2小写字母都改成大写

# 4.去掉str2两边的空格。PS：要求至少用两种方法

# 5.str2中是否有数字，如果有都改成字母“A”

# 6.把str1中第3~7位置的字符串插入到str2中的第5个位置

# 7.反转str2,并打印反转后的内容和字符串的长度
str1 = " w_e_r_tD84 "
str2 = " w_e_r_t84D 78d"
# 1.比较这两个字符串是否相同，如果相同，打印“true”，如果不相同，打印“false”
# if str1==str2:
#     print('相同')
# else:
#     print("不相同")
#
print('2.找出这两个字符串从第几个位置开始不相等的,打印不相等的部分')
str_xt=[]
for i in range(0,len(str1)):
    if str1[i]==str2[i]:
        str_xt.append(str1[i])
    else:
        print('str1是从%d位开始不同的,str1不同的部分为:%s'%(i,str1[i:]))
        print('str2是从%d位开始不同的,str2不同的部分为:%s'%(i, str2[i:]))
print('相同部分：',str1[i],end='')
print(str_xt)
#
# print('3.把str2小写字母都改成大写')
# print(str2.upper())
#
# print('4.去掉str2两边的空格。PS：要求至少用两种方法')
#   # 1.
# print(str2.strip())
#   # 2
# st_1=str2.lstrip()
# st_2=st_1.rstrip()
# print(st_2)

# print("5.str2中是否有数字，如果有都改成字母'A'")
# tep=[]
# for i in range(0,len(str2)):
#     if str2[i] in ['0','1','2','3','4','5','6','7','8','9']:
#         print(i)
#         tep.append(i)
# lst=list(str2)
# for r in tep:
#     lst[r]='A'
# st=''
# sr=st.join(lst)
# print(sr)
# print('6.把str1中第3~7位置的字符串插入到str2中的第5个位置')
# str_6=str1[2:6]
# strt_6=str2[4]
# print(str2.replace(strt_6,str_6))
#
# # 7.反转str2,并打印反转后的内容和字符串的长度
# print('7.反转str2,并打印反转后的内容和字符串的长度')
# for i in str2[-1: :-1]:
#     print(i,end='')
# print(len(str2))