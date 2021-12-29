from tkinter import *
from datetime import datetime

def show1():
    rootmovie1=Toplevel(window)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),   A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get   (),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.   get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

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
            f.write("Morning Show--> 11:00 AM\n")
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
    
    rootmovie1.title("Book Your Tickets")
    rootmovie1.geometry("600x600")
    rootmovie1.resizable(False, False) 

    canvas = Canvas(rootmovie1,height=120,width=600,)    
    canvas.place(x=0,y=0)
    canvas.create_rectangle(
        0, 0, 600, 120,
        outline="#fb0",
        fill="#fb0")
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
    rootmovie1.mainloop()   
    
def show2():
    rootmovie1=Toplevel(window)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),   A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get   (),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.   get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking2

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking2[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking2[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)
        global order2
        with open("Booking.txt","a") as f:
            f.write("Matinee Show--> 01:00 PM\n")
            f.write("Booking Number: "+str(order2)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking2[0][0]==1:
            A1.config(state=DISABLED)
        if checking2[0][1]==1:
            A2.config(state=DISABLED)
        if checking2[0][2]==1:
            A3.config(state=DISABLED)
        if checking2[0][3]==1:
            A4.config(state=DISABLED)
        if checking2[0][4]==1:
            A5.config(state=DISABLED)
        if checking2[0][5]==1:
            A6.config(state=DISABLED)
        if checking2[0][6]==1:
            A7.config(state=DISABLED)
        if checking2[0][7]==1:
            A8.config(state=DISABLED)
        if checking2[0][8]==1:
            A9.config(state=DISABLED)
        if checking2[0][9]==1:
            A10.config(state=DISABLED)
        if checking2[1][0]==1:
            B1.config(state=DISABLED)
        if checking2[1][1]==1:
            B2.config(state=DISABLED)
        if checking2[1][2]==1:
            B3.config(state=DISABLED)
        if checking2[1][3]==1:
            B4.config(state=DISABLED)
        if checking2[1][4]==1:
            B5.config(state=DISABLED)
        if checking2[1][5]==1:
            B6.config(state=DISABLED)
        if checking2[1][6]==1:
            B7.config(state=DISABLED)
        if checking2[1][7]==1:
            B8.config(state=DISABLED)
        if checking2[1][8]==1:
            B9.config(state=DISABLED)
        if checking2[1][9]==1:
            B10.config(state=DISABLED)
        if checking2[2][0]==1:
            C1.config(state=DISABLED)
        if checking2[2][1]==1:
            C2.config(state=DISABLED)
        if checking2[2][2]==1:
            C3.config(state=DISABLED)
        if checking2[2][3]==1:
            C4.config(state=DISABLED)
        if checking2[2][4]==1:
            C5.config(state=DISABLED)
        if checking2[2][5]==1:
            C6.config(state=DISABLED)
        if checking2[2][6]==1:
            C7.config(state=DISABLED)
        if checking2[2][7]==1:
            C8.config(state=DISABLED)
        if checking2[2][8]==1:
            C9.config(state=DISABLED)
        if checking2[2][9]==1:
            C10.config(state=DISABLED)

        order2+=1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")

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

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=300)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=340,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=370,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=410)
    rootmovie1.mainloop()   

def show3():
    rootmovie1=Toplevel(window)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),   A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get   (),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.   get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking3

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking3[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking3[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)
        global order3
        with open("Booking.txt","a") as f:
            f.write("First Show--> 5:00 PM\n")
            f.write("Booking Number: "+str(order3)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking3[0][0]==1:
            A1.config(state=DISABLED)
        if checking3[0][1]==1:
            A2.config(state=DISABLED)
        if checking3[0][2]==1:
            A3.config(state=DISABLED)
        if checking3[0][3]==1:
            A4.config(state=DISABLED)
        if checking3[0][4]==1:
            A5.config(state=DISABLED)
        if checking3[0][5]==1:
            A6.config(state=DISABLED)
        if checking3[0][6]==1:
            A7.config(state=DISABLED)
        if checking3[0][7]==1:
            A8.config(state=DISABLED)
        if checking3[0][8]==1:
            A9.config(state=DISABLED)
        if checking3[0][9]==1:
            A10.config(state=DISABLED)
        if checking3[1][0]==1:
            B1.config(state=DISABLED)
        if checking3[1][1]==1:
            B2.config(state=DISABLED)
        if checking3[1][2]==1:
            B3.config(state=DISABLED)
        if checking3[1][3]==1:
            B4.config(state=DISABLED)
        if checking3[1][4]==1:
            B5.config(state=DISABLED)
        if checking3[1][5]==1:
            B6.config(state=DISABLED)
        if checking3[1][6]==1:
            B7.config(state=DISABLED)
        if checking3[1][7]==1:
            B8.config(state=DISABLED)
        if checking3[1][8]==1:
            B9.config(state=DISABLED)
        if checking3[1][9]==1:
            B10.config(state=DISABLED)
        if checking3[2][0]==1:
            C1.config(state=DISABLED)
        if checking3[2][1]==1:
            C2.config(state=DISABLED)
        if checking3[2][2]==1:
            C3.config(state=DISABLED)
        if checking3[2][3]==1:
            C4.config(state=DISABLED)
        if checking3[2][4]==1:
            C5.config(state=DISABLED)
        if checking3[2][5]==1:
            C6.config(state=DISABLED)
        if checking3[2][6]==1:
            C7.config(state=DISABLED)
        if checking3[2][7]==1:
            C8.config(state=DISABLED)
        if checking3[2][8]==1:
            C9.config(state=DISABLED)
        if checking3[2][9]==1:
            C10.config(state=DISABLED)

        order3+=1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")

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

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=300)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=340,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=370,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=410)
    rootmovie1.mainloop()   

