from tkinter import *
from tkinter import messagebox
import os

tk = Tk()
tk.title('My Phone Number Book')
lbl = Label(tk, text="欢迎使用简易电话本！", font=('Microsoft Yahei', 20))
lbl.grid(column=100, row=5)
tk.geometry('350x200')

def inp_num_do():
    os.system('start inp_num.py')
def src_num_do():
    os.system('start src_num.py')
def ect_prg_do():
    messagebox.showwarning('真的吗？', '真的要退出吗？')
    messagebox.showinfo('Info','官网：？；作者：？')
    exit()

inp_num = Button(tk, text='添加号码', command=inp_num_do)
inp_num.grid(column=101, row=6)
src_num = Button(tk, text='查询号码', command=src_num_do)
src_num.grid(column=101, row=12)
ect_prg = Button(tk, text='退出程序', command=ect_prg_do)
ect_prg.grid(column=101, row=18)

tk.mainloop()