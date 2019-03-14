# 2.文件定位
f=open('G:/pythonfile/t1.txt','rb')
print(f.read())
f.seek(5)
print(f.tell())
f.seek(10,1)
print(f.tell())
f.seek(-10,2)
print(f.tell())