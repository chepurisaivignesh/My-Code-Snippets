from tkinter import *
from tkinter import font
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# def savey():
#     with open("tiffin.txt","a") as f:
#         f.write(f'''
#         Order Number:{ordercount.get()}

#         {datetime.now().strftime('%Y/%m/%d %I:%M:%S')}

#         Tamato Popcorn:{countidli.get()}
#         Cheese Popcorn:{countdosa.get()}
#         Salt Popcorn:{countpuri.get()}
#         Caramel Popcorn:{countpunugu.get()}
#         Nachos:{countparota.get()}
#         Hotdog:{countchapathi.get()}
#         Coke:{countvada.get()}

#         Bill:{billvar.get()}
#         ''')

def decreaseidli():
    c=countidli.get()
    c=c-1
    if c>=0:
        countidli.set(c)
    else:
        countidli.set(0) 
def increaseidli():
    c=countidli.get()
    c=c+1
    countidli.set(c)

def decreasedosa():
    c=countdosa.get()
    c=c-1
    if c>=0:
        countdosa.set(c)
    else:
        countdosa.set(0) 
def increasedosa():
    c=countdosa.get()
    c=c+1
    countdosa.set(c)

def decreasepuri():
    c=countpuri.get()
    c=c-1
    if c>=0:
        countpuri.set(c)
    else:
        countpuri.set(0) 
def increasepuri():
    c=countpuri.get()
    c=c+1
    countpuri.set(c)

def decreasepunugu():
    c=countpunugu.get()
    c=c-1
    if c>=0:
        countpunugu.set(c)
    else:
        countpunugu.set(0) 
def increasepunugu():
    c=countpunugu.get()
    c=c+1
    countpunugu.set(c)

def decreasechapathi():
    c=countchapathi.get()
    c=c-1
    if c>=0:
        countchapathi.set(c)
    else:
        countchapathi.set(0) 
def increasechapathi():
    c=countchapathi.get()
    c=c+1
    countchapathi.set(c)

def decreaseparota():
    c=countparota.get()
    c=c-1
    if c>=0:
        countparota.set(c)
    else:
        countparota.set(0) 
def increaseparota():
    c=countparota.get()
    c=c+1
    countparota.set(c)

def decreasevada():
    c=countvada.get()
    c=c-1
    if c>=0:
        countvada.set(c)
    else:
        countvada.set(0) 
def increasevada():
    c=countvada.get()
    c=c+1
    countvada.set(c)

def billup():
    sum=(countidli.get())*150+(countdosa.get())*150+(countpuri.get())*135+(countpunugu.get())*160+(countparota.get())*100+(countchapathi.get())*120+(countvada.get())*50
    billvar.set(sum)
    number=ordercount.get()
    number+=1
    ordercount.set(number)

def clear():
        
    countidli.set(0)
    countdosa.set(0)
    countpuri.set(0)
    countpunugu.set(0)
    countparota.set(0)
    countchapathi.set(0)
    countvada.set(0)

root=Tk()

root.title("CheckouT")
root.geometry("480x480")

frame2=Frame(root).grid(padx=24,pady=32)

heading=Label(frame2,text="Snacks",font="PROMESHTwoRegular 32")
heading.grid(row=0,column=5)

mymenu=Menu(root)
mymenu.add_command(label="Save")
mymenu.add_command(label="Print")
mymenu.add_command(label="Quit",command=quit)

root.config(menu=mymenu)

idli=Label(frame2,text="Tamoto Popcorn").grid(row=1,column=1)
dosa=Label(frame2,text="Cheese Popcorn").grid(row=2,column=1)
puri=Label(frame2,text="Salt Popcorn").grid(row=3,column=1)
punugu=Label(frame2,text="Caramel Popcorn").grid(row=4,column=1)
parota=Label(frame2,text="Nachos").grid(row=5,column=1)
chapathi=Label(frame2,text="Hotdog").grid(row=6,column=1)
vada=Label(frame2,text="Coke").grid(row=7,column=1)

countidli=IntVar()
countdosa=IntVar()
countpuri=IntVar()
countpunugu=IntVar()
countparota=IntVar()
countchapathi=IntVar()
countvada=IntVar()

ordercount=IntVar()

buttonminus=Button(frame2,text="-",command=decreaseidli,bg="red",fg="white").grid(row=1,column=2)
countidlilabel=Label(frame2,textvariable=countidli).grid(row=1,column=3,padx=10)
buttonplus=Button(frame2,text="+",command=increaseidli,bg="green",fg="white").grid(row=1,column=4)
rateidli=Label(frame2,text="Rs.150",bg="yellow").grid(row=1,column=6)

buttonminus=Button(frame2,text="-",command=decreasedosa,bg="red",fg="white").grid(row=2,column=2)
countdosalabel=Label(frame2,textvariable=countdosa).grid(row=2,column=3)
buttonplus=Button(frame2,text="+",command=increasedosa,bg="green",fg="white").grid(row=2,column=4)
ratedosa=Label(frame2,text="Rs.150",bg="yellow").grid(row=2,column=6)

buttonminus=Button(frame2,text="-",command=decreasepuri,bg="red",fg="white").grid(row=3,column=2)
countpurilabel=Label(frame2,textvariable=countpuri).grid(row=3,column=3)
buttonplus=Button(frame2,text="+",command=increasepuri,bg="green",fg="white").grid(row=3,column=4)
ratepuri=Label(frame2,text="Rs.135",bg="yellow").grid(row=3,column=6)

buttonminus=Button(frame2,text="-",command=decreasepunugu,bg="red",fg="white").grid(row=4,column=2)
countpunugulabel=Label(frame2,textvariable=countpunugu).grid(row=4,column=3)
buttonplus=Button(frame2,text="+",command=increasepunugu,bg="green",fg="white").grid(row=4,column=4)
ratepunugu=Label(frame2,text="Rs.160",bg="yellow").grid(row=4,column=6)

buttonminus=Button(frame2,text="-",command=decreaseparota,bg="red",fg="white").grid(row=5,column=2)
countparotalabel=Label(frame2,textvariable=countparota).grid(row=5,column=3)
buttonplus=Button(frame2,text="+",command=increaseparota,bg="green",fg="white").grid(row=5,column=4)
rateparota=Label(frame2,text="Rs.100",bg="yellow").grid(row=5,column=6)

buttonminus=Button(frame2,text="-",command=decreasechapathi,bg="red",fg="white").grid(row=6,column=2)
countchapathilabel=Label(frame2,textvariable=countchapathi).grid(row=6,column=3)
buttonplus=Button(frame2,text="+",command=increasechapathi,bg="green",fg="white").grid(row=6,column=4)
ratechapathi=Label(frame2,text="Rs.120",bg="yellow").grid(row=6,column=6)

buttonminus=Button(frame2,text="-",command=decreasevada,bg="red",fg="white").grid(row=7,column=2)
countvadalabel=Label(frame2,textvariable=countvada).grid(row=7,column=3)
buttonplus=Button(frame2,text="+",command=increasevada,bg="green",fg="white").grid(row=7,column=4)
ratevada=Label(frame2,text="Rs.50",bg="yellow").grid(row=7,column=6)

billvar=IntVar()
billbutton=Button(frame2,text="Bill up!",command=billup).grid(row=9,column=5)
billval=Label(frame2,textvariable=billvar).grid(row=10,column=5)

clearbutton=Button(frame2,text="Clear!",command=clear).grid(row=11,column=5)

root.mainloop()