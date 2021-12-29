from tkinter import *
from tkinter import font

def result():

    master=Toplevel(root)
    master.geometry("1100x500")
    master.title("RESULT")

    ammonia_product=float(ammonia_produced.get())
    ammonia_product_moles=ammonia_product/17
    nitrogen_moles=ammonia_product_moles/2
    hydrogen_moles=nitrogen_moles*3

    # print(ammonia_product,ammonia_product_moles,nitrogen_moles,hydrogen_moles)

    #Stream A

    overall_nitrogen_conversion_percentage=float(nitrogen_conv_percent.get())
    nitrogen_a=((nitrogen_moles*100)/overall_nitrogen_conversion_percentage)
    hydrogen_a=((hydrogen_moles*100)/overall_nitrogen_conversion_percentage)
    total_nitrogen_hydrogen_a=(nitrogen_a+hydrogen_a)

    # print(overall_nitrogen_conversion_percentage,nitrogen_a,hydrogen_a,total_nitrogen_hydrogen_a)

    co_percentage_a=float(co_a.get())
    co2_percentage_a=float(co2_a.get())
    moles_a=(total_nitrogen_hydrogen_a*100)/(100-co_percentage_a-co2_percentage_a)

    co_moles_a=(co_percentage_a*moles_a)/100
    co2_moles_a=(co2_percentage_a*moles_a)/100

    # print(co_percentage_a,co2_percentage_a,moles_a,co_moles_a,co2_moles_a)

    #Stream B

    nitrogen_b=nitrogen_a-nitrogen_moles
    hydrogen_b=hydrogen_a-hydrogen_moles
    ammonia_b=ammonia_product_moles
    co_b=co_moles_a
    co2_b=co2_moles_a

    b_whole=hydrogen_b+nitrogen_b+ammonia_b+co_b+co2_b

    # print(nitrogen_b,hydrogen_b,ammonia_b,co_b,co2_b)

    #Stream D

    ammonia_d=ammonia_product_moles

    #Stream C

    nitrogen_c=nitrogen_b
    hydrogen_c=hydrogen_b
    co_c=co_b
    co2_c=co2_b

    c_whole=nitrogen_c+hydrogen_c+co_c+co2_c

    #Mole Fractions

    mole_fraction_nitrogen=(nitrogen_c)/(nitrogen_c + hydrogen_c + co_c + co2_c)

    mole_fraction_hydrogen=(hydrogen_c)/(nitrogen_c + hydrogen_c + co_c + co2_c)

    mole_fraction_co=(co_c)/(nitrogen_c + hydrogen_c + co_c + co2_c)

    mole_fraction_co2=(co2_c)/(nitrogen_c + hydrogen_c + co_c + co2_c)

    # print(mole_fraction_nitrogen,mole_fraction_hydrogen,mole_fraction_co,mole_fraction_co2)

    # Whole Stream Q & R

    co_conversion_rate=float(co_conversion.get())
    co2_conversion_rate=float(co2_conversion.get())
    co_q_percentage=float(co_q.get())
    co2_q_percentage=float(co2_q.get())

    mole_fraction_nitrogen_q=(1-((co_q_percentage+co2_q_percentage)/100))*0.25

    r_whole= ((moles_a*mole_fraction_nitrogen_q)-nitrogen_a)/(mole_fraction_nitrogen_q - mole_fraction_nitrogen)

    q_whole= (nitrogen_a - (moles_a*mole_fraction_nitrogen))/(mole_fraction_nitrogen_q - mole_fraction_nitrogen)

    # print(mole_fraction_nitrogen_q,q_whole,r_whole)

    # Purge Stream

    purge_whole=(nitrogen_c+hydrogen_c+co2_c+co_c)-r_whole
    purge_nitrogen=purge_whole*mole_fraction_nitrogen
    purge_hydrogen=purge_whole*mole_fraction_hydrogen
    purge_co=purge_whole*mole_fraction_co
    purge_co2=purge_whole*mole_fraction_co2
    
    # print(purge_whole,purge_nitrogen,purge_hydrogen,purge_co,purge_co2)

    # Stream R

    recycle_nitrogen=r_whole*mole_fraction_nitrogen
    recycle_hydrogen=r_whole*mole_fraction_hydrogen
    recycle_co=r_whole*mole_fraction_co
    recycle_co2=r_whole*mole_fraction_co2

    # print(recycle_nitrogen,recycle_hydrogen,recycle_co,recycle_co2)

    # Stream Q
    
    nitrogen_q=q_whole*mole_fraction_nitrogen_q
    hydrogen_q=q_whole*mole_fraction_nitrogen_q*3
    co_qstream=q_whole*(co_q_percentage)
    co2_qstream=q_whole*(co2_q_percentage)

    # print(nitrogen_q,hydrogen_q,co_qstream,co2_qstream)

    # Stream F

    nitrogen_f=mole_fraction_nitrogen_q*q_whole
    
    co_f=(100*((co_q_percentage/100)*q_whole))/(100-co_conversion_rate)
    
    co2_f=(100*((co2_q_percentage/100)*q_whole))/(100-co2_conversion_rate)

    ch4_produced=((co_f*co_conversion_rate)/100)+((co2_f*co2_conversion_rate)/100)

    h20_produced=((co_f*co_conversion_rate)/100)+(((co2_f*co2_conversion_rate)/100)*2)

    hydrogen_f=(2*ch4_produced)+(h20_produced)+(q_whole*mole_fraction_nitrogen_q*3)

    f_whole=nitrogen_f+hydrogen_f+co_f+co2_f

    # print(nitrogen_f,hydrogen_f,co_f,co2_f,ch4_produced,h20_produced,f_whole)

    Label(master,text="Chemicals",font=("Helvetica",24),relief=SUNKEN,background="seagreen").grid(row=2,rowspan=5,column=0,padx=10)
    Label(master,text="Streams",font=("Helvetica",24),relief=SUNKEN,background="seagreen").grid(row=0,columnspan=8,column=2,pady=5)

    Label(master,text="Nitrogen",justify="left").grid(row=2,column=1,sticky=W,padx=10)
    Label(master,text="Hydrogen",justify="left").grid(row=3,column=1,sticky=W,padx=10)
    Label(master,text="Carbon-Monoxide",justify="left").grid(row=4,column=1,sticky=W,padx=10)
    Label(master,text="Carbon-Di-Oxide",justify="left").grid(row=5,column=1,sticky=W,padx=10)
    Label(master,text="Ammonia",justify="left").grid(row=6,column=1,sticky=W,padx=10)
    
    Label(master,text="[F]").grid(row=1,column=2,pady=5,padx=10)
    Label(master,text="[Q]").grid(row=1,column=3,padx=10)
    Label(master,text="[A]").grid(row=1,column=4,padx=10)
    Label(master,text="[B]").grid(row=1,column=5,padx=10)
    Label(master,text="[C]").grid(row=1,column=6,padx=10)
    Label(master,text="[R]").grid(row=1,column=7,padx=10)
    Label(master,text="[P]").grid(row=1,column=8,padx=10)
    Label(master,text="[D]").grid(row=1,column=9,padx=10)


    Label(master,text=round(nitrogen_f,3)).grid(row=2,column=2,pady=5,padx=10)
    Label(master,text=round(nitrogen_q,3)).grid(row=2,column=3,padx=10)
    Label(master,text=round(nitrogen_a,3)).grid(row=2,column=4,padx=10)
    Label(master,text=round(nitrogen_b,3)).grid(row=2,column=5,padx=10)
    Label(master,text=round(nitrogen_c,3)).grid(row=2,column=6,padx=10)
    Label(master,text=round(recycle_nitrogen,3)).grid(row=2,column=7,padx=10)
    Label(master,text=round(purge_nitrogen,3)).grid(row=2,column=8,padx=10)
    Label(master,text="0").grid(row=2,column=9,padx=10)

    Label(master,text=round(hydrogen_f,3)).grid(row=3,column=2,pady=5,padx=10)
    Label(master,text=round(hydrogen_q,3)).grid(row=3,column=3,padx=10)
    Label(master,text=round(hydrogen_a,3)).grid(row=3,column=4,padx=10)
    Label(master,text=round(hydrogen_b,3)).grid(row=3,column=5,padx=10)
    Label(master,text=round(hydrogen_c,3)).grid(row=3,column=6,padx=10)
    Label(master,text=round(recycle_hydrogen,3)).grid(row=3,column=7,padx=10)
    Label(master,text=round(purge_hydrogen,3)).grid(row=3,column=8,padx=10)
    Label(master,text="0").grid(row=5,column=9,padx=10)

    Label(master,text=round(co_f,3)).grid(row=4,column=2,pady=5,padx=10)
    Label(master,text=round(co_qstream,3)).grid(row=4,column=3,padx=10)
    Label(master,text=round(co_moles_a,3)).grid(row=4,column=4,padx=10)
    Label(master,text=round(co_b,3)).grid(row=4,column=5,padx=10)
    Label(master,text=round(co_c,3)).grid(row=4,column=6,padx=10)
    Label(master,text=round(recycle_co,3)).grid(row=4,column=7,padx=10)
    Label(master,text=round(purge_co,3)).grid(row=4,column=8,padx=10)
    Label(master,text="0").grid(row=4,column=9,padx=10)

    Label(master,text=round(co2_f,3)).grid(row=5,column=2,pady=5,padx=10)
    Label(master,text=round(co2_qstream,3)).grid(row=5,column=3,padx=10)
    Label(master,text=round(co2_moles_a,3)).grid(row=5,column=4,padx=10)
    Label(master,text=round(co2_b,3)).grid(row=5,column=5,padx=10)
    Label(master,text=round(co2_c,3)).grid(row=5,column=6,padx=10)
    Label(master,text=round(recycle_co2,3)).grid(row=5,column=7,padx=10)
    Label(master,text=round(purge_co2,3)).grid(row=5,column=8,padx=10)
    Label(master,text="0").grid(row=5,column=9,padx=10)

    Label(master,text="0").grid(row=6,column=2,pady=5,padx=10)
    Label(master,text="0").grid(row=6,column=3,padx=10)
    Label(master,text="0").grid(row=6,column=4,padx=10)
    Label(master,text=ammonia_product_moles).grid(row=6,column=5,padx=10)
    Label(master,text="0").grid(row=6,column=6,padx=10)
    Label(master,text="0").grid(row=6,column=7,padx=10)
    Label(master,text="0").grid(row=6,column=8,padx=10)
    Label(master,text=ammonia_product_moles).grid(row=6,column=9,padx=10)

    Label(master,text="Total").grid(row=7,column=1,pady=5,padx=10)
    Label(master,text=round(f_whole,3)).grid(row=7,column=2,padx=10)
    Label(master,text=round(q_whole,3)).grid(row=7,column=3,padx=10)
    Label(master,text=round(moles_a,3)).grid(row=7,column=4,padx=10)
    Label(master,text=round(b_whole,3)).grid(row=7,column=5,padx=10)
    Label(master,text=round(c_whole,3)).grid(row=7,column=6,padx=10)
    Label(master,text=round(r_whole,3)).grid(row=7,column=7,padx=10)
    Label(master,text=round(purge_whole,3)).grid(row=7,column=8,padx=10)
    Label(master,text=round(ammonia_product_moles,3)).grid(row=7,column=9,padx=10)

    Label(master,text="Methane produced: ",font=("Helvetica",16)).grid(row=10,column=3,pady=10)
    Label(master,text=round(ch4_produced,3)).grid(row=10,column=4,padx=10)
    Label(master,text="Water produced: ",font=("Helvetica",16)).grid(row=11,column=3,pady=10)
    Label(master,text=round(h20_produced,3)).grid(row=11,column=4,padx=10)


    
    master.mainloop()

