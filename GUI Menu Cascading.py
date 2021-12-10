from tkinter import *

def print():
    pass

root=Tk()
root.geometry("625x625")

mymenu=Menu(root)

fmenu=Menu(mymenu,tearoff=0) #to remove dashed line (which is to  obtain the whole submenu out) we use tearoff=0
fmenu.add_command(label="Save",command=print)
fmenu.add_command(label="Save As",command=print)
fmenu.add_separator()
fmenu.add_command(label="Print",command=print)
mymenu.add_cascade(label="File",menu=fmenu)



emenu=Menu(mymenu,tearoff=0) #to remove dashed line (which is to  obtain the whole submenu out) we use tearoff=0
emenu.add_command(label="Canvas",command=print)
emenu.add_separator()
emenu.add_command(label="Resize",command=print)
emenu.add_separator()
emenu.add_command(label="Colourise",command=print)
emenu.add_command(label="Filters",command=print)
emenu.add_command(label="Saturation",command=print)
mymenu.add_cascade(label="Edit",menu=emenu)


root.config(menu=mymenu) #One config is enough for any number of submenus and menus.

root.mainloop()