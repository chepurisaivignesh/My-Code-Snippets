length=int(input())
bredth=int(input())
l=min(length,bredth)
b=max(length,bredth)

print(" "*(b-1)+"*"*b)
for i in range(2,l):
    print(" "*(b-i)+"*"+" "*(b-2)+"*")
print("*"*b)

# n=int(input())
# for i in range(1,n+1):
#     print(str(i)*(n-i+1))