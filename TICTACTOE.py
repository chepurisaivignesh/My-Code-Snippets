con=True
while con:
    winner=""
    print("\nTic-Tac-Board")
    print("\nTL|TM|TR")
    print("--+--+--")
    print("ML|MM|MR")
    print("--+--+--")
    print("LL|LM|LR\n")
    def boardy(board):
        print(board["TL"]+"|"+board["TM"]+"|"+board["TR"])
        print("-+-+-")
        print(board["ML"]+"|"+board["MM"]+"|"+board["MR"])
        print("-+-+-")
        print(board["LL"]+"|"+board["LM"]+"|"+board["LR"])
    
    board={"TL":" ","TM":" ","TR":" ","ML":" ","MM":" ","MR":" ","LL":" ","LM":" ","LR":" "}
    turn='X'
    for i in range(9):
        move=input("Enter Position :")
        if turn=='X':
            board[move]=turn
            if board["TL"]==turn and board["TM"]==turn and board["TR"]==turn:
                winner="X"
                boardy(board)        
                break
            elif board["ML"]==turn and board["MM"]==turn and board["MR"]==turn:
                winner="X"
                boardy(board)
                break
            elif board["LL"]==turn and board["LM"]==turn and board["LR"]==turn:
                winner="X"
                boardy(board)
                break
            elif board["TL"]==turn and board["ML"]==turn and board["LL"]==turn:
                winner="X"
                boardy(board)
                break
            elif board["TM"]==turn and board["MM"]==turn and board["LM"]==turn:
                winner="X"
                boardy(board)
                break
            elif board["TR"]==turn and board["MR"]==turn and board["LR"]==turn:
                winner="X"
                boardy(board)
                break        
            elif board["TL"]==turn and board["MM"]==turn and board["LR"]==turn:
                winner="X"
                boardy(board)
                break
            elif board["TR"]==turn and board["MM"]==turn and board["LL"]==turn:
                winner="X"
                boardy(board)
                break
            else:
                boardy(board)
            turn='O'
        else:
            board[move]=turn
            if board["TL"]==turn and board["TM"]==turn and board["TR"]==turn:
                winner="O"
                boardy(board)        
                break
            elif board["ML"]==turn and board["MM"]==turn and board["MR"]==turn:
                winner="O"
                boardy(board)
                break
            elif board["LL"]==turn and board["LM"]==turn and board["LR"]==turn:
                winner="O"
                boardy(board)
                break
            elif board["TL"]==turn and board["ML"]==turn and board["LL"]==turn:
                winner="O"
                boardy(board)
                break
            elif board["TM"]==turn and board["MM"]==turn and board["LM"]==turn:
                winner="O"
                boardy(board)
                break
            elif board["TR"]==turn and board["MR"]==turn and board["LR"]==turn:
                winner="O"
                boardy(board)
                break        
            elif board["TL"]==turn and board["MM"]==turn and board["LR"]==turn:
                winner="O"
                boardy(board)
                break
            elif board["TR"]==turn and board["MM"]==turn and board["LL"]==turn:
                winner="O"
                boardy(board)
                break
            else:
                boardy(board)
            turn='X'
    if winner=="X" or winner=="O":      
        print("Winner:"+winner)
    else:
        print("Game is Tie")    
    question=input("Do you want to continue(Y/N):")
    if question=='Y':
        con=True
    else:
        break
print("Thanks for playing game.")        


        



