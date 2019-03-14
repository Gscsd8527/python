from tkinter import *

tk = Tk()
tk.title('Hello World !')
text = Text(width=80,height=10)
text.pack()
lst = ['aaaaaa\n','bbbbbb\n','cccccc\n','dddddd\n',]
for i in lst:
    text.insert(INSERT,i)
text.mainloop()