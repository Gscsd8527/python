# x表示同意或不同意 1,0
# w表示权重
# 最简模型，模拟神经元，设置权重，定义sign来执行这个函数
def nu(x,w):
    offset = 0.5
    n=len(x)
    sum = 0.0
    for i in range(n):
        sum += x[i] * w[i]
    sum += offset
    return sum

def sign(s):
    return s>0.5