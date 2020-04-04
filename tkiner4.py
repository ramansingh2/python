
from tkinter import *
raman=Tk()

"""
Lb=Listbox(raman)
Lb.insert(1,'python')
Lb.insert(2,'java')
Lb.insert(3,'c++')
Lb.insert(4,'other')

Lb.pack()
raman.mainloop()
"""

print('hello this is raman singh ')

mb=Menubutton(raman,text=&quot;GfG&quot;)
mb.grid()
mb.menu=Menu(mb,tearoff=0)
mb[&quot;menu&quot;]= mb.menu
cVar=IntVar()
aVar=IntVar()
mb.menu.add_checkbutton(label='about',variable=aVar)
mb.menu.add_checkbutton(label='Contact',variable=cVar)
mb.pack()
raman.mainloop()



