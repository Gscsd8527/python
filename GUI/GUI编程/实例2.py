from tkinter import *
root = Tk()

lst = ['C','python','php','html','SQL','java']
movie = ['CSS','jQuery','Bootstrap']
lsttb1 = Listbox(root)   #创建两个列表组件
lsttb2 = Listbox(root)
for item in lst:         #第一个小部件插入数据
    lsttb1.insert(0,item)
for item in movie:       # 第二个小部件插入数据
    lsttb2.insert(0,item)
root.title('啦啦啦') #head
lsttb1.pack()
lsttb2.pack()
root.mainloop()  #进入消息循环