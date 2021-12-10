from tkinter import *

def result():
    p=product.get()
    o=ontime.get()
    m=((p*100)/(o*17.03*24))
    moles.set(str("%.3f"%m))

    c=nitroconversion.get()
    ffn=freshfeedn.get()
    ffn=((m)*100)/(2*c)
    freshfeedn.set(str("%.3f"%(ffn))) 

    h=freshfeedh.get()
    h=(ffn*3)
    freshfeedh.set(str("%.3f"%h))
    
    ar=ammoniareactor.get()
    sp=singlepassconversion.get()
    ar=(m*100)/sp
    ammoniareactor.set(str("%.3f"%ar))

    pn=purgen.get()
    pn=((100-c)*ffn)/100
    purgen.set(str("%.3f"%pn))

    ph=purgeh.get()
    ph=pn*3
    purgeh.set(str("%.3f"%ph))

    enh=extentnh.get()
    enh=ar/2
    extentnh.set(str("%.3f"%enh))

    nre=reactneff.get()
    nre=4*enh
    reactneff.set(str("%.3f"%nre))

    nls=nleavesep.get()
    hls=hleavesep.get()
    nls=nre
    hls=nre
    nleavesep.set(str("%.3f"%nls))
    hleavesep.set(str("%.3f"%hls))

    nhls=nhleavesep.get()
    nhls=ar-m
    nhleavesep.set(str("%.3f"%nhls))

    nhlp=nhlostpurge.get()
    nhlp=nhls*(pn/nre)
    nhlostpurge.set(str("%.3f"%nhlp))

    window=Toplevel(root)
    window.title("RESULTS")
    window.geometry("720x720")
    window.config(pady=30)

    Label(window,text="Flow rate of Ammonia as flow rate:").pack()
    Label(window,text=moles.get()).pack()
    Label(window,text="Fresh Nitrogen feed flow rate:").pack()
    Label(window,text=freshfeedn.get()).pack()
    Label(window,text="Fresh Hydrogen feed flow rate:").pack()
    Label(window,text=freshfeedh.get()).pack()
    Label(window,text="Ammonia Leaving reactor").pack()
    Label(window,text=ammoniareactor.get()).pack()
    Label(window,text="Nitrogen in Purge Stream:").pack()
    Label(window,text=purgen.get()).pack()
    Label(window,text="Hydrogen in Purge Stream:").pack()
    Label(window,text=purgeh.get()).pack()
    Label(window,text="Extent of reaction:").pack()
    Label(window,text=extentnh.get()).pack()
    Label(window,text="Flow rate of Nitrogen as reactor flow effluent:").pack()
    Label(window,text=reactneff.get()).pack()                                 #both equal
    Label(window,text="Flow rate of Hydrogen as reactor flow effluent:").pack()
    Label(window,text=reactneff.get()).pack()
    Label(window,text="Flow rate of Nitrogen leaving seprator:").pack()
    Label(window,text=nleavesep.get()).pack()
    Label(window,text="Flow rate of Hydrogen leaving seperator:").pack() 
    Label(window,text=hleavesep.get()).pack()
    Label(window,text="Flow rate of Ammonia leaving seperator:").pack()
    Label(window,text=nhleavesep.get()).pack()
    Label(window,text="Flow rate of Ammonia lost in Purge Stream:").pack()
    Label(window,text=nhlostpurge.get()).pack()

    close=Button(window,text="Close",command=lambda :window.destroy()).pack(pady=20)
    window.mainloop()

def clear():
    product.set("")
    nitroconversion.set("")
    ontime.set("")
    singlepassconversion.set("")    
    
root= Tk()
root.title("AMMONIA SYNTHESIS")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
#setting tkinter root size
root.geometry("%dx%d" % (width, height))
root.config(padx=(width-720)//2)

can=Canvas(root,width=720,height=500)
can.grid(row=0,column=0,columnspan=2)
can.create_line (50,100,400,100,fill="red")
can.create_rectangle(400,50,600,150,fill="blue") 
can.create_line (600,100,680,100,fill="red")
can.create_line (680,100,680,280,fill="red")  
can.create_line (680,280,600,280,fill="red")
can.create_rectangle(400,230,600,330,fill="blue") 
can.create_line (120,280,400,280,fill="red")
can.create_line (180,280,180,100,fill="red")
can.create_line (500,330,500,380,fill="red")
can.create_text(50,80,text="Fresh Feed",font="20")
can.create_text(270,80,text="Recycle Feed",font="20")
can.create_text(120,260,text="Purge",font="20")
can.create_text(270,260,text="Seperator Outlet",font="20")
can.create_text(500,400,text="Ammonia Product",font="20")
can.create_text(600,190,text="Reactor Outlet",font="20")
can.create_text(500,100,text="Reactor",font=('freemono', 20, 'bold'),fill="white")
can.create_text(500,280,text="Seperator",font=('freemono', 20, 'bold'),fill="white")

product=IntVar()
nitroconversion=IntVar()
ontime=IntVar()
singlepassconversion=IntVar()
# ------------
moles=StringVar()
freshfeedn=StringVar()
freshfeedh=StringVar()
ammoniareactor=StringVar()
purgen=StringVar()
purgeh=StringVar()
extentnh=StringVar()
reactneff=StringVar()
nleavesep=StringVar()
hleavesep=StringVar()
nhleavesep=StringVar()
nhlostpurge=StringVar()

productlabel=Label(root,text="Amount of Product formed(kg): ").grid(row=1,column=0,pady=5)
productentry=Entry(root,textvariable=product).grid(row=1,column=1)
ontimelabel=Label(root,text="Ontime(%): ").grid(row=2,column=0,pady=5)
ontimeentry=Entry(root,textvariable=ontime).grid(row=2,column=1)
nitoconversionlabel=Label(root,text="Percentage of Nitrogen Converted(%): ").grid(row=3,column=0,pady=5)
nitoconversionentry=Entry(root,textvariable=nitroconversion).grid(row=3,column=1)
singlepasslabel=Label(root,text="Singlepass Reactor Conversion(%): ").grid(row=4,column=0,pady=5)
singlepassentry=Entry(root,textvariable=singlepassconversion).grid(row=4,column=1)

resulty=Button(root,text="Result",command=result).grid(row=5,column=0,pady=5)
clr=Button(root,text="Clear",command=clear).grid(row=5,column=1)

root.mainloop()