def show4():
    rootmovie1=Toplevel(window)
    
    def book():
        listy=[
            [A_1.get(),A_2.get(),A_3.get(),A_4.get(),A_5.get(),A_6.get(),A_7.get(),A_8.get(),   A_9.get(),A_10.get()],[B_1.get(),B_2.get(),B_3.get(),B_4.get(),B_5.get(),B_6.get   (),B_7.get(),B_8.get(),B_9.get(),B_10.get()],[C_1.get(),C_2.get(),C_3.get(),C_4.   get(),C_5.get(),C_6.get(),C_7.get(),C_8.get(),C_9.get(),C_10.get()] ]

        global checking4

        ticket=[]
        val=" "

        for j in range(len(listy)):
            for i in range(len(listy[j])):
                if listy[j][i]==1 and checking4[j][i]==0:
                    if j==0:
                        val="A"
                    elif j==1:
                        val="B"    
                    elif j==2:
                        val="C"
                    ticket.append(str(val+str(i+1)))
                    checking4[j][i]=1 

        stringy=""
        for item in ticket:
            stringy=stringy+item+" "

        c=numtic.get()
        c="Number of Tickets Booked: "+str(len(ticket))
        numtic.set(c)   

        d=ticnum.get()
        d="Tickets Booked are: "+stringy
        ticnum.set(d)
        global order4
        with open("Booking.txt","a") as f:
            f.write("Second Show--> 09:00 PM\n")
            f.write("Booking Number: "+str(order4)+"\n")
            f.write(f"{datetime.now().strftime('%Y/%m/%d %I:%M:%S')}\n")
            f.write(c+"\n")
            f.write(d+"\n")
            f.write("\n")

        if checking4[0][0]==1:
            A1.config(state=DISABLED)
        if checking4[0][1]==1:
            A2.config(state=DISABLED)
        if checking4[0][2]==1:
            A3.config(state=DISABLED)
        if checking4[0][3]==1:
            A4.config(state=DISABLED)
        if checking4[0][4]==1:
            A5.config(state=DISABLED)
        if checking4[0][5]==1:
            A6.config(state=DISABLED)
        if checking4[0][6]==1:
            A7.config(state=DISABLED)
        if checking4[0][7]==1:
            A8.config(state=DISABLED)
        if checking4[0][8]==1:
            A9.config(state=DISABLED)
        if checking4[0][9]==1:
            A10.config(state=DISABLED)
        if checking4[1][0]==1:
            B1.config(state=DISABLED)
        if checking4[1][1]==1:
            B2.config(state=DISABLED)
        if checking4[1][2]==1:
            B3.config(state=DISABLED)
        if checking4[1][3]==1:
            B4.config(state=DISABLED)
        if checking4[1][4]==1:
            B5.config(state=DISABLED)
        if checking4[1][5]==1:
            B6.config(state=DISABLED)
        if checking4[1][6]==1:
            B7.config(state=DISABLED)
        if checking4[1][7]==1:
            B8.config(state=DISABLED)
        if checking4[1][8]==1:
            B9.config(state=DISABLED)
        if checking4[1][9]==1:
            B10.config(state=DISABLED)
        if checking4[2][0]==1:
            C1.config(state=DISABLED)
        if checking4[2][1]==1:
            C2.config(state=DISABLED)
        if checking4[2][2]==1:
            C3.config(state=DISABLED)
        if checking4[2][3]==1:
            C4.config(state=DISABLED)
        if checking4[2][4]==1:
            C5.config(state=DISABLED)
        if checking4[2][5]==1:
            C6.config(state=DISABLED)
        if checking4[2][6]==1:
            C7.config(state=DISABLED)
        if checking4[2][7]==1:
            C8.config(state=DISABLED)
        if checking4[2][8]==1:
            C9.config(state=DISABLED)
        if checking4[2][9]==1:
            C10.config(state=DISABLED)

        order4+=1

    def newbook():
        numtic.set("Number of Tickets Booked: 0")
        ticnum.set("")

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

    book=Button(rootmovie1,text="BOOK NOW!",command=book).place(x=250,y=300)

    numtic=StringVar()
    numtic.set("Number of Tickets Booked: 0")
    ticnum=StringVar()

    noftic=Label(rootmovie1,textvariable=numtic).place(y=340,x=210)
    ticno=Label(rootmovie1,textvariable=ticnum).place(y=370,x=220)

    book=Button(rootmovie1,text="New Booking!",command=newbook).place(x=245,y=410)
    rootmovie1.mainloop()   

window=Tk()
window.title("Show Timings")
window.geometry("600x600")
window.resizable(False,False)
window.eval('tk::PlaceWindow . center')

label=Label(window,text="Marvel Screens",font="Robotto 24 bold").pack(pady=20,side=TOP)

checking=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking2=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking3=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
checking4=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
order=1
order2=1
order3=1
order4=1

button1=Button(window, text="11:00 AM",command=show1).pack(side=LEFT,anchor=N,padx=20)
button2=Button(window, text="1:00 PM",command=show2).pack(side=LEFT,anchor=N,padx=20)
button3=Button(window, text="5:00 PM",command=show3).pack(side=LEFT,anchor=N,padx=20)
button4=Button(window, text="9:00 AM",command=show4).pack(side=LEFT,anchor=N,padx=20)

window.mainloop()