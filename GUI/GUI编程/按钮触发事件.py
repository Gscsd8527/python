from tkinter import *

class App:
    def __init__(self,root):
        root.title('打招呼程序')  #标题
        frame = Frame(root,width=200,height=200) #创建一个框架，作用一般是在复杂的布局中起到将
        frame.pack()
        self.hi_there = Button(frame,text='打招呼',fg='blue',command=self.say_hi)
        self.hi_there.pack(side=LEFT)
    def say_hi(self):
        print('您刚才通过点击打招呼触发了我：大家好，我是Gscsd')

root = Tk()
app = App(root)
root.mainloop()