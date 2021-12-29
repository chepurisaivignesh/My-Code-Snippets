n=int(input())
fv=n*(n+1) #Final Value
row=1
column=n
column2=n
ini=1
ini2=1
line=""
while row<=n:
    while column>=1:
        line=line+str(ini)+" "
        ini+=1
        column-=1
    ini2=ini
    while column2>=1:
        line=line+str(fv-ini2+2)+" "
        ini2-=1
        column2-=1

    print(" "*(row-1)*2+line)
    row+=1
    column=n-row+1
    column2=column
    line=""