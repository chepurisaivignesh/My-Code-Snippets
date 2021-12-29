n=int(input())
for i in range(1,n+1):
    line=""
    rline=""
    for j in range(1,i+1):
        line=line+str(j)
    for k in range(i,0,-1):
        rline=rline+str(k)
    print(line+" "*(n-j)*2+rline)