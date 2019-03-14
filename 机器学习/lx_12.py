import numpy as np
# from matplotlib.pyplot import *
x = np.array(
    [[1,3,3],
     [1,4,1],
     [1,1,1]]
)

y = np.array([1,1,-1])

# 权值初始化
w = (np.random.random(3)-0.5)
print(w)
# 设置学习率
lr = 0.11

# 计算迭代次数
n = 0

# 神经网络输出
O = 0

# 学习并更新权值
def update():
    global x,y,w,lr,n
    n+=1
    s = np.dot(x,w.T)
    O = np.sign(s)
    w_c = lr*((y-O.T).dot(x))/int

# 重复进行学习并更新权值
for _ in range(100):
    update()
    print(w)  #显示当前权值
    print(n)  #显示迭代次数
    O = np.sign(np.dot(x,w.T))
    # 判断O、y.T是否相等，返回的是一组数据，所以要判断all是否全部相等
    if(O==y.T).all():
        print('Finished')
        print('epoch',n)
        break
