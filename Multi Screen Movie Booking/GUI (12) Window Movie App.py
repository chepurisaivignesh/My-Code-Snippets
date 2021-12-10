import tkinter
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime

def show11():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking11

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking11[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking11[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order11
        with open("Booking.txt","a") as f:
            f.write("Eternals Movie\n")
            f.write("Morning Show--> 11:00 AM\n")
            f.write("Booking Number: "+str(order11)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking11[0][0]==1:
            A1.config(state=DISABLED)
        if checking11[0][1]==1:
            A2.config(state=DISABLED)
        if checking11[0][2]==1:
            A3.config(state=DISABLED)
        if checking11[0][3]==1:
            A4.config(state=DISABLED)
        if checking11[0][4]==1:
            A5.config(state=DISABLED)
        if checking11[0][5]==1:
            A6.config(state=DISABLED)
        if checking11[0][6]==1:
            A7.config(state=DISABLED)
        if checking11[0][7]==1:
            A8.config(state=DISABLED)
        if checking11[0][8]==1:
            A9.config(state=DISABLED)
        if checking11[0][9]==1:
            A10.config(state=DISABLED)
        if checking11[1][0]==1:
            B1.config(state=DISABLED)
        if checking11[1][1]==1:
            B2.config(state=DISABLED)
        if checking11[1][2]==1:
            B3.config(state=DISABLED)
        if checking11[1][3]==1:
            B4.config(state=DISABLED)
        if checking11[1][4]==1:
            B5.config(state=DISABLED)
        if checking11[1][5]==1:
            B6.config(state=DISABLED)
        if checking11[1][6]==1:
            B7.config(state=DISABLED)
        if checking11[1][7]==1:
            B8.config(state=DISABLED)
        if checking11[1][8]==1:
            B9.config(state=DISABLED)
        if checking11[1][9]==1:
            B10.config(state=DISABLED)
        if checking11[2][0]==1:
            C1.config(state=DISABLED)
        if checking11[2][1]==1:
            C2.config(state=DISABLED)
        if checking11[2][2]==1:
            C3.config(state=DISABLED)
        if checking11[2][3]==1:
            C4.config(state=DISABLED)
        if checking11[2][4]==1:
            C5.config(state=DISABLED)
        if checking11[2][5]==1:
            C6.config(state=DISABLED)
        if checking11[2][6]==1:
            C7.config(state=DISABLED)
        if checking11[2][7]==1:
            C8.config(state=DISABLED)
        if checking11[2][8]==1:
            C9.config(state=DISABLED)
        if checking11[2][9]==1:
            C10.config(state=DISABLED)
        
        order11=order11+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Eternals, 11:00 AM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    Label(rootmovie1,text="First Class",font="20").place(x=250,y=220)
    Label(rootmovie1,text="Balcony",font="20").place(x=260,y=300)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking11[0][0]==1:
        A1.config(state=DISABLED)
    if checking11[0][1]==1:
        A2.config(state=DISABLED)
    if checking11[0][2]==1:
        A3.config(state=DISABLED)
    if checking11[0][3]==1:
        A4.config(state=DISABLED)
    if checking11[0][4]==1:
        A5.config(state=DISABLED)
    if checking11[0][5]==1:
        A6.config(state=DISABLED)
    if checking11[0][6]==1:
        A7.config(state=DISABLED)
    if checking11[0][7]==1:
        A8.config(state=DISABLED)
    if checking11[0][8]==1:
        A9.config(state=DISABLED)
    if checking11[0][9]==1:
        A10.config(state=DISABLED)
    if checking11[1][0]==1:
        B1.config(state=DISABLED)
    if checking11[1][1]==1:
        B2.config(state=DISABLED)
    if checking11[1][2]==1:
        B3.config(state=DISABLED)
    if checking11[1][3]==1:
        B4.config(state=DISABLED)
    if checking11[1][4]==1:
        B5.config(state=DISABLED)
    if checking11[1][5]==1:
        B6.config(state=DISABLED)
    if checking11[1][6]==1:
        B7.config(state=DISABLED)
    if checking11[1][7]==1:
        B8.config(state=DISABLED)
    if checking11[1][8]==1:
        B9.config(state=DISABLED)
    if checking11[1][9]==1:
        B10.config(state=DISABLED)
    if checking11[2][0]==1:
        C1.config(state=DISABLED)
    if checking11[2][1]==1:
        C2.config(state=DISABLED)
    if checking11[2][2]==1:
        C3.config(state=DISABLED)
    if checking11[2][3]==1:
        C4.config(state=DISABLED)
    if checking11[2][4]==1:
        C5.config(state=DISABLED)
    if checking11[2][5]==1:
        C6.config(state=DISABLED)
    if checking11[2][6]==1:
        C7.config(state=DISABLED)
    if checking11[2][7]==1:
        C8.config(state=DISABLED)
    if checking11[2][8]==1:
        C9.config(state=DISABLED)
    if checking11[2][9]==1:
        C10.config(state=DISABLED)

    rootmovie1.mainloop()

def show12():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking12

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking12[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking12[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order12
        with open("Booking.txt","a") as f:
            f.write("Eternals Movie\n")
            f.write("Matinee Show--> 01:00 PM\n")
            f.write("Booking Number: "+str(order12)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking12[0][0]==1:
            A1.config(state=DISABLED)
        if checking12[0][1]==1:
            A2.config(state=DISABLED)
        if checking12[0][2]==1:
            A3.config(state=DISABLED)
        if checking12[0][3]==1:
            A4.config(state=DISABLED)
        if checking12[0][4]==1:
            A5.config(state=DISABLED)
        if checking12[0][5]==1:
            A6.config(state=DISABLED)
        if checking12[0][6]==1:
            A7.config(state=DISABLED)
        if checking12[0][7]==1:
            A8.config(state=DISABLED)
        if checking12[0][8]==1:
            A9.config(state=DISABLED)
        if checking12[0][9]==1:
            A10.config(state=DISABLED)
        if checking12[1][0]==1:
            B1.config(state=DISABLED)
        if checking12[1][1]==1:
            B2.config(state=DISABLED)
        if checking12[1][2]==1:
            B3.config(state=DISABLED)
        if checking12[1][3]==1:
            B4.config(state=DISABLED)
        if checking12[1][4]==1:
            B5.config(state=DISABLED)
        if checking12[1][5]==1:
            B6.config(state=DISABLED)
        if checking12[1][6]==1:
            B7.config(state=DISABLED)
        if checking12[1][7]==1:
            B8.config(state=DISABLED)
        if checking12[1][8]==1:
            B9.config(state=DISABLED)
        if checking12[1][9]==1:
            B10.config(state=DISABLED)
        if checking12[2][0]==1:
            C1.config(state=DISABLED)
        if checking12[2][1]==1:
            C2.config(state=DISABLED)
        if checking12[2][2]==1:
            C3.config(state=DISABLED)
        if checking12[2][3]==1:
            C4.config(state=DISABLED)
        if checking12[2][4]==1:
            C5.config(state=DISABLED)
        if checking12[2][5]==1:
            C6.config(state=DISABLED)
        if checking12[2][6]==1:
            C7.config(state=DISABLED)
        if checking12[2][7]==1:
            C8.config(state=DISABLED)
        if checking12[2][8]==1:
            C9.config(state=DISABLED)
        if checking12[2][9]==1:
            C10.config(state=DISABLED)
        
        order12=order12+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Eternals, 01:00 PM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking12[0][0]==1:
        A1.config(state=DISABLED)
    if checking12[0][1]==1:
        A2.config(state=DISABLED)
    if checking12[0][2]==1:
        A3.config(state=DISABLED)
    if checking12[0][3]==1:
        A4.config(state=DISABLED)
    if checking12[0][4]==1:
        A5.config(state=DISABLED)
    if checking12[0][5]==1:
        A6.config(state=DISABLED)
    if checking12[0][6]==1:
        A7.config(state=DISABLED)
    if checking12[0][7]==1:
        A8.config(state=DISABLED)
    if checking12[0][8]==1:
        A9.config(state=DISABLED)
    if checking12[0][9]==1:
        A10.config(state=DISABLED)
    if checking12[1][0]==1:
        B1.config(state=DISABLED)
    if checking12[1][1]==1:
        B2.config(state=DISABLED)
    if checking12[1][2]==1:
        B3.config(state=DISABLED)
    if checking12[1][3]==1:
        B4.config(state=DISABLED)
    if checking12[1][4]==1:
        B5.config(state=DISABLED)
    if checking12[1][5]==1:
        B6.config(state=DISABLED)
    if checking12[1][6]==1:
        B7.config(state=DISABLED)
    if checking12[1][7]==1:
        B8.config(state=DISABLED)
    if checking12[1][8]==1:
        B9.config(state=DISABLED)
    if checking12[1][9]==1:
        B10.config(state=DISABLED)
    if checking12[2][0]==1:
        C1.config(state=DISABLED)
    if checking12[2][1]==1:
        C2.config(state=DISABLED)
    if checking12[2][2]==1:
        C3.config(state=DISABLED)
    if checking12[2][3]==1:
        C4.config(state=DISABLED)
    if checking12[2][4]==1:
        C5.config(state=DISABLED)
    if checking12[2][5]==1:
        C6.config(state=DISABLED)
    if checking12[2][6]==1:
        C7.config(state=DISABLED)
    if checking12[2][7]==1:
        C8.config(state=DISABLED)
    if checking12[2][8]==1:
        C9.config(state=DISABLED)
    if checking12[2][9]==1:
        C10.config(state=DISABLED)

    rootmovie1.mainloop()

def show13():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking13

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking13[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking13[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order13
        with open("Booking.txt","a") as f:
            f.write("Eternals Movie\n")
            f.write("First Show--> 05:00 PM\n")
            f.write("Booking Number: "+str(order13)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking13[0][0]==1:
            A1.config(state=DISABLED)
        if checking13[0][1]==1:
            A2.config(state=DISABLED)
        if checking13[0][2]==1:
            A3.config(state=DISABLED)
        if checking13[0][3]==1:
            A4.config(state=DISABLED)
        if checking13[0][4]==1:
            A5.config(state=DISABLED)
        if checking13[0][5]==1:
            A6.config(state=DISABLED)
        if checking13[0][6]==1:
            A7.config(state=DISABLED)
        if checking13[0][7]==1:
            A8.config(state=DISABLED)
        if checking13[0][8]==1:
            A9.config(state=DISABLED)
        if checking13[0][9]==1:
            A10.config(state=DISABLED)
        if checking13[1][0]==1:
            B1.config(state=DISABLED)
        if checking13[1][1]==1:
            B2.config(state=DISABLED)
        if checking13[1][2]==1:
            B3.config(state=DISABLED)
        if checking13[1][3]==1:
            B4.config(state=DISABLED)
        if checking13[1][4]==1:
            B5.config(state=DISABLED)
        if checking13[1][5]==1:
            B6.config(state=DISABLED)
        if checking13[1][6]==1:
            B7.config(state=DISABLED)
        if checking13[1][7]==1:
            B8.config(state=DISABLED)
        if checking13[1][8]==1:
            B9.config(state=DISABLED)
        if checking13[1][9]==1:
            B10.config(state=DISABLED)
        if checking13[2][0]==1:
            C1.config(state=DISABLED)
        if checking13[2][1]==1:
            C2.config(state=DISABLED)
        if checking13[2][2]==1:
            C3.config(state=DISABLED)
        if checking13[2][3]==1:
            C4.config(state=DISABLED)
        if checking13[2][4]==1:
            C5.config(state=DISABLED)
        if checking13[2][5]==1:
            C6.config(state=DISABLED)
        if checking13[2][6]==1:
            C7.config(state=DISABLED)
        if checking13[2][7]==1:
            C8.config(state=DISABLED)
        if checking13[2][8]==1:
            C9.config(state=DISABLED)
        if checking13[2][9]==1:
            C10.config(state=DISABLED)
        
        order13=order13+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Eternals, 05:00 PM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking13[0][0]==1:
            A1.config(state=DISABLED)
    if checking13[0][1]==1:
        A2.config(state=DISABLED)
    if checking13[0][2]==1:
        A3.config(state=DISABLED)
    if checking13[0][3]==1:
        A4.config(state=DISABLED)
    if checking13[0][4]==1:
        A5.config(state=DISABLED)
    if checking13[0][5]==1:
        A6.config(state=DISABLED)
    if checking13[0][6]==1:
        A7.config(state=DISABLED)
    if checking13[0][7]==1:
        A8.config(state=DISABLED)
    if checking13[0][8]==1:
        A9.config(state=DISABLED)
    if checking13[0][9]==1:
        A10.config(state=DISABLED)
    if checking13[1][0]==1:
        B1.config(state=DISABLED)
    if checking13[1][1]==1:
        B2.config(state=DISABLED)
    if checking13[1][2]==1:
        B3.config(state=DISABLED)
    if checking13[1][3]==1:
        B4.config(state=DISABLED)
    if checking13[1][4]==1:
        B5.config(state=DISABLED)
    if checking13[1][5]==1:
        B6.config(state=DISABLED)
    if checking13[1][6]==1:
        B7.config(state=DISABLED)
    if checking13[1][7]==1:
        B8.config(state=DISABLED)
    if checking13[1][8]==1:
        B9.config(state=DISABLED)
    if checking13[1][9]==1:
        B10.config(state=DISABLED)
    if checking13[2][0]==1:
        C1.config(state=DISABLED)
    if checking13[2][1]==1:
        C2.config(state=DISABLED)
    if checking13[2][2]==1:
        C3.config(state=DISABLED)
    if checking13[2][3]==1:
        C4.config(state=DISABLED)
    if checking13[2][4]==1:
        C5.config(state=DISABLED)
    if checking13[2][5]==1:
        C6.config(state=DISABLED)
    if checking13[2][6]==1:
        C7.config(state=DISABLED)
    if checking13[2][7]==1:
        C8.config(state=DISABLED)
    if checking13[2][8]==1:
        C9.config(state=DISABLED)
    if checking13[2][9]==1:
        C10.config(state=DISABLED)


    rootmovie1.mainloop()

def show14():
    rootmovie1=Toplevel(master)
    global checking14
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking14[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking14[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order14
        with open("Booking.txt","a") as f:
            f.write("Eternals Movie\n")
            f.write("Second Show--> 09:00 PM\n")
            f.write("Booking Number: "+str(order14)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking14[0][0]==1:
            A1.config(state=DISABLED)
        if checking14[0][1]==1:
            A2.config(state=DISABLED)
        if checking14[0][2]==1:
            A3.config(state=DISABLED)
        if checking14[0][3]==1:
            A4.config(state=DISABLED)
        if checking14[0][4]==1:
            A5.config(state=DISABLED)
        if checking14[0][5]==1:
            A6.config(state=DISABLED)
        if checking14[0][6]==1:
            A7.config(state=DISABLED)
        if checking14[0][7]==1:
            A8.config(state=DISABLED)
        if checking14[0][8]==1:
            A9.config(state=DISABLED)
        if checking14[0][9]==1:
            A10.config(state=DISABLED)
        if checking14[1][0]==1:
            B1.config(state=DISABLED)
        if checking14[1][1]==1:
            B2.config(state=DISABLED)
        if checking14[1][2]==1:
            B3.config(state=DISABLED)
        if checking14[1][3]==1:
            B4.config(state=DISABLED)
        if checking14[1][4]==1:
            B5.config(state=DISABLED)
        if checking14[1][5]==1:
            B6.config(state=DISABLED)
        if checking14[1][6]==1:
            B7.config(state=DISABLED)
        if checking14[1][7]==1:
            B8.config(state=DISABLED)
        if checking14[1][8]==1:
            B9.config(state=DISABLED)
        if checking14[1][9]==1:
            B10.config(state=DISABLED)
        if checking14[2][0]==1:
            C1.config(state=DISABLED)
        if checking14[2][1]==1:
            C2.config(state=DISABLED)
        if checking14[2][2]==1:
            C3.config(state=DISABLED)
        if checking14[2][3]==1:
            C4.config(state=DISABLED)
        if checking14[2][4]==1:
            C5.config(state=DISABLED)
        if checking14[2][5]==1:
            C6.config(state=DISABLED)
        if checking14[2][6]==1:
            C7.config(state=DISABLED)
        if checking14[2][7]==1:
            C8.config(state=DISABLED)
        if checking14[2][8]==1:
            C9.config(state=DISABLED)
        if checking14[2][9]==1:
            C10.config(state=DISABLED)
        
        order14=order14+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Eternals, 09:00 PM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)
    if checking14[0][0]==1:
        A1.config(state=DISABLED)
    if checking14[0][1]==1:
        A2.config(state=DISABLED)
    if checking14[0][2]==1:
        A3.config(state=DISABLED)
    if checking14[0][3]==1:
        A4.config(state=DISABLED)
    if checking14[0][4]==1:
        A5.config(state=DISABLED)
    if checking14[0][5]==1:
        A6.config(state=DISABLED)
    if checking14[0][6]==1:
        A7.config(state=DISABLED)
    if checking14[0][7]==1:
        A8.config(state=DISABLED)
    if checking14[0][8]==1:
        A9.config(state=DISABLED)
    if checking14[0][9]==1:
        A10.config(state=DISABLED)
    if checking14[1][0]==1:
        B1.config(state=DISABLED)
    if checking14[1][1]==1:
        B2.config(state=DISABLED)
    if checking14[1][2]==1:
        B3.config(state=DISABLED)
    if checking14[1][3]==1:
        B4.config(state=DISABLED)
    if checking14[1][4]==1:
        B5.config(state=DISABLED)
    if checking14[1][5]==1:
        B6.config(state=DISABLED)
    if checking14[1][6]==1:
        B7.config(state=DISABLED)
    if checking14[1][7]==1:
        B8.config(state=DISABLED)
    if checking14[1][8]==1:
        B9.config(state=DISABLED)
    if checking14[1][9]==1:
        B10.config(state=DISABLED)
    if checking14[2][0]==1:
        C1.config(state=DISABLED)
    if checking14[2][1]==1:
        C2.config(state=DISABLED)
    if checking14[2][2]==1:
        C3.config(state=DISABLED)
    if checking14[2][3]==1:
        C4.config(state=DISABLED)
    if checking14[2][4]==1:
        C5.config(state=DISABLED)
    if checking14[2][5]==1:
        C6.config(state=DISABLED)
    if checking14[2][6]==1:
        C7.config(state=DISABLED)
    if checking14[2][7]==1:
        C8.config(state=DISABLED)
    if checking14[2][8]==1:
        C9.config(state=DISABLED)
    if checking14[2][9]==1:
        C10.config(state=DISABLED)

    rootmovie1.mainloop()

def show21():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking21

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking21[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking21[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order21
        with open("Booking.txt","a") as f:
            f.write("Venom Movie\n")
            f.write("Morning Show--> 11:00 AM\n")
            f.write("Booking Number: "+str(order21)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking21[0][0]==1:
            A1.config(state=DISABLED)
        if checking21[0][1]==1:
            A2.config(state=DISABLED)
        if checking21[0][2]==1:
            A3.config(state=DISABLED)
        if checking21[0][3]==1:
            A4.config(state=DISABLED)
        if checking21[0][4]==1:
            A5.config(state=DISABLED)
        if checking21[0][5]==1:
            A6.config(state=DISABLED)
        if checking21[0][6]==1:
            A7.config(state=DISABLED)
        if checking21[0][7]==1:
            A8.config(state=DISABLED)
        if checking21[0][8]==1:
            A9.config(state=DISABLED)
        if checking21[0][9]==1:
            A10.config(state=DISABLED)
        if checking21[1][0]==1:
            B1.config(state=DISABLED)
        if checking21[1][1]==1:
            B2.config(state=DISABLED)
        if checking21[1][2]==1:
            B3.config(state=DISABLED)
        if checking21[1][3]==1:
            B4.config(state=DISABLED)
        if checking21[1][4]==1:
            B5.config(state=DISABLED)
        if checking21[1][5]==1:
            B6.config(state=DISABLED)
        if checking21[1][6]==1:
            B7.config(state=DISABLED)
        if checking21[1][7]==1:
            B8.config(state=DISABLED)
        if checking21[1][8]==1:
            B9.config(state=DISABLED)
        if checking21[1][9]==1:
            B10.config(state=DISABLED)
        if checking21[2][0]==1:
            C1.config(state=DISABLED)
        if checking21[2][1]==1:
            C2.config(state=DISABLED)
        if checking21[2][2]==1:
            C3.config(state=DISABLED)
        if checking21[2][3]==1:
            C4.config(state=DISABLED)
        if checking21[2][4]==1:
            C5.config(state=DISABLED)
        if checking21[2][5]==1:
            C6.config(state=DISABLED)
        if checking21[2][6]==1:
            C7.config(state=DISABLED)
        if checking21[2][7]==1:
            C8.config(state=DISABLED)
        if checking21[2][8]==1:
            C9.config(state=DISABLED)
        if checking21[2][9]==1:
            C10.config(state=DISABLED)
        
        order21=order21+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Venom, 11:00 AM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking21[0][0]==1:
        A1.config(state=DISABLED)
    if checking21[0][1]==1:
        A2.config(state=DISABLED)
    if checking21[0][2]==1:
        A3.config(state=DISABLED)
    if checking21[0][3]==1:
        A4.config(state=DISABLED)
    if checking21[0][4]==1:
        A5.config(state=DISABLED)
    if checking21[0][5]==1:
        A6.config(state=DISABLED)
    if checking21[0][6]==1:
        A7.config(state=DISABLED)
    if checking21[0][7]==1:
        A8.config(state=DISABLED)
    if checking21[0][8]==1:
        A9.config(state=DISABLED)
    if checking21[0][9]==1:
        A10.config(state=DISABLED)
    if checking21[1][0]==1:
        B1.config(state=DISABLED)
    if checking21[1][1]==1:
        B2.config(state=DISABLED)
    if checking21[1][2]==1:
        B3.config(state=DISABLED)
    if checking21[1][3]==1:
        B4.config(state=DISABLED)
    if checking21[1][4]==1:
        B5.config(state=DISABLED)
    if checking21[1][5]==1:
        B6.config(state=DISABLED)
    if checking21[1][6]==1:
        B7.config(state=DISABLED)
    if checking21[1][7]==1:
        B8.config(state=DISABLED)
    if checking21[1][8]==1:
        B9.config(state=DISABLED)
    if checking21[1][9]==1:
        B10.config(state=DISABLED)
    if checking21[2][0]==1:
        C1.config(state=DISABLED)
    if checking21[2][1]==1:
        C2.config(state=DISABLED)
    if checking21[2][2]==1:
        C3.config(state=DISABLED)
    if checking21[2][3]==1:
        C4.config(state=DISABLED)
    if checking21[2][4]==1:
        C5.config(state=DISABLED)
    if checking21[2][5]==1:
        C6.config(state=DISABLED)
    if checking21[2][6]==1:
        C7.config(state=DISABLED)
    if checking21[2][7]==1:
        C8.config(state=DISABLED)
    if checking21[2][8]==1:
        C9.config(state=DISABLED)
    if checking21[2][9]==1:
        C10.config(state=DISABLED)


    rootmovie1.mainloop()

def show22():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking22

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking22[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking22[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order22
        with open("Booking.txt","a") as f:
            f.write("Venom Movie\n")
            f.write("Morning Show--> 01:00 PM\n")
            f.write("Booking Number: "+str(order22)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking22[0][0]==1:
            A1.config(state=DISABLED)
        if checking22[0][1]==1:
            A2.config(state=DISABLED)
        if checking22[0][2]==1:
            A3.config(state=DISABLED)
        if checking22[0][3]==1:
            A4.config(state=DISABLED)
        if checking22[0][4]==1:
            A5.config(state=DISABLED)
        if checking22[0][5]==1:
            A6.config(state=DISABLED)
        if checking22[0][6]==1:
            A7.config(state=DISABLED)
        if checking22[0][7]==1:
            A8.config(state=DISABLED)
        if checking22[0][8]==1:
            A9.config(state=DISABLED)
        if checking22[0][9]==1:
            A10.config(state=DISABLED)
        if checking22[1][0]==1:
            B1.config(state=DISABLED)
        if checking22[1][1]==1:
            B2.config(state=DISABLED)
        if checking22[1][2]==1:
            B3.config(state=DISABLED)
        if checking22[1][3]==1:
            B4.config(state=DISABLED)
        if checking22[1][4]==1:
            B5.config(state=DISABLED)
        if checking22[1][5]==1:
            B6.config(state=DISABLED)
        if checking22[1][6]==1:
            B7.config(state=DISABLED)
        if checking22[1][7]==1:
            B8.config(state=DISABLED)
        if checking22[1][8]==1:
            B9.config(state=DISABLED)
        if checking22[1][9]==1:
            B10.config(state=DISABLED)
        if checking22[2][0]==1:
            C1.config(state=DISABLED)
        if checking22[2][1]==1:
            C2.config(state=DISABLED)
        if checking22[2][2]==1:
            C3.config(state=DISABLED)
        if checking22[2][3]==1:
            C4.config(state=DISABLED)
        if checking22[2][4]==1:
            C5.config(state=DISABLED)
        if checking22[2][5]==1:
            C6.config(state=DISABLED)
        if checking22[2][6]==1:
            C7.config(state=DISABLED)
        if checking22[2][7]==1:
            C8.config(state=DISABLED)
        if checking22[2][8]==1:
            C9.config(state=DISABLED)
        if checking22[2][9]==1:
            C10.config(state=DISABLED)
        
        order22=order22+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Venom, 01:00 PM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking22[0][0]==1:
        A1.config(state=DISABLED)
    if checking22[0][1]==1:
        A2.config(state=DISABLED)
    if checking22[0][2]==1:
        A3.config(state=DISABLED)
    if checking22[0][3]==1:
        A4.config(state=DISABLED)
    if checking22[0][4]==1:
        A5.config(state=DISABLED)
    if checking22[0][5]==1:
        A6.config(state=DISABLED)
    if checking22[0][6]==1:
        A7.config(state=DISABLED)
    if checking22[0][7]==1:
        A8.config(state=DISABLED)
    if checking22[0][8]==1:
        A9.config(state=DISABLED)
    if checking22[0][9]==1:
        A10.config(state=DISABLED)
    if checking22[1][0]==1:
        B1.config(state=DISABLED)
    if checking22[1][1]==1:
        B2.config(state=DISABLED)
    if checking22[1][2]==1:
        B3.config(state=DISABLED)
    if checking22[1][3]==1:
        B4.config(state=DISABLED)
    if checking22[1][4]==1:
        B5.config(state=DISABLED)
    if checking22[1][5]==1:
        B6.config(state=DISABLED)
    if checking22[1][6]==1:
        B7.config(state=DISABLED)
    if checking22[1][7]==1:
        B8.config(state=DISABLED)
    if checking22[1][8]==1:
        B9.config(state=DISABLED)
    if checking22[1][9]==1:
        B10.config(state=DISABLED)
    if checking22[2][0]==1:
        C1.config(state=DISABLED)
    if checking22[2][1]==1:
        C2.config(state=DISABLED)
    if checking22[2][2]==1:
        C3.config(state=DISABLED)
    if checking22[2][3]==1:
        C4.config(state=DISABLED)
    if checking22[2][4]==1:
        C5.config(state=DISABLED)
    if checking22[2][5]==1:
        C6.config(state=DISABLED)
    if checking22[2][6]==1:
        C7.config(state=DISABLED)
    if checking22[2][7]==1:
        C8.config(state=DISABLED)
    if checking22[2][8]==1:
        C9.config(state=DISABLED)
    if checking22[2][9]==1:
        C10.config(state=DISABLED)

    rootmovie1.mainloop()

def show23():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking23

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking23[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking23[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order23
        with open("Booking.txt","a") as f:
            f.write("Venom Movie\n")
            f.write("Morning Show--> 05:00 PM\n")
            f.write("Booking Number: "+str(order23)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking23[0][0]==1:
            A1.config(state=DISABLED)
        if checking23[0][1]==1:
            A2.config(state=DISABLED)
        if checking23[0][2]==1:
            A3.config(state=DISABLED)
        if checking23[0][3]==1:
            A4.config(state=DISABLED)
        if checking23[0][4]==1:
            A5.config(state=DISABLED)
        if checking23[0][5]==1:
            A6.config(state=DISABLED)
        if checking23[0][6]==1:
            A7.config(state=DISABLED)
        if checking23[0][7]==1:
            A8.config(state=DISABLED)
        if checking23[0][8]==1:
            A9.config(state=DISABLED)
        if checking23[0][9]==1:
            A10.config(state=DISABLED)
        if checking23[1][0]==1:
            B1.config(state=DISABLED)
        if checking23[1][1]==1:
            B2.config(state=DISABLED)
        if checking23[1][2]==1:
            B3.config(state=DISABLED)
        if checking23[1][3]==1:
            B4.config(state=DISABLED)
        if checking23[1][4]==1:
            B5.config(state=DISABLED)
        if checking23[1][5]==1:
            B6.config(state=DISABLED)
        if checking23[1][6]==1:
            B7.config(state=DISABLED)
        if checking23[1][7]==1:
            B8.config(state=DISABLED)
        if checking23[1][8]==1:
            B9.config(state=DISABLED)
        if checking23[1][9]==1:
            B10.config(state=DISABLED)
        if checking23[2][0]==1:
            C1.config(state=DISABLED)
        if checking23[2][1]==1:
            C2.config(state=DISABLED)
        if checking23[2][2]==1:
            C3.config(state=DISABLED)
        if checking23[2][3]==1:
            C4.config(state=DISABLED)
        if checking23[2][4]==1:
            C5.config(state=DISABLED)
        if checking23[2][5]==1:
            C6.config(state=DISABLED)
        if checking23[2][6]==1:
            C7.config(state=DISABLED)
        if checking23[2][7]==1:
            C8.config(state=DISABLED)
        if checking23[2][8]==1:
            C9.config(state=DISABLED)
        if checking23[2][9]==1:
            C10.config(state=DISABLED)
        
        order23=order23+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Venom, 05:00 PM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking23[0][0]==1:
        A1.config(state=DISABLED)
    if checking23[0][1]==1:
        A2.config(state=DISABLED)
    if checking23[0][2]==1:
        A3.config(state=DISABLED)
    if checking23[0][3]==1:
        A4.config(state=DISABLED)
    if checking23[0][4]==1:
        A5.config(state=DISABLED)
    if checking23[0][5]==1:
        A6.config(state=DISABLED)
    if checking23[0][6]==1:
        A7.config(state=DISABLED)
    if checking23[0][7]==1:
        A8.config(state=DISABLED)
    if checking23[0][8]==1:
        A9.config(state=DISABLED)
    if checking23[0][9]==1:
        A10.config(state=DISABLED)
    if checking23[1][0]==1:
        B1.config(state=DISABLED)
    if checking23[1][1]==1:
        B2.config(state=DISABLED)
    if checking23[1][2]==1:
        B3.config(state=DISABLED)
    if checking23[1][3]==1:
        B4.config(state=DISABLED)
    if checking23[1][4]==1:
        B5.config(state=DISABLED)
    if checking23[1][5]==1:
        B6.config(state=DISABLED)
    if checking23[1][6]==1:
        B7.config(state=DISABLED)
    if checking23[1][7]==1:
        B8.config(state=DISABLED)
    if checking23[1][8]==1:
        B9.config(state=DISABLED)
    if checking23[1][9]==1:
        B10.config(state=DISABLED)
    if checking23[2][0]==1:
        C1.config(state=DISABLED)
    if checking23[2][1]==1:
        C2.config(state=DISABLED)
    if checking23[2][2]==1:
        C3.config(state=DISABLED)
    if checking23[2][3]==1:
        C4.config(state=DISABLED)
    if checking23[2][4]==1:
        C5.config(state=DISABLED)
    if checking23[2][5]==1:
        C6.config(state=DISABLED)
    if checking23[2][6]==1:
        C7.config(state=DISABLED)
    if checking23[2][7]==1:
        C8.config(state=DISABLED)
    if checking23[2][8]==1:
        C9.config(state=DISABLED)
    if checking23[2][9]==1:
        C10.config(state=DISABLED)

    rootmovie1.mainloop()

def show24():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking24

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking24[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking24[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order24
        with open("Booking.txt","a") as f:
            f.write("Venom Movie\n")
            f.write("Morning Show--> 09:00 PM\n")
            f.write("Booking Number: "+str(order24)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking24[0][0]==1:
            A1.config(state=DISABLED)
        if checking24[0][1]==1:
            A2.config(state=DISABLED)
        if checking24[0][2]==1:
            A3.config(state=DISABLED)
        if checking24[0][3]==1:
            A4.config(state=DISABLED)
        if checking24[0][4]==1:
            A5.config(state=DISABLED)
        if checking24[0][5]==1:
            A6.config(state=DISABLED)
        if checking24[0][6]==1:
            A7.config(state=DISABLED)
        if checking24[0][7]==1:
            A8.config(state=DISABLED)
        if checking24[0][8]==1:
            A9.config(state=DISABLED)
        if checking24[0][9]==1:
            A10.config(state=DISABLED)
        if checking24[1][0]==1:
            B1.config(state=DISABLED)
        if checking24[1][1]==1:
            B2.config(state=DISABLED)
        if checking24[1][2]==1:
            B3.config(state=DISABLED)
        if checking24[1][3]==1:
            B4.config(state=DISABLED)
        if checking24[1][4]==1:
            B5.config(state=DISABLED)
        if checking24[1][5]==1:
            B6.config(state=DISABLED)
        if checking24[1][6]==1:
            B7.config(state=DISABLED)
        if checking24[1][7]==1:
            B8.config(state=DISABLED)
        if checking24[1][8]==1:
            B9.config(state=DISABLED)
        if checking24[1][9]==1:
            B10.config(state=DISABLED)
        if checking24[2][0]==1:
            C1.config(state=DISABLED)
        if checking24[2][1]==1:
            C2.config(state=DISABLED)
        if checking24[2][2]==1:
            C3.config(state=DISABLED)
        if checking24[2][3]==1:
            C4.config(state=DISABLED)
        if checking24[2][4]==1:
            C5.config(state=DISABLED)
        if checking24[2][5]==1:
            C6.config(state=DISABLED)
        if checking24[2][6]==1:
            C7.config(state=DISABLED)
        if checking24[2][7]==1:
            C8.config(state=DISABLED)
        if checking24[2][8]==1:
            C9.config(state=DISABLED)
        if checking24[2][9]==1:
            C10.config(state=DISABLED)
        
        order24=order24+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Venom, 09:00 PM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking24[0][0]==1:
        A1.config(state=DISABLED)
    if checking24[0][1]==1:
        A2.config(state=DISABLED)
    if checking24[0][2]==1:
        A3.config(state=DISABLED)
    if checking24[0][3]==1:
        A4.config(state=DISABLED)
    if checking24[0][4]==1:
        A5.config(state=DISABLED)
    if checking24[0][5]==1:
        A6.config(state=DISABLED)
    if checking24[0][6]==1:
        A7.config(state=DISABLED)
    if checking24[0][7]==1:
        A8.config(state=DISABLED)
    if checking24[0][8]==1:
        A9.config(state=DISABLED)
    if checking24[0][9]==1:
        A10.config(state=DISABLED)
    if checking24[1][0]==1:
        B1.config(state=DISABLED)
    if checking24[1][1]==1:
        B2.config(state=DISABLED)
    if checking24[1][2]==1:
        B3.config(state=DISABLED)
    if checking24[1][3]==1:
        B4.config(state=DISABLED)
    if checking24[1][4]==1:
        B5.config(state=DISABLED)
    if checking24[1][5]==1:
        B6.config(state=DISABLED)
    if checking24[1][6]==1:
        B7.config(state=DISABLED)
    if checking24[1][7]==1:
        B8.config(state=DISABLED)
    if checking24[1][8]==1:
        B9.config(state=DISABLED)
    if checking24[1][9]==1:
        B10.config(state=DISABLED)
    if checking24[2][0]==1:
        C1.config(state=DISABLED)
    if checking24[2][1]==1:
        C2.config(state=DISABLED)
    if checking24[2][2]==1:
        C3.config(state=DISABLED)
    if checking24[2][3]==1:
        C4.config(state=DISABLED)
    if checking24[2][4]==1:
        C5.config(state=DISABLED)
    if checking24[2][5]==1:
        C6.config(state=DISABLED)
    if checking24[2][6]==1:
        C7.config(state=DISABLED)
    if checking24[2][7]==1:
        C8.config(state=DISABLED)
    if checking24[2][8]==1:
        C9.config(state=DISABLED)
    if checking24[2][9]==1:
        C10.config(state=DISABLED)

    rootmovie1.mainloop()

def show31():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking31

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking31[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking31[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order31
        with open("Booking.txt","a") as f:
            f.write("Shang-Chi Movie\n")
            f.write("Morning Show--> 11:00 AM\n")
            f.write("Booking Number: "+str(order31)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking31[0][0]==1:
            A1.config(state=DISABLED)
        if checking31[0][1]==1:
            A2.config(state=DISABLED)
        if checking31[0][2]==1:
            A3.config(state=DISABLED)
        if checking31[0][3]==1:
            A4.config(state=DISABLED)
        if checking31[0][4]==1:
            A5.config(state=DISABLED)
        if checking31[0][5]==1:
            A6.config(state=DISABLED)
        if checking31[0][6]==1:
            A7.config(state=DISABLED)
        if checking31[0][7]==1:
            A8.config(state=DISABLED)
        if checking31[0][8]==1:
            A9.config(state=DISABLED)
        if checking31[0][9]==1:
            A10.config(state=DISABLED)
        if checking31[1][0]==1:
            B1.config(state=DISABLED)
        if checking31[1][1]==1:
            B2.config(state=DISABLED)
        if checking31[1][2]==1:
            B3.config(state=DISABLED)
        if checking31[1][3]==1:
            B4.config(state=DISABLED)
        if checking31[1][4]==1:
            B5.config(state=DISABLED)
        if checking31[1][5]==1:
            B6.config(state=DISABLED)
        if checking31[1][6]==1:
            B7.config(state=DISABLED)
        if checking31[1][7]==1:
            B8.config(state=DISABLED)
        if checking31[1][8]==1:
            B9.config(state=DISABLED)
        if checking31[1][9]==1:
            B10.config(state=DISABLED)
        if checking31[2][0]==1:
            C1.config(state=DISABLED)
        if checking31[2][1]==1:
            C2.config(state=DISABLED)
        if checking31[2][2]==1:
            C3.config(state=DISABLED)
        if checking31[2][3]==1:
            C4.config(state=DISABLED)
        if checking31[2][4]==1:
            C5.config(state=DISABLED)
        if checking31[2][5]==1:
            C6.config(state=DISABLED)
        if checking31[2][6]==1:
            C7.config(state=DISABLED)
        if checking31[2][7]==1:
            C8.config(state=DISABLED)
        if checking31[2][8]==1:
            C9.config(state=DISABLED)
        if checking31[2][9]==1:
            C10.config(state=DISABLED)
        
        order31=order31+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Shang-Chi, 11:00 AM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking31[0][0]==1:
        A1.config(state=DISABLED)
    if checking31[0][1]==1:
        A2.config(state=DISABLED)
    if checking31[0][2]==1:
        A3.config(state=DISABLED)
    if checking31[0][3]==1:
        A4.config(state=DISABLED)
    if checking31[0][4]==1:
        A5.config(state=DISABLED)
    if checking31[0][5]==1:
        A6.config(state=DISABLED)
    if checking31[0][6]==1:
        A7.config(state=DISABLED)
    if checking31[0][7]==1:
        A8.config(state=DISABLED)
    if checking31[0][8]==1:
        A9.config(state=DISABLED)
    if checking31[0][9]==1:
        A10.config(state=DISABLED)
    if checking31[1][0]==1:
        B1.config(state=DISABLED)
    if checking31[1][1]==1:
        B2.config(state=DISABLED)
    if checking31[1][2]==1:
        B3.config(state=DISABLED)
    if checking31[1][3]==1:
        B4.config(state=DISABLED)
    if checking31[1][4]==1:
        B5.config(state=DISABLED)
    if checking31[1][5]==1:
        B6.config(state=DISABLED)
    if checking31[1][6]==1:
        B7.config(state=DISABLED)
    if checking31[1][7]==1:
        B8.config(state=DISABLED)
    if checking31[1][8]==1:
        B9.config(state=DISABLED)
    if checking31[1][9]==1:
        B10.config(state=DISABLED)
    if checking31[2][0]==1:
        C1.config(state=DISABLED)
    if checking31[2][1]==1:
        C2.config(state=DISABLED)
    if checking31[2][2]==1:
        C3.config(state=DISABLED)
    if checking31[2][3]==1:
        C4.config(state=DISABLED)
    if checking31[2][4]==1:
        C5.config(state=DISABLED)
    if checking31[2][5]==1:
        C6.config(state=DISABLED)
    if checking31[2][6]==1:
        C7.config(state=DISABLED)
    if checking31[2][7]==1:
        C8.config(state=DISABLED)
    if checking31[2][8]==1:
        C9.config(state=DISABLED)
    if checking31[2][9]==1:
        C10.config(state=DISABLED)

    rootmovie1.mainloop()

def show32():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking32

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking32[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking32[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order32
        with open("Booking.txt","a") as f:
            f.write("Shang-Chi Movie\n")
            f.write("Morning Show--> 01:00 PM\n")
            f.write("Booking Number: "+str(order32)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking32[0][0]==1:
            A1.config(state=DISABLED)
        if checking32[0][1]==1:
            A2.config(state=DISABLED)
        if checking32[0][2]==1:
            A3.config(state=DISABLED)
        if checking32[0][3]==1:
            A4.config(state=DISABLED)
        if checking32[0][4]==1:
            A5.config(state=DISABLED)
        if checking32[0][5]==1:
            A6.config(state=DISABLED)
        if checking32[0][6]==1:
            A7.config(state=DISABLED)
        if checking32[0][7]==1:
            A8.config(state=DISABLED)
        if checking32[0][8]==1:
            A9.config(state=DISABLED)
        if checking32[0][9]==1:
            A10.config(state=DISABLED)
        if checking32[1][0]==1:
            B1.config(state=DISABLED)
        if checking32[1][1]==1:
            B2.config(state=DISABLED)
        if checking32[1][2]==1:
            B3.config(state=DISABLED)
        if checking32[1][3]==1:
            B4.config(state=DISABLED)
        if checking32[1][4]==1:
            B5.config(state=DISABLED)
        if checking32[1][5]==1:
            B6.config(state=DISABLED)
        if checking32[1][6]==1:
            B7.config(state=DISABLED)
        if checking32[1][7]==1:
            B8.config(state=DISABLED)
        if checking32[1][8]==1:
            B9.config(state=DISABLED)
        if checking32[1][9]==1:
            B10.config(state=DISABLED)
        if checking32[2][0]==1:
            C1.config(state=DISABLED)
        if checking32[2][1]==1:
            C2.config(state=DISABLED)
        if checking32[2][2]==1:
            C3.config(state=DISABLED)
        if checking32[2][3]==1:
            C4.config(state=DISABLED)
        if checking32[2][4]==1:
            C5.config(state=DISABLED)
        if checking32[2][5]==1:
            C6.config(state=DISABLED)
        if checking32[2][6]==1:
            C7.config(state=DISABLED)
        if checking32[2][7]==1:
            C8.config(state=DISABLED)
        if checking32[2][8]==1:
            C9.config(state=DISABLED)
        if checking32[2][9]==1:
            C10.config(state=DISABLED)
        
        order32=order32+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Shang-Chi, 01:00 PM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking32[0][0]==1:
        A1.config(state=DISABLED)
    if checking32[0][1]==1:
        A2.config(state=DISABLED)
    if checking32[0][2]==1:
        A3.config(state=DISABLED)
    if checking32[0][3]==1:
        A4.config(state=DISABLED)
    if checking32[0][4]==1:
        A5.config(state=DISABLED)
    if checking32[0][5]==1:
        A6.config(state=DISABLED)
    if checking32[0][6]==1:
        A7.config(state=DISABLED)
    if checking32[0][7]==1:
        A8.config(state=DISABLED)
    if checking32[0][8]==1:
        A9.config(state=DISABLED)
    if checking32[0][9]==1:
        A10.config(state=DISABLED)
    if checking32[1][0]==1:
        B1.config(state=DISABLED)
    if checking32[1][1]==1:
        B2.config(state=DISABLED)
    if checking32[1][2]==1:
        B3.config(state=DISABLED)
    if checking32[1][3]==1:
        B4.config(state=DISABLED)
    if checking32[1][4]==1:
        B5.config(state=DISABLED)
    if checking32[1][5]==1:
        B6.config(state=DISABLED)
    if checking32[1][6]==1:
        B7.config(state=DISABLED)
    if checking32[1][7]==1:
        B8.config(state=DISABLED)
    if checking32[1][8]==1:
        B9.config(state=DISABLED)
    if checking32[1][9]==1:
        B10.config(state=DISABLED)
    if checking32[2][0]==1:
        C1.config(state=DISABLED)
    if checking32[2][1]==1:
        C2.config(state=DISABLED)
    if checking32[2][2]==1:
        C3.config(state=DISABLED)
    if checking32[2][3]==1:
        C4.config(state=DISABLED)
    if checking32[2][4]==1:
        C5.config(state=DISABLED)
    if checking32[2][5]==1:
        C6.config(state=DISABLED)
    if checking32[2][6]==1:
        C7.config(state=DISABLED)
    if checking32[2][7]==1:
        C8.config(state=DISABLED)
    if checking32[2][8]==1:
        C9.config(state=DISABLED)
    if checking32[2][9]==1:
        C10.config(state=DISABLED)

    rootmovie1.mainloop()

def show33():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking33

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking33[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking33[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order33
        with open("Booking.txt","a") as f:
            f.write("Shang-Chi Movie\n")
            f.write("Morning Show--> 05:00 PM\n")
            f.write("Booking Number: "+str(order33)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking33[0][0]==1:
            A1.config(state=DISABLED)
        if checking33[0][1]==1:
            A2.config(state=DISABLED)
        if checking33[0][2]==1:
            A3.config(state=DISABLED)
        if checking33[0][3]==1:
            A4.config(state=DISABLED)
        if checking33[0][4]==1:
            A5.config(state=DISABLED)
        if checking33[0][5]==1:
            A6.config(state=DISABLED)
        if checking33[0][6]==1:
            A7.config(state=DISABLED)
        if checking33[0][7]==1:
            A8.config(state=DISABLED)
        if checking33[0][8]==1:
            A9.config(state=DISABLED)
        if checking33[0][9]==1:
            A10.config(state=DISABLED)
        if checking33[1][0]==1:
            B1.config(state=DISABLED)
        if checking33[1][1]==1:
            B2.config(state=DISABLED)
        if checking33[1][2]==1:
            B3.config(state=DISABLED)
        if checking33[1][3]==1:
            B4.config(state=DISABLED)
        if checking33[1][4]==1:
            B5.config(state=DISABLED)
        if checking33[1][5]==1:
            B6.config(state=DISABLED)
        if checking33[1][6]==1:
            B7.config(state=DISABLED)
        if checking33[1][7]==1:
            B8.config(state=DISABLED)
        if checking33[1][8]==1:
            B9.config(state=DISABLED)
        if checking33[1][9]==1:
            B10.config(state=DISABLED)
        if checking33[2][0]==1:
            C1.config(state=DISABLED)
        if checking33[2][1]==1:
            C2.config(state=DISABLED)
        if checking33[2][2]==1:
            C3.config(state=DISABLED)
        if checking33[2][3]==1:
            C4.config(state=DISABLED)
        if checking33[2][4]==1:
            C5.config(state=DISABLED)
        if checking33[2][5]==1:
            C6.config(state=DISABLED)
        if checking33[2][6]==1:
            C7.config(state=DISABLED)
        if checking33[2][7]==1:
            C8.config(state=DISABLED)
        if checking33[2][8]==1:
            C9.config(state=DISABLED)
        if checking33[2][9]==1:
            C10.config(state=DISABLED)
        
        order33=order33+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Shang-Chi, 05:00 PM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking33[0][0]==1:
        A1.config(state=DISABLED)
    if checking33[0][1]==1:
        A2.config(state=DISABLED)
    if checking33[0][2]==1:
        A3.config(state=DISABLED)
    if checking33[0][3]==1:
        A4.config(state=DISABLED)
    if checking33[0][4]==1:
        A5.config(state=DISABLED)
    if checking33[0][5]==1:
        A6.config(state=DISABLED)
    if checking33[0][6]==1:
        A7.config(state=DISABLED)
    if checking33[0][7]==1:
        A8.config(state=DISABLED)
    if checking33[0][8]==1:
        A9.config(state=DISABLED)
    if checking33[0][9]==1:
        A10.config(state=DISABLED)
    if checking33[1][0]==1:
        B1.config(state=DISABLED)
    if checking33[1][1]==1:
        B2.config(state=DISABLED)
    if checking33[1][2]==1:
        B3.config(state=DISABLED)
    if checking33[1][3]==1:
        B4.config(state=DISABLED)
    if checking33[1][4]==1:
        B5.config(state=DISABLED)
    if checking33[1][5]==1:
        B6.config(state=DISABLED)
    if checking33[1][6]==1:
        B7.config(state=DISABLED)
    if checking33[1][7]==1:
        B8.config(state=DISABLED)
    if checking33[1][8]==1:
        B9.config(state=DISABLED)
    if checking33[1][9]==1:
        B10.config(state=DISABLED)
    if checking33[2][0]==1:
        C1.config(state=DISABLED)
    if checking33[2][1]==1:
        C2.config(state=DISABLED)
    if checking33[2][2]==1:
        C3.config(state=DISABLED)
    if checking33[2][3]==1:
        C4.config(state=DISABLED)
    if checking33[2][4]==1:
        C5.config(state=DISABLED)
    if checking33[2][5]==1:
        C6.config(state=DISABLED)
    if checking33[2][6]==1:
        C7.config(state=DISABLED)
    if checking33[2][7]==1:
        C8.config(state=DISABLED)
    if checking33[2][8]==1:
        C9.config(state=DISABLED)
    if checking33[2][9]==1:
        C10.config(state=DISABLED)

    rootmovie1.mainloop()

def show34():
    rootmovie1=Toplevel(master)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get(),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking34

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking34[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking34[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)

        e=final.get()
        e="Final checkout amount: "+str(len(ticket)*150)
        final.set(e)

        global order34
        with open("Booking.txt","a") as f:
            f.write("Shang-Chi Movie\n")
            f.write("Morning Show--> 09:00 PM\n")
            f.write("Booking Number: "+str(order34)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking34[0][0]==1:
            A1.config(state=DISABLED)
        if checking34[0][1]==1:
            A2.config(state=DISABLED)
        if checking34[0][2]==1:
            A3.config(state=DISABLED)
        if checking34[0][3]==1:
            A4.config(state=DISABLED)
        if checking34[0][4]==1:
            A5.config(state=DISABLED)
        if checking34[0][5]==1:
            A6.config(state=DISABLED)
        if checking34[0][6]==1:
            A7.config(state=DISABLED)
        if checking34[0][7]==1:
            A8.config(state=DISABLED)
        if checking34[0][8]==1:
            A9.config(state=DISABLED)
        if checking34[0][9]==1:
            A10.config(state=DISABLED)
        if checking34[1][0]==1:
            B1.config(state=DISABLED)
        if checking34[1][1]==1:
            B2.config(state=DISABLED)
        if checking34[1][2]==1:
            B3.config(state=DISABLED)
        if checking34[1][3]==1:
            B4.config(state=DISABLED)
        if checking34[1][4]==1:
            B5.config(state=DISABLED)
        if checking34[1][5]==1:
            B6.config(state=DISABLED)
        if checking34[1][6]==1:
            B7.config(state=DISABLED)
        if checking34[1][7]==1:
            B8.config(state=DISABLED)
        if checking34[1][8]==1:
            B9.config(state=DISABLED)
        if checking34[1][9]==1:
            B10.config(state=DISABLED)
        if checking34[2][0]==1:
            C1.config(state=DISABLED)
        if checking34[2][1]==1:
            C2.config(state=DISABLED)
        if checking34[2][2]==1:
            C3.config(state=DISABLED)
        if checking34[2][3]==1:
            C4.config(state=DISABLED)
        if checking34[2][4]==1:
            C5.config(state=DISABLED)
        if checking34[2][5]==1:
            C6.config(state=DISABLED)
        if checking34[2][6]==1:
            C7.config(state=DISABLED)
        if checking34[2][7]==1:
            C8.config(state=DISABLED)
        if checking34[2][8]==1:
            C9.config(state=DISABLED)
        if checking34[2][9]==1:
            C10.config(state=DISABLED)
        
        order34=order34+1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")
        final.set("Final checkout amount: 0")    

    
    # -------------------------------------------------------------
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_text(520,20,text="Shang-Chi, 09:00 PM")
    canvas.create_text(300,60,text="Screen here, Watch Out!",font="32")

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

    A1=Checkbutton(rootmovie1,text="A1",variable=A_1)
    A2=Checkbutton(rootmovie1,text="A2",variable=A_2)
    A3=Checkbutton(rootmovie1,text="A3",variable=A_3)
    A4=Checkbutton(rootmovie1,text="A4",variable=A_4)
    A5=Checkbutton(rootmovie1,text="A5",variable=A_5)
    A6=Checkbutton(rootmovie1,text="A6",variable=A_6)
    A7=Checkbutton(rootmovie1,text="A7",variable=A_7)
    A8=Checkbutton(rootmovie1,text="A8",variable=A_8)
    A9=Checkbutton(rootmovie1,text="A9",variable=A_9)
    A10=Checkbutton(rootmovie1,text="A10",variable=A_10)

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

    B1=Checkbutton(rootmovie1,text="B1",variable=B_1)
    B2=Checkbutton(rootmovie1,text="B2",variable=B_2)
    B3=Checkbutton(rootmovie1,text="B3",variable=B_3)
    B4=Checkbutton(rootmovie1,text="B4",variable=B_4)
    B5=Checkbutton(rootmovie1,text="B5",variable=B_5)
    B6=Checkbutton(rootmovie1,text="B6",variable=B_6)
    B7=Checkbutton(rootmovie1,text="B7",variable=B_7)
    B8=Checkbutton(rootmovie1,text="B8",variable=B_8)
    B9=Checkbutton(rootmovie1,text="B9",variable=B_9)
    B10=Checkbutton(rootmovie1,text="B10",variable=B_10)

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

    C1=Checkbutton(rootmovie1,text="C1",variable=C_1)
    C2=Checkbutton(rootmovie1,text="C2",variable=C_2)
    C3=Checkbutton(rootmovie1,text="C3",variable=C_3)
    C4=Checkbutton(rootmovie1,text="C4",variable=C_4)
    C5=Checkbutton(rootmovie1,text="C5",variable=C_5)
    C6=Checkbutton(rootmovie1,text="C6",variable=C_6)
    C7=Checkbutton(rootmovie1,text="C7",variable=C_7)
    C8=Checkbutton(rootmovie1,text="C8",variable=C_8)
    C9=Checkbutton(rootmovie1,text="C9",variable=C_9)
    C10=Checkbutton(rootmovie1,text="C10",variable=C_10)

    C1.place(x=10,y=260)
    C2.place(x=70,y=260)
    C3.place(x=130,y=260)
    C4.place(x=190,y=260)
    C5.place(x=250,y=260)
    C6.place(x=310,y=260)
    C7.place(x=370,y=260)
    C8.place(x=430,y=260)
    C9.place(x=490,y=260)
    C10.place(x=545,y=260)

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=350)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=380,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=400,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=425)
    final=StringVar()
    final.set("Final checkout amount: 0")
    finalamount=Label(rootmovie1,textvariable=final).place(x=220,y=480)

    if checking34[0][0]==1:
        A1.config(state=DISABLED)
    if checking34[0][1]==1:
        A2.config(state=DISABLED)
    if checking34[0][2]==1:
        A3.config(state=DISABLED)
    if checking34[0][3]==1:
        A4.config(state=DISABLED)
    if checking34[0][4]==1:
        A5.config(state=DISABLED)
    if checking34[0][5]==1:
        A6.config(state=DISABLED)
    if checking34[0][6]==1:
        A7.config(state=DISABLED)
    if checking34[0][7]==1:
        A8.config(state=DISABLED)
    if checking34[0][8]==1:
        A9.config(state=DISABLED)
    if checking34[0][9]==1:
        A10.config(state=DISABLED)
    if checking34[1][0]==1:
        B1.config(state=DISABLED)
    if checking34[1][1]==1:
        B2.config(state=DISABLED)
    if checking34[1][2]==1:
        B3.config(state=DISABLED)
    if checking34[1][3]==1:
        B4.config(state=DISABLED)
    if checking34[1][4]==1:
        B5.config(state=DISABLED)
    if checking34[1][5]==1:
        B6.config(state=DISABLED)
    if checking34[1][6]==1:
        B7.config(state=DISABLED)
    if checking34[1][7]==1:
        B8.config(state=DISABLED)
    if checking34[1][8]==1:
        B9.config(state=DISABLED)
    if checking34[1][9]==1:
        B10.config(state=DISABLED)
    if checking34[2][0]==1:
        C1.config(state=DISABLED)
    if checking34[2][1]==1:
        C2.config(state=DISABLED)
    if checking34[2][2]==1:
        C3.config(state=DISABLED)
    if checking34[2][3]==1:
        C4.config(state=DISABLED)
    if checking34[2][4]==1:
        C5.config(state=DISABLED)
    if checking34[2][5]==1:
        C6.config(state=DISABLED)
    if checking34[2][6]==1:
        C7.config(state=DISABLED)
    if checking34[2][7]==1:
        C8.config(state=DISABLED)
    if checking34[2][8]==1:
        C9.config(state=DISABLED)
    if checking34[2][9]==1:
        C10.config(state=DISABLED)


    rootmovie1.mainloop()

def offer():

    root=Toplevel(master)
    root.geometry("600x600")
    root.title("Offers")
    root.resizable(False,False)
    root.config(pady=150)

    Label(root,text="Buy a Movie-Pass at just Rs.90 and avail cashback of Rs.50 per each movie ticket you buy using this account for upcoming 3 MARVEL MOVIES.",font="Robotto 10 bold" ,wraplength=400).pack(pady=20)

    Label(root,text="Avail Rs.50 cashback on your first transaction via LAZY Pay.",font="Robotto 10 bold").pack(pady=20)
    Label(root,text="Avail cashback upto Rs.150 on your first transaction via Amazon Pay.",font="Robotto 10 bold").pack(pady=20)
    Label(root,text="Use SBI premium card to avail 20 percent off on your payment on mobile app or web. ",font="Robotto 10 bold").pack(pady=20)

    root.mainloop()

def upcoming():

    root=Toplevel(master)
    root.title("Upcoming Movies")
    root.geometry("600x600")
    root.config(pady=100,padx=200)

    movie1 = Image.open(r"Multi Screen Movie Booking\thumb-1920-1159896.jpg")
    movie1 = movie1.resize((192, 108))
    testmovie1 = ImageTk.PhotoImage(movie1)
    movielabel1 = tkinter.Label(root,image=testmovie1)
    movielabel1.image = testmovie1
    movielabel1.grid(column=5,row=2,rowspan=5,pady=10)

    movie2 = Image.open(r"Multi Screen Movie Booking\thor_love_and_thunder_fanart_2021_4k_hd_thor_love_and_thunder.jpg")
    movie2 = movie2.resize((192, 108))
    testmovie2 = ImageTk.PhotoImage(movie2)
    movielabel2 = tkinter.Label(root,image=testmovie2)
    movielabel2.image = testmovie2
    movielabel2.grid(column=5,row=10,rowspan=5,pady=10)

    movie3 = Image.open(r"Multi Screen Movie Booking\doctor-strange.jpg")
    movie3 = movie3.resize((192, 108))
    testmovie3 = ImageTk.PhotoImage(movie3)
    movielabel3 = tkinter.Label(root,image=testmovie3)
    movielabel3.image = testmovie3
    movielabel3.grid(column=5,row=18,rowspan=5,pady=10)

    root.mainloop()

master=Tk()
master.title("Marvel Movies")
master.geometry("720x600")
master.resizable(False,False)
master.config(padx=90)
master.eval('tk::PlaceWindow . center')

topmenu=Menu(master)
topmenu.add_command(label="Offers",command=offer)
topmenu.add_command(label="Upcoming Movies",command=upcoming)
master.config(menu=topmenu)

Label(master,text="Marvel Movies",font="Robotto 32",justify=CENTER).grid(row=0,column=1,columnspan=5,pady=30)

movie1 = Image.open(r'Multi Screen Movie Booking\052421_Eternals-teaser_01.jpg')
movie1 = movie1.resize((192, 108))
testmovie1 = ImageTk.PhotoImage(movie1)
movielabel1 = tkinter.Label(image=testmovie1)
movielabel1.image = testmovie1
movielabel1.grid(column=5,row=2,rowspan=5,padx=10)

movie1button1=Button(master, text="11:00 AM",command=show11).grid(row=4,column=1,padx=10)
movie1button2=Button(master, text="01:00 PM",command=show12).grid(row=4,column=2,padx=10)
movie1button3=Button(master, text="05:00 PM",command=show13).grid(row=4,column=3,padx=10)
movie1button4=Button(master, text="09:00 PM",command=show14).grid(row=4,column=4,padx=10)

movie2 = Image.open(r"Multi Screen Movie Booking\Venom-Let-There-Be-Carnage-Featured-New.jpg")
movie2 = movie2.resize((192, 108))
testmovie2 = ImageTk.PhotoImage(movie2)
movielabel2 = tkinter.Label(image=testmovie2)
movielabel2.image = testmovie2
movielabel2.grid(column=5,row=10,rowspan=5,padx=10)

movie2button1=Button(master, text="11:00 AM",command=show21).grid(row=12,column=1,padx=10)
movie2button2=Button(master, text="01:00 PM",command=show22).grid(row=12,column=2,padx=10)
movie2button3=Button(master, text="05:00 PM",command=show23).grid(row=12,column=3,padx=10)
movie2button4=Button(master, text="09:00 PM",command=show24).grid(row=12,column=4,padx=10)

movie3 = Image.open(r"Multi Screen Movie Booking\Shang-Chi-And-The-Legend-Of-The-Ten-Rings-Header-2.jpg")
movie3 = movie3.resize((192, 108))
testmovie3 = ImageTk.PhotoImage(movie3)
movielabel3 = tkinter.Label(image=testmovie3)
movielabel3.image = testmovie3
movielabel3.grid(column=5,row=18,rowspan=5,padx=10)

movie3button1=Button(master, text="11:00 AM",command=show31).grid(row=20,column=1,padx=10)
movie3button2=Button(master, text="01:00 PM",command=show32).grid(row=20,column=2,padx=10)
movie3button3=Button(master, text="05:00 PM",command=show33).grid(row=20,column=3,padx=10)
movie3button4=Button(master, text="09:00 PM",command=show34).grid(row=20,column=4,padx=10)

Label(master,text="You can add snacks during your checkout!").grid(row=25,column=1,columnspan=5,pady=10)
Label(master,text="Do checkout offers and cashbacks section to save your money.").grid(row=26,column=1,columnspan=5,pady=10)

checking11=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking12=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking13=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking14=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
order11=1
order12=1
order13=1
order14=1
checking21=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking22=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking23=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking24=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
order21=1
order22=1
order23=1
order24=1
checking31=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking32=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking33=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking34=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
order31=1
order32=1
order33=1
order34=1

master.mainloop()