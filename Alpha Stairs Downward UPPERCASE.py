al=input()
al=al.upper()
o=ord(al)
for i in range(1,(o-ord("A"))+2):
    start=o-i+1
    line=""
    for j in range(start,(ord("A")-1),-1):
        line=line+chr(j)+" "
    print(line)

