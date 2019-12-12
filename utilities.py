# utilities class, where all the methods to be reused in the project are found

class Utilities():

    # Constructor Method
    def __init__(self):
        self.Lpair   = [chr(9633), chr(9632), chr(9633), chr(
            9632), chr(9633), chr(9632), chr(9633), chr(9632)]
        self.Lodd    = [chr(9632), chr(9633), chr(9632), chr(
            9633), chr(9632), chr(9633), chr(9632), chr(9633)]
        self.board   = []
        self.FBlack  = ['', chr(9819), chr(9823)]
        self.FWhite  = ['', chr(9813), chr(9817)]
        self.column  = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.row     = [8, 7, 6, 5, 4, 3, 2, 1, 0]

        
    # Pair Method
    def pair(self, n):
        if n % 2 == 0:
            return True
        return False

    # Print Board Method
    def Print_Board(self,board,LB,LW):

        print()
        for LisN in LB:
            print(LisN, end=' ')
        print()
        print("_________________")
        print()

        for items in board:
            for i in items:
                print(i, end=' ')
            print()

        print("_________________")
        for LisN in LW:
            print(LisN, end=' ')
        print()

    # Find that piece on the board without pieces
    def Piece_in_Board(self, p,board):
        return board[p[0]][p[1]]

    # Find that chess piece on the board but with the chips placed
    def Piece_of_Chess(self, p, board):
        return board[p[0]][p[1]]

    # validation when moving the piece if there is a piece of your equipment where it goes
    def Validate_Piece(self,posAct,PosDest,board,ColorPiece):
        rowAct      = self.row.index(posAct[0])
        columnAct   = self.column.index(posAct[1])
        rowDest     = self.row.index(PosDest[0])
        columnDest  = self.column.index(PosDest[1])

        if board[rowAct][columnAct] not in ColorPiece :
            print("not your piece")
            return False
        elif  board[rowDest][columnDest] in ColorPiece:
            print("there is a piece of your team in that position")
            return False
        return True  


    #  crossing coordinates where the piece will pass
    def Cycle_Travel(self,posAct,PosDest,ColorPiece,board):
        rowAct      = self.row.index(posAct[0])
        rowDest     = self.row.index(PosDest[0])
        columnDest  = self.column.index(PosDest[1])

        for items in range(int(rowDest),int(rowAct)):
            if board[items][columnDest] in ColorPiece:
                print("can't fly piece of your team")
                return False
        return True 

    # Validate movement of the secondary diagonal queen
    def Validate_Queen_Diagonal_second(self,PosAct,PosDest,ColorPiece,ColorPieceEne,board):
        rowAct      = self.row.index(PosAct[0])
        columnAct   =self.column.index(PosAct[1])
        rowDest     = self.row.index(PosDest[0])
        columnDest  = self.column.index(PosDest[1])
        contC       = columnDest
        contAct     = columnAct - 1 
        TemRecorDest = rowDest 

        if rowDest < rowAct:# so that it also validates when moving backwards
            for f in range(int(rowDest),int(rowAct)):
                if board[f][contC] in ColorPiece :
                    print("can't fly piece of your team")
                    return False 

                if f != TemRecorDest  and  board[f][contC] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False     
                contC -= 1
            return True  
        else:
            for f in range(int(rowAct+1),int(rowDest+1)):
                if board[f][contAct] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f != rowDest+1 and  board[f][contAct] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False 
                contAct -= 1
            return True


    # validate that the queen moves in the secondary diagonal
    def Validate_Queen_Diagonal_second_Black(self,PosAct,PosDest,ColorPiece,ColorPieceEne,board):
        if ColorPiece == self.FWhite:#validate that the queen is white
            return self.Validate_Queen_Diagonal_second(PosAct,PosDest,ColorPiece,ColorPieceEne,board)  

        rowAct      = self.row.index(PosAct[0])
        columnAct   = self.column.index(PosAct[1])
        rowDest     = self.row.index(PosDest[0])
        columnDest  = self.column.index(PosDest[1])

        TemRecorDest = rowDest

        if rowDest < rowAct:# so that it also validates when moving backwards
            contC = columnDest
            for f in range(int(rowDest),int(rowAct)):
                if board[f][contC] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f != TemRecorDest  and  board[f][contC] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False     
                contC -= 1
            return True  
        else:
            contC = columnAct - 1
            for f in range(int(rowAct+1),int(rowDest+1)):
                if board[f][contC] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f != rowDest and  board[f][contC] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False    
                contC -= 1
            return True

    # validate that the queen moves on the main diagonal
    def Validate_Queen_Diagonal_Principal(self,PosAct,PosDest,ColorPiece,ColorPieceEne,board):
        rowAct      = self.row.index(PosAct[0])
        columnAct   = self.column.index(PosAct[1])
        rowDest     = self.row.index(PosDest[0])
        columnDest  = self.column.index(PosDest[1])

        contAct     = columnAct + 1 
        TemRecorDest = rowDest
        contC = columnDest
        if rowDest < rowAct:# so that it also validates when moving backwards
            for f in range(int(rowDest),int(rowAct)):
                if board[f][contC] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f != TemRecorDest  and  board[f][contC] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False     
                contC += 1
            return True 
        else:
            for f in range(int(rowAct+1),int(rowDest+1)):
                if board[f][contAct] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f != rowDest+1 and  board[f][contAct] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False    
                contAct += 1
            return True 

    # validate that the queen moves on the main diagonal
    def Validate_Queen_Diagonal_Principal_Black(self,PosAct,PosDest,ColorPiece,ColorPieceEne,board):
        if ColorPiece == self.FWhite:#validate that the queen is white
            return self.Validate_Queen_Diagonal_Principal(PosAct,PosDest,ColorPiece,ColorPieceEne,board) 

        rowAct      = self.row.index(PosAct[0])
        columnAct   = self.column.index(PosAct[1])
        rowDest     = self.row.index(PosDest[0])
        columnDest  = self.column.index(PosDest[1])
        TemRecorDest = rowDest

        if rowDest < rowAct:# so that it also validates when moving backwards
            contC = columnDest
            for f in range(int(rowDest),int(rowAct)):
                if board[f][contC] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f != TemRecorDest  and  board[f][contC] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False    
                contC += 1
            return True 
        else:
            contC = columnAct + 1
            for f in range(int(rowAct+1),int(rowDest+1)):
                if board[f][contC] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f != rowDest and  board[f][contC] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False    
                contC += 1
            return True 

    #  Validate the queen's movement vertically
    def Validate_Queen_Vertical(self,PosAct,PosDest,ColorPiece,ColorPieceEne,board):
        rowAct      = self.row.index(PosAct[0])
        rowDest     = self.row.index(PosDest[0])
        columnDest  = self.column.index(PosDest[1])

        if rowDest < rowAct:# so that it also validates when moving backwards
            for f in range(int(rowDest),int(rowAct)):
                print(f,columnDest,board[f][columnDest])
                if board[f][columnDest] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f!= rowDest and board[f][columnDest] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False     
            return True 
        else:
            for f in range(int(rowAct+1),int(rowDest+1)):
                print(f,columnDest,board[f][columnDest])
                if board[f][columnDest] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f!= rowDest+1 and board[f][columnDest] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False    
            return True

    # Validate the queen's movement horizontally
    def Validate_Queen_Horizontal(self,PosAct,PosDest,ColorPiece,ColorPieceEne,board):
        rowAct      = self.row.index(PosAct[0])
        columnAct   = self.column.index(PosAct[1])
        columnDest  = self.column.index(PosDest[1])

        if columnAct < columnDest:# so that it also validates when moving backwards
            for f in range(int(columnAct+1),int(columnDest+1)):
                if board[rowAct][f] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f!= columnDest+1 and board[rowAct][f] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False       
            return True  
        else:
            for f in range(int(columnDest),int(columnAct)):
                if board[rowAct][f] in ColorPiece:
                    print("can't fly piece of your team")
                    return False

                if f!= columnDest and board[rowAct][f] in ColorPieceEne:
                    print("can't fly piece of your team contrary")
                    return False     
            return True     

    

