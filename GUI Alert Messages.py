from re import L
from tkinter import *
from tkinter.filedialog import SaveAs
import tkinter.messagebox as tmb

def save():
    tmb.showwarning("Error","You have to first use 'Save As' option.")

def saveas():
    pass

def about():
    tmb.showinfo("About Me","My name is Vignesh and I am the one who created this GUI.")

def rate():
    val=tmb.askquestion("Rate Us","How do you rate this GUI")
    if val=="yes":
        msg="Thank You!"
    elif val=="no":
        msg="Sorry to hear that."
    tmb.showinfo("Experience",msg)

def ratebool():
    val=tmb.askyesno("Rate Us","How do you rate this GUI")#askyesno is bool and askquestion is string of "yes" or "no".
    print(val)
    if val==True:
        msg="Thank You!"
    elif val==False:
        msg="Sorry to hear that."
    tmb.showinfo("Experience",msg)    

def con():
    val=tmb.askyesnocancel("What now?","Continue?")#gives bool of True,False,None.
    print(val)

def err():
    val=tmb.showerror("Error!","Please correct your mistake.")
    print(val)

def confirm(): 
    val=tmb.askyesno("Quit","Are you sure?")
    if val:
        root.destroy() #Other way to close the tkinter window. 

root=Tk()
root.title("Alert Messages")
root.geometry("720x480")

mymenu=Menu(root)
fmenu=Menu(mymenu,tearoff=0)
fmenu.add_command(label="Save",command=save)
fmenu.add_command(label="Save As",command=saveas)
mymenu.add_cascade(label="File",menu=fmenu)

mymenu.add_command(label="About Us",command=about)
mymenu.add_command(label="Continue",command=con)
mymenu.add_command(label="Error",command=err)
mymenu.add_command(label="Rate Us",command=rate)
mymenu.add_command(label="Rate Us Bool",command=ratebool)
mymenu.add_command(label="Quit Confirm",command=confirm)
mymenu.add_command(label="Quit",command=quit)

Label(root,text="GUI Alert or Message Boxes.",font="PROMESHTwoRegular 32 bold").pack()

root.config(menu=mymenu)

root.mainloop()

