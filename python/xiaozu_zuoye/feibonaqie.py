#斐波那契数列（Fibonacci sequence），
# 又称黄金分割数列，指的是这样一个数列：
# 0、1、1、2、3、5、8、13、21、34、……。
a=0
b=1
for i in range(0,100):
    print(a,end='\t')
    print(b,end='\t')
    a+=b
    b+=a