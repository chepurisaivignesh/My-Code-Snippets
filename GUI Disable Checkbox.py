from tkinter import *

def change():
    if checky['state']==NORMAL:
        checky.config(state=DISABLED)
    else:
        checky.config(state=NORMAL)
def check():
    print(st.get())  
def chvalue():
    st.set(0)  
    

root=Tk()
root.geometry("720x480")
root.title("Enable/Disable The Checkbox")

st=IntVar()

checky=Checkbutton(root,text="Done",variable=st)
checky.pack()
but=Button(root,text="Change activity",command=change).pack()
but1=Button(root,text="Check Value",command=check).pack()
but2=Button(root,text="Change Value",command=chvalue).pack()
root.mainloop()