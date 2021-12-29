n=int(input())
for i in range((2*n)-1):
    line=""
    for j in range((2*n)-1):
        line=line+str(n-min(i,j,(2*n-2-i),(2*n-2-j)))+" "
    print(line)

