from tkinter import *
tk=Tk()
tk.title('Game')
tk.resizable(0,0)
tk.attributes('-topmost',1)
canvas=Canvas(tk,width=500,helght=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()