import os
#获取到指定文件夹目录
path='G:'
# 得到文件夹下所有的文件名称
files=os.listdir(path)
s=[]
# 遍历文件夹
for file in files:
    # 判断是否是文件夹，不是文件夹才打开
    if not os.path.join(file):
        # 打开文件
        f=open(path+'/'+file)
        # 创建迭代器
        iter_f=iter(f)
        str=''
        # 遍历文件，一遍遍执行遍历，读取文本
        for line in iter_f:
            str=str+line
            # 每个文件的文本存到list中
            s.append(str)
# 打印结果
print(s)