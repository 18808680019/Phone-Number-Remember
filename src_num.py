from tkinter import *
from tkinter import messagebox

tk = Tk()
lbl = Label(tk, text='号码查询器', font=('Microsoft Yahei', 20))
lbl.grid(column=1,row=1)
tk.geometry('500x350')
selected = IntVar()
f = open('Phone_Number.txt', encoding='utf-8')

rad1 = Radiobutton(tk, text="以号码查询", value=1, variable=selected)
rad1.grid(column=2,row=2)
rad2 = Radiobutton(tk, text="以账户查询", value=2, variable=selected)
rad2.grid(column=3,row=2)



def button1_clicked():
    if selected.get() == 1:
        lbl_choose = Label(tk, text='号码：')
        lbl_choose.grid(column=1,row=5)
        entry_choose = Entry(tk)
        entry_choose.grid(column=2,row=5)
        def _rad1():
            while True:
                a = entry_choose.get()
                if len(a) != 11:
                    messagebox.showerror('Error', '无效号码！')
                    messagebox.showinfo('Info', '请重新输入！')
                    break
                else:
                    try:
                        int(a)
                    except:
                        messagebox.showerror('Error', '无效号码！')
                        messagebox.showinfo('Info', '请重新输入！')
                        break
                    else:
                        k = 1
                        break
            if k == 1:
                i = f.read()
                l = i.split('\n')
                for k in range(1,len(l)):
                    k2 = l[k].split('\t')
                    k3 = k2[0].split(':')
                    if k3[1] == a:
                        lbl3 = Label(tk, text=l[k])
                        lbl3.grid(column=2,row=8)
                        messagebox.showinfo('查询完毕,关闭窗口以退出', l[k])
                        exit()
            else:
                messagebox.showinfo('Info', '号码不存在！')
        button2 = Button(tk, text='确认', command=_rad1)
        button2.grid(column=5,row=7)
    elif selected.get() == 2:
        lbl_choose = Label(tk, text='用户名：')
        lbl_choose.grid(column=1,row=5)
        entry_choose = Entry(tk)
        entry_choose.grid(column=2,row=5)
        def _rad1():
            while True:
                a = entry_choose.get()
                if len(a) == 0:
                    messagebox.showerror('Error', '无效用户名！')
                    messagebox.showinfo('Info', '请重新输入！')
                    break
                else:
                    k = 1
                    break
            if k == 1:
                i = f.read()
                l = i.split('\n')
                for k in range(1,len(l)):
                    k2 = l[k].split('\t')
                    k3 = k2[1].split(':')
                    if k3[1] == a:
                        lbl3 = Label(tk, text=l[k])
                        lbl3.grid(column=2,row=8)
                        messagebox.showinfo('查询完毕,关闭窗口以退出', l[k])
                        exit()
                else:
                    messagebox.showinfo('Info', '用户不存在！')
        button2 = Button(tk, text='确认', command=_rad1)
        button2.grid(column=5,row=7)

        
button1 = Button(tk, text='选择完毕', command=button1_clicked)
button1.grid(column=4,row=4)

tk.mainloop()