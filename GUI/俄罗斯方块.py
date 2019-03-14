from tkinter import *
import time
tk=Tk()
# 标题
tk.title('俄罗斯方块')
# 创建一个窗口，宽400 高800 背景为蓝色 边框宽度为0
canvas=Canvas(tk,width=500,height=700,bg='blue',bd=0)
# 将该组件包装到一个父组件中，创建一个版面
canvas.pack()
p1=100,10
p2=100,60
p3=50,60
p4=50,110
p5=150,110
p6=150,10
# 获取图形的ID
id=canvas.create_polygon(p1,p2,p3,p4,p5,p6)
        # 调用移动方法
        # temp_move()
# def temp_move():
#     while True:
#         for i in range(60):
#             # 把ID为1的对象水平移动0像素，向下移动5像素
#             canvas.move(1, 0, 5)
#             # 强制更新屏幕，即重画图形
#             tk.update()
#             # 休息0.05秒后再继续执行程序
#             time.sleep(0.05)

def key_move(event):
    if event.keysym=='Down':
        canvas.move(id,0,5)
    elif event.keysym=="Up":
        canvas.move((id,0,-5))
    elif event.keysym=="Left":
        canvas.move(id,-5,0)
    elif event.keysym=='Right':
        canvas.move(id,5,0)
# while True:
#     for i in range(60):
#         # 把ID为1的对象水平移动0像素，向下移动5像素
#         id.move(1, 0, 5)
#         # 强制更新屏幕，即重画图形
#         tk.update()
#         # 休息0.05秒后再继续执行程序
#         time.sleep(0.05)
canvas.bind_all("<KeyPress-Up>",key_move)
canvas.bind_all("<KeyPress-Down>",key_move)
canvas.bind_all("<KeyPress-Left>",key_move)
canvas.bind_all("<KeyPress-Right>",key_move)
tk.mainloop()
