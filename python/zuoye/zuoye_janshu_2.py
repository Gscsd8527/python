#  2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def my_count(mystr):
    sum_num,sum_zimu,sum_space,sum_sep=0,0,0,0
    for i in mystr:
        if i.isdigit():
            sum_num+=1
        elif i.isalpha():
            sum_zimu+=1
        elif i in ' ':
            sum_space+=1
        else:
            sum_sep+=1
    return sum_num,sum_zimu,sum_space,sum_sep
mystring='13  2rr55gd!^fg,45o 24tk!l lw&&#e4rt'
a,b,c,d=my_count(mystring)
print(a,b,c,d)




