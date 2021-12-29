from tkinter import *

def check():
    print(var.get())

root=Tk()
root.title("Radiobuttons")
root.geometry("720x480")

Label(root,text="Hello in this way we get value from a Radio-Button").pack()

var=IntVar()
radio=Radiobutton(root,text="Radio-Button",variable=var,value=1).pack()

button=Button(root,text="Check",command=check).pack()


var1 = IntVar
list1= ["idly", "dosa", "samosa"]
for i in list1:
    x = list1.index(i)
    radio = Radiobutton(root, text=f"{i}", variable=var1, value=(x+1))
    radio.pack()
    pass


root.mainloop()