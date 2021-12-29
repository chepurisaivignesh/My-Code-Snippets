n=int(input())
for i in range(1,n+1):
    spaces=" "*(n-i)
    line=""
    for j in range(i,0,-1):
        line=line+str(j)
    for k in range(2,i+1):
        line=line+str(k)
    print(spaces+line)
for i in range(n-1,0,-1):
    spaces=" "*(n-i)
    line=""
    for j in range(i,0,-1):
        line=line+str(j)
    for k in range(2,i+1):
        line=line+str(k)
    print(spaces+line)
    