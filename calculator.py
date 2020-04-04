from tkinter import *
from tkinter import messagebox

from functools import partial

raman=Tk()
raman.geometry('400x400')
def f1(label_result,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    label_result.config(text='Result=%d'% result)
    return


raman.title('Calculaor')


number1=StringVar()
number2=StringVar()

lb1=Label(raman,text='A',padx=10,relief=RAISED).grid(row=1,column=0)  #.place(x=10,)
lb1=Label(raman,text='B',padx=10,relief=RIDGE).grid(row=2,column=0)  #.place(x=10,y=35)

lb_result=Label(raman)
lb_result.grid(row=7,column=2)
en1=Entry(raman,textvariable=number1).grid(row=1,column=2)
en1=Entry(raman,textvariable=number2).grid(row=2,column=2)

f1=partial(f1,lb_result,number1,number2)

bt1=Button(raman,text="calculate",relief=RAISED,command=f1).grid(row=3,column=0)


raman.mainloop()
