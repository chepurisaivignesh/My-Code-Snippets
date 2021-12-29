from tkinter import *
from datetime import datetime
def book():
    listy=[
        [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

    global checking
    
    ticket=[]
    val=" "
    
    for j in range(len(listy)):
        for i in range(len(listy[j])):
            if listy[j][i]==1 and checking[j][i]==0:
                if j==0:
                    val="A"
                elif j==1:
                    val="B"    
                elif j==2:
                    val="C"
                ticket.append(str(val+str(i+1)))
                checking[j][i]=1 

    stringy=""
    for item in ticket:
        stringy=stringy+item+" "

    c=numtic.get()
    c="Number of Tickets Booked: "+str(len(ticket))
    numtic.set(c)   

    d=ticnum.get()
    d="Tickets Booked are: "+stringy
    ticnum.set(d)
    global order
    with open("Booking.txt","a") as f:
        f.write("Booking Number: "+str(order)+"\n")
        f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
        f.write(c+"\n")
        f.write(d+"\n")
        f.write("\n")

    if checking[0][0]==1:
        A1.config(state=DISABLED)
    if checking[0][1]==1:
        A2.config(state=DISABLED)
    if checking[0][2]==1:
        A3.config(state=DISABLED)
    if checking[0][3]==1:
        A4.config(state=DISABLED)
    if checking[0][4]==1:
        A5.config(state=DISABLED)
    if checking[0][5]==1:
        A6.config(state=DISABLED)
    if checking[0][6]==1:
        A7.config(state=DISABLED)
    if checking[0][7]==1:
        A8.config(state=DISABLED)
    if checking[0][8]==1:
        A9.config(state=DISABLED)
    if checking[0][9]==1:
        A10.config(state=DISABLED)
    if checking[1][0]==1:
        B1.config(state=DISABLED)
    if checking[1][1]==1:
        B2.config(state=DISABLED)
    if checking[1][2]==1:
        B3.config(state=DISABLED)
    if checking[1][3]==1:
        B4.config(state=DISABLED)
    if checking[1][4]==1:
        B5.config(state=DISABLED)
    if checking[1][5]==1:
        B6.config(state=DISABLED)
    if checking[1][6]==1:
        B7.config(state=DISABLED)
    if checking[1][7]==1:
        B8.config(state=DISABLED)
    if checking[1][8]==1:
        B9.config(state=DISABLED)
    if checking[1][9]==1:
        B10.config(state=DISABLED)
    if checking[2][0]==1:
        C1.config(state=DISABLED)
    if checking[2][1]==1:
        C2.config(state=DISABLED)
    if checking[2][2]==1:
        C3.config(state=DISABLED)
    if checking[2][3]==1:
        C4.config(state=DISABLED)
    if checking[2][4]==1:
        C5.config(state=DISABLED)
    if checking[2][5]==1:
        C6.config(state=DISABLED)
    if checking[2][6]==1:
        C7.config(state=DISABLED)
    if checking[2][7]==1:
        C8.config(state=DISABLED)
    if checking[2][8]==1:
        C9.config(state=DISABLED)
    if checking[2][9]==1:
        C10.config(state=DISABLED)
    
    order+=1

def newbook():
    numtic.set("Number of Tickets Booked: 0")
    ticnum.set("")
    
# -------------------------------------------------------------
root=Tk()
root.title("Book Your Tickets")
root.geometry("600x600")
root.resizable(False, False) 

canvas = Canvas(root,height=120,width=600,)    
canvas.place(x=0,y=0)
canvas.create_rectangle(
    0, 0, 600, 120,
    outline="#fb0",
    fill="#fb0")
canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

checking=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
order=1

A_1=IntVar()
A_2=IntVar()
A_3=IntVar()
A_4=IntVar()
A_5=IntVar()
A_6=IntVar()
A_7=IntVar()
A_8=IntVar()
A_9=IntVar()
A_10=IntVar()

A1=Checkbutton(root,text="A1",variable=A_1)
A2=Checkbutton(root,text="A2",variable=A_2)
A3=Checkbutton(root,text="A3",variable=A_3)
A4=Checkbutton(root,text="A4",variable=A_4)
A5=Checkbutton(root,text="A5",variable=A_5)
A6=Checkbutton(root,text="A6",variable=A_6)
A7=Checkbutton(root,text="A7",variable=A_7)
A8=Checkbutton(root,text="A8",variable=A_8)
A9=Checkbutton(root,text="A9",variable=A_9)
A10=Checkbutton(root,text="A10",variable=A_10)

A1.place(x=10,y=130)
A2.place(x=70,y=130)
A3.place(x=130,y=130)
A4.place(x=190,y=130)
A5.place(x=250,y=130)
A6.place(x=310,y=130)
A7.place(x=370,y=130)
A8.place(x=430,y=130)
A9.place(x=490,y=130)
A10.place(x=545,y=130)

B_1=IntVar()
B_2=IntVar()
B_3=IntVar()
B_4=IntVar()
B_5=IntVar()
B_6=IntVar()
B_7=IntVar()
B_8=IntVar()
B_9=IntVar()
B_10=IntVar()

B1=Checkbutton(root,text="B1",variable=B_1)
B2=Checkbutton(root,text="B2",variable=B_2)
B3=Checkbutton(root,text="B3",variable=B_3)
B4=Checkbutton(root,text="B4",variable=B_4)
B5=Checkbutton(root,text="B5",variable=B_5)
B6=Checkbutton(root,text="B6",variable=B_6)
B7=Checkbutton(root,text="B7",variable=B_7)
B8=Checkbutton(root,text="B8",variable=B_8)
B9=Checkbutton(root,text="B9",variable=B_9)
B10=Checkbutton(root,text="B10",variable=B_10)

B1.place(x=10,y=180)
B2.place(x=70,y=180)
B3.place(x=130,y=180)
B4.place(x=190,y=180)
B5.place(x=250,y=180)
B6.place(x=310,y=180)
B7.place(x=370,y=180)
B8.place(x=430,y=180)
B9.place(x=490,y=180)
B10.place(x=545,y=180)

C_1=IntVar()
C_2=IntVar()
C_3=IntVar()
C_4=IntVar()
C_5=IntVar()
C_6=IntVar()
C_7=IntVar()
C_8=IntVar()
C_9=IntVar()
C_10=IntVar()

C1=Checkbutton(root,text="C1",variable=C_1)
C2=Checkbutton(root,text="C2",variable=C_2)
C3=Checkbutton(root,text="C3",variable=C_3)
C4=Checkbutton(root,text="C4",variable=C_4)
C5=Checkbutton(root,text="C5",variable=C_5)
C6=Checkbutton(root,text="C6",variable=C_6)
C7=Checkbutton(root,text="C7",variable=C_7)
C8=Checkbutton(root,text="C8",variable=C_8)
C9=Checkbutton(root,text="C9",variable=C_9)
C10=Checkbutton(root,text="C10",variable=C_10)

C1.place(x=10,y=230)
C2.place(x=70,y=230)
C3.place(x=130,y=230)
C4.place(x=190,y=230)
C5.place(x=250,y=230)
C6.place(x=310,y=230)
C7.place(x=370,y=230)
C8.place(x=430,y=230)
C9.place(x=490,y=230)
C10.place(x=545,y=230)

book=Button(text="BOOK NOW!",command=book).place(x=250,y=300)

numtic=StringVar()
numtic.set("Number of Tickets Booked: 0")
ticnum=StringVar()

noftic=Label(root,textvariable=numtic).place(y=340,x=210)
ticno=Label(root,textvariable=ticnum).place(y=370,x=220)

book=Button(text="New Booking!",command=newbook).place(x=245,y=410)
root.mainloop()   