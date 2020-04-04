from tkinter import *

raman=Tk()

checkvar1=IntVar(value=1)  #value=1 for default check
checkvar2=IntVar(value=1)
checkvar3=IntVar()
cb1=Checkbutton(raman,variable=checkvar1,text='cbbb',onvalue=1,offvalue=0,height=2,width=10)
cb2=Checkbutton(raman,variable=checkvar2,text='cccc',onvalue=1,offvalue=0,height=2,width=10)
cb3=Checkbutton(raman,variable=checkvar3,text='dddd',onvalue=1,offvalue=0,height=2,width=10)



cb1.pack(anchor='nw')
cb2.pack(anchor='nw')
cb3.pack(anchor='nw')



raman.mainloop()

