from tkinter import *
raman=Tk()
raman.title("raman singh")
#width x height
raman.geometry('444x234')


# width, height
raman.minsize(400,400)

raman.maxsize(1200,1000)
#border styling - relief--Sunken,raised,groove,ridge
lb=Label(text='raman singh is mhy name and thuis is my gui')
lb.pack()

title_label=Label(text='hello this is again raman singh',bg='green',fg='blue',padx=9,pady=99,font=('arial',20,'bold','italic'),borderwidth=5,relief=RIDGE)
title_label.pack(fill=X,padx=22,pady=22)

#important pack(options) options=anchor


photo=PhotoImage(file=r"C:\Users\Hp\Pictures\untitled.png")

photo_label=Label(image=photo)

photo_label.pack(side='bottom',anchor='ne')












raman.mainloop()
