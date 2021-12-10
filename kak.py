items=["A4","Pen","Pencil","Eraser"]
inp=list(map(int,input().split()))
for i,j in zip(items,inp):
    print(i+": "+str(j))