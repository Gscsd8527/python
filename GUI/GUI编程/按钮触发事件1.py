from tkinter import *

def active():
    print('啦啦啦，我是卖菜的小当家')
root = Tk()
frame = Frame(root,width=500,height=500)
widget = Button(None,text='Hello, World',command=active)
widget.pack()
widget.mainloop()

