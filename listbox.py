from tkinter import *

top = Tk()

top.geometry("200x250")

lbl = Label(top, text="A list of favourite countries...")

listbox = Listbox(top)

listbox.insert(1, "India")

listbox.insert(2, "USA")

listbox.insert(3, "Japan")

listbox.insert(4, "Austrelia")

# this button will delete the selected item from the list

btn = Button(top, text="delete", command=lambda listbox=listbox: listbox.delete(ANCHOR))

lbl.pack()

listbox.pack()

btn.pack()
top.mainloop()
