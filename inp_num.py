from tkinter import *
from tkinter import messagebox
from os import system

a = 0

tk = Tk()
lbl = Label(tk, text='号码写入工具', font=('Microsoft Yahei', 20))
lbl.grid(column=1,row=1)
tk.geometry('500x350')

def inp_button_clicked():
    a = inp_num_spin.get()
    b = inp_user_entry.get()
    while True:
        try:
            int(a)
        except:
            messagebox.showerror('Error', '请输入电话号码!')
            messagebox.showinfo('Info', '请在重新输入电话号码!')
            break
        else:
            if len(a) != 11:
                messagebox.showerror('Error', '请输入长度11为电话号码!')
                messagebox.showinfo('Info', '请在重新输入电话号码!')
                break
            else:
                k = 1
        if len(b) == 0:
            messagebox.showerror('Error', '请输入用户名!')
            break
        else:
            k = 1
            break
    if k == 1:
        messagebox.showinfo('Info', '开始载入!')
        f = open('Phone_Number.txt', 'a', encoding='utf-8')
        f.write('\n号码:')
        f.write(a)
        f.write('\t用户:')
        f.write(b)
        messagebox.showinfo('Info', '载入完毕!')
        exit()


inp_num_lbl = Label(tk, text='号码：', font=('Microsoft Yahei', 10))
inp_num_lbl.grid(column=1,row=2)
inp_num_spin = Spinbox(tk)
inp_num_spin.grid(column=2,row=2)

inp_user_lbl = Label(tk, text='用户名：', font=('Microsoft Yahei', 10))
inp_user_lbl.grid(column=1,row=3)
inp_user_entry = Entry(tk)
inp_user_entry.grid(column=2,row=3)

inp_button = Button(tk, text='确认写入', command=inp_button_clicked)
inp_button.grid(column=100,row=5)

tk.mainloop()