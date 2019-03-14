# 写一个幅度
from tkinter import *
tk=Tk()
canvas=Canvas(tk,width=400,height=500,bg='red',bd=0)
canvas.pack()
coord=10,10,200,80
# start表示从哪个角度开始画的
canvas.create_arc(coord,start=0,extent=359,style=ARC)

# 进入主循环体，否则一闪而过看不到界面
tk.mainloop()