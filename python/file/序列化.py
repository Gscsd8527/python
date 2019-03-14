import pickle
dct={
    'tan':123,
    'zhen':456,
    'hua':789
}
cls=dct
output=open('G:/pythonfile/xuelie.txt','wb')
# 将类序列化到文件xuelie.txt中
pickle.dump(cls,output)
output.close()
output=open('G:/pythonfile/xuelie.txt','rb')
x=pickle.load(output)
print(x)
output.close()