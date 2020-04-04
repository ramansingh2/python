from tkinter import *
raman=Tk()


var1=IntVar()
Checkbutton(raman,text='male',variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(raman,text='female',variable=var2).grid(row=1,sticky=W)
Label(raman,text='First name').grid(row=0)
Label(raman,text='last name').grid(row=1)
e1=Entry(raman)
e2=Entry(raman)

e1.grid(row=0,column=1)

e2.grid(row=1,column=1)

raman.mainloop()



