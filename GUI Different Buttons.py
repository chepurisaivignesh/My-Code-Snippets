from tkinter import *

root=Tk()
root.geometry("720x480")
def button1():
    s="*\n"+"* *\n"+"* * *\n"
    t.set(s)
def button2():
    s="*\n"+"* *\n"+"* * *\n"+"* * * *\n"
    t.set(s)
def button3():
    s="*\n"+"* *\n"+"* * *\n"+"* * * *\n"+"* * * * *\n"
    t.set(s)
def button4():
    s="*\n"+"* *\n"+"* * *\n"+"* * * *\n"+"* * * * *\n"+"* * * * * *\n"
    t.set(s)
def button5():
    s="*\n"+"* *\n"+"* * *\n"+"* * * *\n"+"* * * * *\n"+"* * * * * *\n"+"* * * * * * *\n"
    t.set(s)
def clear():
    t.set("")


but1=Button(root,text="PATTERN1",command=button1).pack()
but2=Button(root,text="PATTERN2",command=button2).pack()
but3=Button(root,text="PATTERN3",command=button3).pack()
but4=Button(root,text="PATTERN4",command=button4).pack()
but5=Button(root,text="PATTERN5",command=button5).pack()

t=StringVar()
cl=Button(root,text="Clear",command=clear).pack(pady=20)
label=Label(root,textvariable=t).pack(pady=10)


root.mainloop()