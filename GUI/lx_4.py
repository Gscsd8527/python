import tkinter as tk
root=tk.Tk()
root.title('FishC Demo')
theLabel=tk.Label(root,text='----------我的第二个窗口程序----------')
# 将该组件包装到一个父组件中，创建一个版面，它会自动配置窗口的大小
theLabel.pack()
# 执行程序后进入主事件循环
root.mainloop()