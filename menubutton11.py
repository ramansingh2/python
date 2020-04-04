from tkinter import *
raman=Tk()

raman.title("pycharm")

def f1():
    print("hello thusi is raman singh ")


main=Menu(raman)
main.add_command(label='file',command=f1)
main.add_command(label='quit',command=quit)


m1=Menu(main,tearoff=0)
m1.add_command(label="new project",command=f1)
m1.add_command(label='save')
m1.add_command(label='save as')
m1.add_separator()
m1.add_command(label='print')
m1.add_command(label='raman')
raman.config(menu=main)
main.add_cascade(label='fillle',menu=m1)



raman.mainloop()