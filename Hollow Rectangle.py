l=int(input("Enter the length:"))
b=int(input("Enter the bredth:"))
if l>=2 and b>=2:
    print("*"*b)
    for i in range(0,l-2):
        print("*"+" "*(b-2)+"*")
    print("*"*b)
else:
    print("Cant print following rectangle.")
