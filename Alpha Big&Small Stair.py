n=int(input())
alpha=ord("a")
number=1
for i in range(1,n+1):
    line=""
    for j in range(i):
        if number%2:
            line=line+chr(alpha)+" "
        else:
            line=line+chr(alpha).upper()+" "
        alpha+=1
        number+=1
    print(line)