#-------------------------------------------------------------------

root=Tk()
root.title("Haber's Process")
root.geometry("800x800")
root.config(pady=20)

heading=Label(root,text="Ammonia Synthesis",font=("Helvetica",24),relief=SOLID,background="magenta").pack(ipadx=5,ipady=5)

subheading=Label(root,text="Flow-Chart for Reference",font=(16)).pack(pady=10)

#-------------------------------------------------------------------------

#Designing Flow Chart Diagram
can=Canvas(root,width=750,height=250)

can.create_text((15*1.5),(60*1.5),text="Input [F]")
can.create_line(10*1.5,70*1.5,40*1.5,70*1.5,fill="green",width=5)
can.create_rectangle(40*1.5,50*1.5,120*1.5,90*1.5,fill="gray")#Feed Guard Converter
can.create_line(120*1.5,70*1.5,150*1.5,70*1.5,fill="blue",width=5)
can.create_line(150*1.5,70*1.5,180*1.5,70*1.5,fill="brown",width=5)
can.create_rectangle(180*1.5,50*1.5,240*1.5,90*1.5,fill="gray")#Reactor
can.create_line(240*1.5,70*1.5,270*1.5,70*1.5,fill="seagreen",width=5)
can.create_rectangle(270*1.5,50*1.5,330*1.5,90*1.5,fill="gray")#Condensor
can.create_line(330*1.5,70*1.5,390*1.5,70*1.5)
can.create_line(420*1.5,90*1.5,420*1.5,120*1.5,fill="magenta",width=5)#Ammonia Product
can.create_rectangle(390*1.5,50*1.5,450*1.5,90*1.5,fill="gray")#Seperator
can.create_line(420*1.5,50*1.5,420*1.5,20*1.5,fill="orange",width=5)
can.create_line(420*1.5,20*1.5,450*1.5,20*1.5,fill="purple",width=5)#Purge
can.create_line(420*1.5,20*1.5,150*1.5,20*1.5,fill="red",width=5)
can.create_line(150*1.5,20*1.5,150*1.5,70*1.5,fill="red",width=5)
can.create_text((80*1.5),(70*1.5),text="Feed Convertor")
can.create_text((210*1.5),(70*1.5),text="Reactor")
can.create_text((250*1.5),(30*1.5),text="Recycle [R]")
can.create_text((300*1.5),(70*1.5),text="Condensor")
can.create_text((420*1.5),(70*1.5),text="Seperator")
can.create_text((420*1.5),(130*1.5),text="Ammonia [D]")
can.create_text((470*1.5),(20*1.5),text="Purge [P]")
can.create_text((135*1.5),(60*1.5),text="[Q]")
can.create_text((165*1.5),(60*1.5),text="[A]")
can.create_text((255*1.5),(60*1.5),text="[B]")
can.create_text((430*1.5),(35*1.5),text="[C]")

