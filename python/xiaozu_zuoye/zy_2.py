# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
# 因为153=1的三次方＋5的三次方＋3的三次方。
import  math

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            num=str(i)+str(j)+str(k)
            my_num=int(num)
            if my_num==i**3+j**3+k**3:
                print(my_num)