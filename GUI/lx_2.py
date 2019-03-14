# 水平方向移动三角形
from tkinter import *
import time
tk=Tk()
canvas=Canvas(tk,width=400,height=500,bg='red',bd=0)
canvas.pack()
poin1=10,10
poin2=10,60
poin3=50,35
canvas.create_polygon(poin1,poin2,poin3)
while True:
    for i in range(60):
        # 1表示从开始位置 5表示从x轴移动5 3表示y轴移动3
        canvas.move(1,5,3)
        tk.update()
        time.sleep(0.05)
    for i in range(60):
        # 1表示从开始位置 5表示从x轴移动5 3表示y轴移动3
        canvas.move(1,-5,-3)
        tk.update()
        time.sleep(0.05)
tk.mainloop()

