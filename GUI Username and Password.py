from tkinter import *
def defval():
    print(uservalue.get())
    print(passvalue.get())
window=Tk()
window.geometry("500x500")
frame1=Frame(window,borderwidth=6,bg="red",relief=GROOVE)
frame1.pack(side=LEFT,fill=Y)
# label=Label(frame,text="Hello!",font="CourierNew 100 ")
# label.pack()
button=Button(frame1,text="Click Me").pack(side=LEFT,padx=32)
frame2=Frame(window,borderwidth=6,bg="pink",relief=GROOVE)
frame2.pack(side=LEFT,fill=Y)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(frame2,textvariable=uservalue)
passentry=Entry(frame2,textvariable=passvalue)
button=Button(frame2,text="Click Me!",command=defval)
userentry.grid(row=0,padx=10,pady=10)
passentry.grid(row=1,padx=10,pady=10)
button.grid()
window.mainloop()