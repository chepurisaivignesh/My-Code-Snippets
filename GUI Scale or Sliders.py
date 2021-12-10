from tkinter import *

def dol():
    print((v.get()))
    dollar.set(str("In Dollars: $ "+str((v.get())/75)))

def rup():
    print((r.get()))   
    rupee.set(str("In Rupees: "+(u"\u20B9") +" "+str((r.get())*75))) 

def cleary():    
    v.set(0)
    r.set(0)
    dollar.set(str("In Dollars: $ "+str(0)))
    rupee.set(str("In Rupees: "+(u"\u20B9") +" "+str(0)))


root=Tk()
root.geometry("720x480")
root.title("Sliders")

v=IntVar()
dollar=StringVar()
dollar.set("In Dollars: $ 0 ")

r=IntVar()
rupee=StringVar()
rupee.set("In Rupees: "+(u"\u20B9") +" 0")

Label(root,text="Slider in Rupees:").grid(row=0,column=0,padx=20)
slider1=Scale(root,variable=v,from_=0,to_=100,orient=HORIZONTAL,tickinterval=10,length=200).grid(row=0,column=1,padx=20)
dolbut=Button(root,text="Get Value",command=dol).grid(row=0,column=3,padx=20)
label1=Label(root,textvariable=dollar).grid(row=0,column=4,padx=20)

Label(root,text="Slider in Dollars:").grid(row=1,column=0,)
slider2=Scale(root,variable=r,from_=0,to_=100,orient=HORIZONTAL,length=200,tickinterval=10).grid(row=1,column=1)
rupbut=Button(root,text="Get Value",command=rup).grid(row=1,column=3)
label2=Label(root,textvariable=rupee).grid(row=1,column=4)

buttonmain=Button(root,text="Clear Values",command=cleary).grid(row=4,column=2)

root.mainloop()