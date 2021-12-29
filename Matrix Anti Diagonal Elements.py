m,n=map(int,input().split())

listy=[]

val=0

for numb in range(m):
    l=list(map(int,input().split()))
    listy.append(l)

for val in range((m+n)-1):
    stringy=""
    for i in range(m):
        for j in range(n):
            if i+j==val:
                stringy=stringy+str(listy[i][j])+" "
    print(stringy)
    