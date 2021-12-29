n=int(input())
print(" "*(n-0-1)+"*")
for i in range(1,n-1):
    print(" "*(n-i-1)+"* "+" "*((i-1)*2)+"*")
print("* "+" "*((n-2)*2)+"*")
for i in range(n-1,1,-1):
    print(" "*(n-i)+"* "+" "*((i-2)*2)+"*")
print(" "*(n-0-1)+"*")

     
