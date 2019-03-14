from tkinter import *


def printInfo():
    # 清理entry2
    entry2.delete(0, END)
    # 根据输入半径计算面积
    R = int(entry1.get())
    S = 3.1415926 * R * R
    entry2.insert(10, S)
    # 清空entry2控件
    entry1.delete(0, END)


# 初始化Tk()
myWindow = Tk()
# 设置标题
myWindow.title('Python GUI Learning')

# 标签控件布局
Label(myWindow, text="input").grid(row=0)
Label(myWindow, text="output").grid(row=1)

# Entry控件布局
entry1 = Entry(myWindow)
entry2 = Entry(myWindow)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

# Quit按钮退出；Run按钮打印计算结果
Button(myWindow, text='Quit', command=myWindow.quit).grid(row=2, column=0, sticky=W, padx=5, pady=5)
Button(myWindow, text='Run', command=printInfo).grid(row=2, column=1, sticky=W, padx=5, pady=5)

# 进入消息循环
myWindow.mainloop()
