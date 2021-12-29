a=int(input())
for a in range(a):
    b=input()
    c=sorted(b)
    sum=0
    for k in range(len(c)):
        sum=sum+((k+1)*(ord(c[k])-96))
    print(sum)    
