from tkinter import *

root = Tk()

text = Text(root, width=100, height=3, fg='red')
# insert的第一个参数为索引;第二个为添加的内容
text.insert(1.0, 'fgjsdfkjgierjgidfkgjol ')
#
text.insert(1.0, 'uilqwwwwwre ')
#
text.insert('2.end', '\n')
text.insert(2.0, 'weqrfrfrfrfrfrfrfrf ')
text.insert(2.0, 'qwrewrrrrrw ')
# text.insert(3,'fgjsdfkjgierjgidfkgjol')
text.pack()
root.mainloop()
