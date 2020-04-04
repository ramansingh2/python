from tkinter import *
from tkinter import ttk
raman=Tk()

b1=Button(raman,text='click')
b1.pack()

m1=PhotoImage(file='E:\q.gif')
b1.config(image=m1,compound=RIGHT)
raman.mainloop()



'''

#import tkinter

from tkinter import *

from PIL import ImageTk,Image

root=Tk()

#set width and height

canvas=Canvas(root,width=300,height=160)

#give this image path. image should be in png format.

#Example: "C:\\Users\\ASUS\\OneDrive\\Pictures\\image.png"

image=ImageTk.PhotoImage(Image.open('E:\q.gif'))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
root.mainloop()

'''