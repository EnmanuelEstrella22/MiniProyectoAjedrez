from utilities import *

# class board which inherits from the utilities class

# in this class are the methods where the bacio board is generated and then a method where it is
# assign the pieces
# We also have the method of changing the piece, the method of changing the pawn for a queen
# method of validating if the game is over, method of finding the first piece on the board


class Chessboard(Utilities):

    # Generating the board without parts
    def Empty_Board(self):
        for row in range(0,8):
            Lpair=[chr(9633),chr(9632),chr(9633),chr(9632),chr(9633),chr(9632),chr(9633),chr(9632)]
            Lodd=[chr(9632),chr(9633),chr(9632),chr(9633),chr(9632),chr(9633),chr(9632),chr(9633)]
            if self.pair(row):
                Lpair.insert(0,8-row)
                self.board.append(Lpair)
            else:
                Lodd.insert(0,8-row)
                self.board.append(Lodd)
        self.board.append(self.column) 
        return self.board

    # assigning the pieces to the board
    def Piece_Board(self, t):
        for f in range(0, 9):
            for c in range(0, 9):
                if f < 2 and c > 0:
                    if f == 0:
                        if c == 4:
                            t[f][c] = self.FBlack[1]
                    else:
                        t[f][c] = self.FBlack[2]
                elif f > 5 and f < 8 and c > 0:
                    if f == 7:
                        if c == 4:
                            t[f][c] = self.FWhite[1]
                    else:
                        t[f][c] = self.FWhite[2]
        return t


    # move position pieces
    def Piece_Move(self, t, f1, f2):
        rowAct  = self.row.index(f1[0])
        columnAct =self.column.index(f1[1])
        rowDest= self.row.index(f2[0])
        columnDest =self.column.index(f2[1])
        posicion = [rowAct, columnAct]
        posicion1 = [rowDest,columnDest]
        pieza1 = self.Piece_in_Board(posicion, self.Empty_Board())
        pieza2 = self.Piece_of_Chess(posicion, t)
        r = self.Change_Pawn_To_Queen(t,posicion,posicion1)
        if r:
            t[rowAct][columnAct] = pieza1
            t[rowDest][columnDest] = r
        else:
            t[rowAct][columnAct] = pieza1
            t[rowDest][columnDest] = pieza2    
        return t  

    # Change the pawn to queen when she reaches the end
    def Change_Pawn_To_Queen(self,t,pos1,pos2): 
        r = t[pos1[0]][pos1[1]] == self.FWhite[2]
        r2 = t[pos1[0]][pos1[1]] == self.FBlack[2]     
        if r :
            if pos2[0] == 0:
                return self.FWhite[1]
        else:
            if r2 :
                if pos2[0] == 7:
                    return self.FBlack[1]
        return False

    # Validate if the game is over, in case you find a different piece than the one you found it returns false
    def Play_End(self,t):
        r = self.First_Piece_Board(t)
        if r:
            for items in t:
                for i in items:
                    if i in r[1]:
                        return False
            return True                  
        return False


    # Find the first piece
    def First_Piece_Board(self,t):
        for items in t:
            for i in items:
                if i in self.FWhite: 
                    return [i,self.FBlack] 
                if i in self.FBlack: 
                    return [i,self.FWhite]           
        return False