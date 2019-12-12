from piece import *

# class start the game which inherits from the piece class

# the 2 players must enter their name and each one must select
# the piece of their color they want to move and then indicate where they want to move it

# a cycle is generated until waiting for the game to end, when only one piece of a color remains
# that will be the player who won the game

class Play(Piece):
    cont = 0
    board = Piece().Piece_Board(Piece().Empty_Board())
    column =['','a','b','c','d','e','f','g','h']
    row =[8,7,6,5,4,3,2,1,0]
    player1 = input("Enter player name 1: ")
    player2 = input("Enter player name 2: ")
    lb = []
    lw = []
    Piece().Print_Board(board,lb,lw)

    end = Piece().Play_End(board)
    while end == False :
        end = Piece().Play_End(board)
        if end:
            if (cont+1) % 2 == 0:
                print("Winner White pieces")
                print("player: "+player1)
                break
            else:
                print("Winner Black pieces")
                print("player: "+player2)    
                break
        try:
            if cont % 2 == 0:
                print("Turn: "+player1)
                print("Piece: White")
            else:
                print("Turn: "+player2)
                print("Piece: Black")
            PosAct =input("Select piece: ")
            PosDest =input("Movement: ")    
            columnAct=PosAct[0]
            RowAct=int(PosAct[1])
            columnDest=PosDest[0]
            RowDest=int(PosDest[1])
            PosActP=[RowAct,columnAct]
            PosDestP=[RowDest,columnDest]
            boardTemp = board
            if cont % 2 == 0:
                #if the turn is of the white piece
                if board[row.index(PosActP[0])] [column.index(PosActP[1])] == chr(9817):

                    board =  Piece().Pawn(PosActP,PosDestP,board,Piece().FWhite,Piece().FBlack,6,9,13)
                    if board != False:
                        cont += 1
                        if board[1] != "":
                            lw.append(board[1])
                        board = board[0]    
                    else:
                        board = boardTemp  

                elif  board[row.index(PosActP[0])] [column.index(PosActP[1])] == chr(9813):
                
                    board = Piece().Queen(PosActP,PosDestP,board,Piece().FWhite,Piece().FBlack)
                    if board != False:
                        cont += 1
                        if board[1] != "":
                            lw.append(board[1])
                        board = board[0]  
                    else:
                        board = boardTemp 
                else:
                    print("It is not a white piece")  
            else:   
                #if the turn is of the Black piece
                
                if board[row.index(PosActP[0])] [column.index(PosActP[1])] == chr(9823):

                    board =  Piece().Pawn(PosActP,PosDestP,board,Piece().FBlack,Piece().FWhite,1,1,5)
                    if board != False:
                        cont += 1
                        if board[1] != "":
                            lb.append(board[1])
                        board = board[0]  
                    else:
                        board = boardTemp 
                elif  board[row.index(PosActP[0])] [column.index(PosActP[1])] == chr(9819):
                    board = Piece().Queen(PosActP,PosDestP,board,Piece().FBlack,Piece().FWhite)
                    if board != False:
                        cont += 1
                        if board[1] != "":
                            lb.append(board[1])
                        board = board[0]  
                    else:
                        board = boardTemp 
                else:
                    print("It is not a Black piece")    

            Piece().Print_Board(board,lb,lw)
        except (ValueError,IndexError):print("Incorrect coordinate. Try again...")     


# play class call
Play()

