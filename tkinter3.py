from tkinter import *
raman=Tk()
frame=Frame(raman)
frame.pack()
bottomframe=Frame(raman)
bottomframe.pack(side=BOTTOM)
redbutton=Button(frame,text='red',fg='red')
redbutton.pack(side=LEFT)
greenbutton=Button(frame,text='Brown',fg='brown')
greenbutton.pack(side=LEFT)
bluebutton=Button(frame,text='Blue',fg='blue')
bluebutton.pack(side=LEFT)
blackbutton=Button(raman,text='black',fg='black')
blackbutton.pack(side=BOTTOM)

w=Label(raman,text='ramansingh is my name ')
w.pack()




raman.mainloop()
