n=int(input())
row=1
ini=1
line=""
while row<=n:
    while ini>0:
        line=line+str(ini)
        ini-=1
    ini+=1
    while ini<row:
        ini+=1
        line=line+str(ini)
    print(" "*(n-row)+line)
    line=""
    row+=1
    ini=row
