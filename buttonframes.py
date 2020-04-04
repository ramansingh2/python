from tkinter import *
from tkinter import messagebox

raman=Tk()

raman.geometry('400x400')

f1=Frame(raman,bg='grey',borderwidth=4)
f1.pack(side=LEFT,anchor='nw',pady=10,fill="x")


b1=Button(f1,text='hello')
b1.pack(side=LEFT,padx=22)


b2=Button(f1,text='lklkhello')
b2.pack(side=LEFT,padx=22)

b3=Button(f1,text='hellofegf')
b3.pack(side=LEFT,padx=22)

b4=Button(f1,text='hellojhhyj')
b4.pack(side=LEFT)





raman.mainloop()