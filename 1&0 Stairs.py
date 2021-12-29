n=int(input())
initial=1
row=1
column=1
line=""
while row<=n:
    while column<=row:
        line=line+str(initial)+" "
        column+=1
        if initial==0:
            initial=1
        else:
            initial=0
    print(line)
    line=""
    row+=1
    column=1
        