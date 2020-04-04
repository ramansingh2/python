from tkinter import *
raman=Tk()

raman.geometry('400x400')
f1=Frame(raman,bg="grey",borderwidth=6,relief=RAISED)
f1.pack(side=LEFT,fill=Y)
l=Label(f1,text='project tkinter-pycharm',bg='green')
l.pack(pady=142)
f2=Frame(raman,bg='grey',borderwidth=8,relief=RAISED)
f2.pack(side=TOP,fill=X)
l1=Label(f2,text='welcome to pycharm',bg='green',font=('algerian',19,'bold'))
l1.pack()
raman.mainloop()
