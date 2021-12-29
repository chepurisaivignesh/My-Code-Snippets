n=int(input())
#Downward Triangular Pyramid
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

print("########")

#Upward Triangular Pyramid
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

print("Trinagular Sand Clock")
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
