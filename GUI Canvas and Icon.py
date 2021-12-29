from tkinter import *
root = Tk()
root.geometry("500x500")
# root.iconbitmap("detective_investigation_avatar_man_police_icon_191340.ico") To insert Logo to window.
canv = Canvas(root,bg="black")
canv.pack()
canv.create_line (300,100,0,0,fill="red")
canv.create_rectangle(300,100,500,500,fill="blue")

canv.create_line(10,10,100,10,100,200,10,10,fill="white")
root.mainloop()