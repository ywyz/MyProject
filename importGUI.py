from tkinter import *

# 创建窗口
window = Tk()
window.title("数据查询")
window.geometry('1024x800')

# 创建姓名填写框
name = Entry(window, show=None, font=('Arial', 14))
name.pack()

# 创建查询框
find = Button(window, text='查询', font=('Arial', 14), width=10, height=2, command=DISABLED)
find.pack(

)

window.mainloop()
