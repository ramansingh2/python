from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
raman=Tk()

raman.title('raman')
raman.geometry('400x400')
#b=Button(raman,text='simple',padx=10,pady=10)
#b.pack(padx=10,pady=10)



def r1():
    messagebox.showinfo('hello','red button clicked')

def b1():
    messagebox.showinfo('hellob', 'blue button clicked')


def g1():
    messagebox.showinfo('hellog','green button clicked')


def y1():
    messagebox.showinfo('helloy','yellow button clicked')


a=PhotoImage(file=r'C:\Users\Hp\Pictures\a.jpg')

rb=Button(raman,text='red',command=r1,activebackground='pink',activeforeground='red',background='pink',foreground='red',pady=10,padx=10,image='C:/Users/Hp/Pictures/download.gif',compound=LEFT)

bb=Button(raman,text='blue',command=b1,activebackground='pink',activeforeground='blue',background='pink',foreground='blue')
gb=Button(raman,text='green',command=g1,activebackground='pink',activeforeground='green',background='pink',foreground='green')
yb=Button(raman,text='yellow',command=y1,activebackground='pink',activeforeground='yellow',background='pink',foreground='yellow')

rb.pack(side=LEFT)
bb.pack(side=TOP)
gb.pack(side=RIGHT)
yb.pack(side=BOTTOM)

raman.mainloop()