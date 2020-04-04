from tkinter import *
from tkinter import messagebox
raman=Tk()
raman.geometry('400x400')

def getvals():
    messagebox.showinfo('hello',uservalue.get())

    messagebox.showinfo('hello',passwordvalue.get())


f1=Frame(raman,bg="grey",borderwidth=10,relief=RAISED)
f1.pack(side=LEFT,fill=X)


user=Label(f1,text="user").grid(row=0,column=0)
password=Label(f1,text="password").grid(row=1,column=0)
uservalue=StringVar()
passwordvalue=StringVar()

ue=Entry(f1,textvariable=uservalue).grid(row=0,column=1)
pe=Entry(f1,textvariable=passwordvalue,show="*").grid(row=1,column=1)

b1=Button(f1,text='submit',command=getvals,relief=RAISED).grid(row=2,column=1)

raman.mainloop()
