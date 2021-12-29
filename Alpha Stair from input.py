al=input()
al=al.upper()
n=ord(al)
for i in range(1,(n-ord("A"))+2):
    line=""
    for j in range(ord(al),ord(al)-i,-1):
        line=line+chr(j)+" "
    print(line)