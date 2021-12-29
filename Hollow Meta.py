n=int(input())
print("*"+" "*(n-1)*2+"*")
for i in range(2,n+1):
    print("*"+" "*(i-2)+"*"+" "*(n-i)*2+"*"+" "*(i-2)+"*")
for j in range(n,1,-1):
    print("*"+" "*(j-2)+"*"+" "*(n-j)*2+"*"+" "*(j-2)+"*")
print("*"+" "*(n-1)*2+"*")