can.pack()
#------------------------------------------------------------------------------------

subheadinginputs=Label(root,text="INPUTS",font=(16),relief=SOLID,background="cyan").pack(pady=10,ipadx=5,ipady=2)

ammonia_produced=StringVar()
f1=Frame(root,pady=5,width=800)
q1=Label(f1,text="Ammonia Produced per Day (KG):   ").pack(side="left")
a1=Entry(f1,textvariable=ammonia_produced).pack(side="left",padx=5)
# q1.pack(side="left")
# a1.pack(side="left")
f1.pack()

nitrogen_conv_percent=StringVar()
f2=Frame(root,pady=5,width=800)
q2=Label(f2,text="Overall Nitrogen Conversion Percentage:   ").pack(side="left")
a2=Entry(f2,textvariable=nitrogen_conv_percent).pack(side="left",padx=5)
# q2.pack(side="left")
# a2.pack(side="left")
f2.pack()

co_conversion=StringVar()
f7=Frame(root,pady=5,width=800)
q7=Label(f7,text="Carbon-Monoxide conversion percentage :   ").pack(side="left")
a7=Entry(f7,textvariable=co_conversion).pack(side="left",padx=5)
# q2.pack(side="left")
# a2.pack(side="left")
f7.pack()

co2_conversion=StringVar()
f8=Frame(root,pady=5,width=800)
q8=Label(f8,text="Carbon-Monoxide conversion percentage :   ").pack(side="left")
a8=Entry(f8,textvariable=co2_conversion).pack(side="left",padx=5)
# q2.pack(side="left")
# a2.pack(side="left")
f8.pack()

