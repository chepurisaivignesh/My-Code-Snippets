line1=list(map(str,(input().upper()).split()))
line2=list(map(str,(input().upper()).split()))
line3=list(map(str,(input().upper()).split()))
listy=[line1,line2,line3]

if listy[0][0]==listy[1][0]==listy[2][0]=="O" or listy[0][0]==listy[1][0]==listy[2][0]=="X":
    if listy[0][0]=="O":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
elif listy[0][1]==listy[1][1]==listy[2][1]=="O" or listy[0][1]==listy[1][1]==listy[2][1]=="X":
    if listy[0][1]=="O":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
elif listy[0][2]==listy[1][2]==listy[2][0]=="O" or listy[0][2]==listy[1][2]==listy[2][2]=="X":
    if listy[0][2]=="O":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
elif listy[0][0]==listy[0][1]==listy[0][2]=="O" or listy[0][0]==listy[0][1]==listy[0][2]=="X":
    if listy[0][0]=="O":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
elif listy[1][0]==listy[1][1]==listy[1][2]=="O" or listy[1][0]==listy[1][1]==listy[1][2]=="X":
    if listy[1][0]=="O":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
elif listy[2][0]==listy[2][1]==listy[2][2]=="O" or listy[2][0]==listy[2][1]==listy[2][2]=="X":
    if listy[2][0]=="O":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
elif listy[0][0]==listy[1][1]==listy[2][2]=="O" or listy[0][0]==listy[1][1]==listy[2][2]=="X":
    if listy[0][0]=="O":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
elif listy[0][2]==listy[1][1]==listy[2][0]=="O" or listy[0][2]==listy[1][1]==listy[2][0]=="X":
    if listy[0][2]=="O":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
else:
    print("Tie")
