n=int(input())
start=1 #For rows count
number=1 #For 1,2,3..15 to be printed
i=1 #For how many columns
line="" #To print a row
while start<=n:
    while i<=start:
        line=line+str(number)+" "
        i+=1
        number+=1
    print(line)
    line="" #Bringing back default value for new row
    i=1 #Bringing back to get number of columns.
    start+=1