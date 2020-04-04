from tkinter import *
from ttkthemes import ThemedStyle
root=Tk()

root.geometry('400x400')
to = Toplevel(root)
to.geometry('100x100')
def open():
    top=Toplevel(root)
    b = Button(top, text='open', command=open).grid()
    top.mainloop()
root.resizable(0,0)
theme='scidgreen'
logins = ThemedStyle(root)
logins.set_theme(theme)

b=Button(root,text='open',command=open).grid()
b=Button(to,text='open',command=open).grid()

root.mainloop()

to.mainloop(Toplevel)