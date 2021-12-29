from tkinter import *
def getvalue():
    print(f"{Namevar.get(),Agevar.get(),Gendervar.get(),Statevar.get(),Cityvar.get(),Pincodevar.get(),Contact_Numbervar.get(),checkvar.get()}")

    with open ("formanswers.txt","a") as f:
        f.write(f"{Namevar.get(),Agevar.get(),Gendervar.get(),Statevar.get(),Cityvar.get(),Pincodevar.get(),Contact_Numbervar.get(),checkvar.get()}")

root=Tk()

root.title("Questionaire")
heading=Label(root,text="Please Answer The Questions").grid(row=0,column=1)

Name=Label(root,text="Name").grid(row=1,column=0)
Age=Label(root,text="Age").grid(row=2,column=0)
Gender=Label(root,text="Gender").grid(row=3,column=0)
State=Label(root,text="State").grid(row=4,column=0)
City=Label(root,text="City").grid(row=5,column=0)
Pincode=Label(root,text="Pincode").grid(row=6,column=0)
Contact_Number=Label(root,text="Contact Number").grid(row=7,column=0)

Namevar=StringVar()
Agevar=StringVar()
Gendervar=StringVar()
Statevar=StringVar()
Cityvar=StringVar()
Pincodevar=IntVar()
Contact_Numbervar=IntVar()
checkvar=IntVar()

Nameentry=Entry(root,textvariable=Namevar).grid(row=1,column=1)
Ageentry=Entry(root,textvariable=Agevar).grid(row=2,column=1)
Genderentry=Entry(root,textvariable=Gendervar).grid(row=3,column=1)
Stateentry=Entry(root,textvariable=Statevar).grid(row=4,column=1)
Cityentry=Entry(root,textvariable=Cityvar).grid(row=5,column=1)
Pincodeentry=Entry(root,textvariable=Pincodevar).grid(row=6,column=1)
Contact_Numberentry=Entry(root,textvariable=Contact_Numbervar).grid(row=7,column=1)

check=Checkbutton(root,text="Do you want to hide details?",variable=checkvar).grid(row=8,column=0)

button=Button(root,text="Submit",command=getvalue).grid(row=8,column=1)
root.mainloop()