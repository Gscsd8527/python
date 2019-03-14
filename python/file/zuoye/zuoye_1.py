# 1.文件复制
f1=open('G:/pythonfile/t1.txt','r')
f2=open('G:/pythonfile/t2.txt','w+')
mystr=f1.read()
print(mystr)
f2.write(mystr)
f1.close()
f2.close()


