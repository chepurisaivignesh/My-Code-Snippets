n=int(input())
print("Upward Hollow Pyramid:")
print(" "*(n-1)+"*")
for i in range(1,n-1):
    print(" "*(n-i-1)+"* "+" "*((i-1)*(2))+"*")
print("* "*n)

print("Downward Hollow Pyramid:")
print("* "*n)
for i in range(n-1,1,-1):
    print(" "*(n-i)+"* "+" "*((i-2)*(2))+"*")
print(" "*(n-1)+"*")