co_q=StringVar()
f3=Frame(root,pady=5,width=800)
q3=Label(f3,text="Carbon-Monoxide percentage in feed after Conversion [Q]:   ").pack(side="left")
a3=Entry(f3,textvariable=co_q).pack(side="left",padx=5)
# q2.pack(side="left")
# a2.pack(side="left")
f3.pack()

co2_q=StringVar()
f4=Frame(root,pady=5,width=800)
q4=Label(f4,text="Carbon-Di-Oxide percentage in feed after Conversion [Q]:   ").pack(side="left")
a4=Entry(f4,textvariable=co2_q).pack(side="left",padx=5)
# q2.pack(side="left")
# a2.pack(side="left")
f4.pack()

co_a=StringVar()
f5=Frame(root,pady=5,width=800)
q5=Label(f5,text="Carbon-Monoxide percentage in Stream [A]:   ").pack(side="left")
a5=Entry(f5,textvariable=co_a).pack(side="left",padx=5)
# q2.pack(side="left")
# a2.pack(side="left")
f5.pack()

co2_a=StringVar()
f6=Frame(root,pady=5,width=800)
q6=Label(f6,text="Carbon-Di-Oxide percentage in Stream [A]:   ").pack(side="left")
a6=Entry(f6,textvariable=co2_a).pack(side="left",padx=5)
# q2.pack(side="left")
# a2.pack(side="left")
f6.pack()

res=Button(root,text="Result",command=result).pack(pady=20,ipady=2,ipadx=10)

root.mainloop()

