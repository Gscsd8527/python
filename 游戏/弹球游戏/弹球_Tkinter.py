from tkinter import *
import random
import time
tk=Tk()
tk.title('弹球游戏')
# 创建一个窗口，宽500 高650 背景为蓝色 边框宽度为0
canvas=Canvas(tk,width=500,height=650,bg='blue',bd=0,highlightthickness=0 )
# 将该组件包装到一个父组件中，创建一个版面
canvas.pack()
# 定义球类
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        # 给小球加一个起始位置
        self.x=starts[0]
        self.y=-3
        # 获取画布的当前高度
        self.canvas_height=self.canvas.winfo_height()
        # 获取画布的当前宽度
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom=False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if self.hit_bottom(pos)==True:
            self.y=-3
        if pos[3]>=self.canvas_height:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3


# 定义球拍类
class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(200,500,350,510,fill='black')
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas.width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def draw(self):
        # 由变量X决定在水平方向移动
        self.canvas.move(self.id,self.x,0)
        # 获取球拍的当前位置
        pos=self.canvas.coords(self.id)
        # 判断球拍是否撞到了屏幕的左右边界
        if pos[0]<=0:
            self.x=0
        elif pos[2]>=self.canvas_width:
            self.x=0
    def turn_left(self,evt):
        self.x=-2
    def turn_right(self,evt):
        self.x=2
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False

paddle=Paddle(canvas,'black')
ball=Ball(canvas,paddle,'red')
while True:
    ball.draw()
    paddle.draw()
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
tk.mainloop()