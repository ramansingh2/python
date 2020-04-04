from tkinter import *
from tkinter import messagebox
raman=Tk()
raman.geometry('400x400')

def fun():
    messagebox.showinfo('hello','you clickeed the button')


name=Label(raman,text="name").place(x=30,y=50)
email=Label(raman,text='email').place(x=30,y=90)

password=Label(raman,text='password',cursor='arrow',fg='green',relief=SUNKEN).place(x=30,y=130)

submit_button=Button(raman,text='submit',command=fun,activebackground='pink',bg='light blue').place(x=30,y=170)
e1=Entry(raman).place(x=80,y=50)
e2=Entry(raman).place(x=80,y=90)
e3=Entry(raman,show='*').place(x=90,y=130)
raman.mainloop()