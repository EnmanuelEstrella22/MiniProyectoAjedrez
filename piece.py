from board import *

# class piece where the pawn and queen's methods are located. this class inherits from the chess board

# in this is the pawn method with each of the validations of its movements
# the pawn method will also validate a white pawn like a black pawn

# also the queen's method meets each of the validations of her movements
# the queen's method will validate a white queen like a black queen

class Piece(Chessboard):

    # method to establish the rules and movements of the pawn
    def Pawn(self,posAct,PosDest,board,ColorPiece,ColorPieceEne,num1,num2,num3):
        RowAct = self.row.index(posAct[0])
        ColumnAct = self.column.index(posAct[1])
        RowDest = self.row.index(PosDest[0])
        ColumnDest = self.column.index(PosDest[1])
        ListPiece = (board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])])
        if PosDest[1] != posAct[1]:
            if RowAct + ColumnAct == RowDest + ColumnDest or RowAct - ColumnAct == RowDest - ColumnDest and abs(self.row.index(PosDest[0]) - self.row.index(posAct[0])) == 1:
                if self.Validate_Piece(posAct,PosDest,board,ColorPiece):
                    if board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])] in ColorPieceEne:
                         print("Ate Piece") 
                         return [self.Piece_Move(board,posAct,PosDest),ListPiece]
                    else:
                        print("don't has piece for ate")
                else:
                    print("the pawn can't fly piece")         
            else:  
                print("The Pawn only moves vertically")
        elif self.row.index(posAct[0]) == num1 :
            if self.row.index(posAct[0])+self.row.index(PosDest[0]) > num2 and self.row.index(posAct[0])+self.row.index(PosDest[0]) < num3 and  board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])] not in ColorPieceEne:  
                if self.Cycle_Travel(posAct,PosDest,ColorPieceEne,board):
                    return [self.Piece_Move(board,posAct,PosDest),""]      
            else: 
                print("invalid movement")
        else:# validate that it moves only one step forward if it has already left its position
            if ColorPiece == self.FBlack: # If it is not white piece
                if self.row.index(PosDest[0]) > self.row.index(posAct[0]) and self.row.index(PosDest[0]) - self.row.index(posAct[0]) == 1 and  board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])] not in ColorPieceEne:       
                    if self.Validate_Piece(posAct,PosDest,board,ColorPiece):
                        return [self.Piece_Move(board,posAct,PosDest),""]
                else: 
                    print("invalid movement")
            else: 
                if self.row.index(PosDest[0]) < self.row.index(posAct[0]) and abs(self.row.index(PosDest[0]) - self.row.index(posAct[0])) == 1 and  board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])] not in ColorPieceEne:       
                    if self.Validate_Piece(posAct,PosDest,board,ColorPiece):
                        return [self.Piece_Move(board,posAct,PosDest),""]
                else: 
                    print("invalid movement")   
        return False 


    # method to establish the rules and movements of the queen
    def Queen(self,posAct,PosDest,board,ColorPiece,ColorPieceEne):
        RowAct = self.row.index(posAct[0])
        ColumnAct = self.column.index(posAct[1])
        RowDest = self.row.index(PosDest[0])
        ColumnDest = self.column.index(PosDest[1])
        ListPiece = (board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])])
        if RowAct == RowDest  or ColumnAct == ColumnDest   or RowAct + ColumnAct == RowDest + ColumnDest or RowAct - ColumnAct == RowDest - ColumnDest:      
            if RowAct + ColumnAct == RowDest + ColumnDest and self.Validate_Queen_Diagonal_second_Black(posAct,PosDest,ColorPiece,ColorPieceEne,board):
                 if board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])] in ColorPieceEne:
                    print("Ate Piece")
                    return [self.Piece_Move(board,posAct,PosDest),ListPiece]
                 return [self.Piece_Move(board,posAct,PosDest),""]   
            if RowAct - ColumnAct == RowDest - ColumnDest and self.Validate_Queen_Diagonal_Principal_Black(posAct,PosDest,ColorPiece,ColorPieceEne,board):
                if board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])] in ColorPieceEne:
                    print("Ate Piece")
                    return [self.Piece_Move(board,posAct,PosDest),ListPiece]
                return [self.Piece_Move(board,posAct,PosDest),""]     
            if RowAct == RowDest and self.Validate_Queen_Horizontal(posAct,PosDest,ColorPiece,ColorPieceEne,board):
                if board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])] in ColorPieceEne:
                    print("Ate Piece")
                    return [self.Piece_Move(board,posAct,PosDest),ListPiece]
                return [self.Piece_Move(board,posAct,PosDest),""]     
            if ColumnAct == ColumnDest and self.Validate_Queen_Vertical(posAct,PosDest,ColorPiece,ColorPieceEne,board):
                if board[self.row.index(PosDest[0])] [self.column.index(PosDest[1])] in ColorPieceEne:
                    print("Ate Piece")
                    return [self.Piece_Move(board,posAct,PosDest),ListPiece]
                return [self.Piece_Move(board,posAct,PosDest),""]     
        else:
            print("invalid coordinate")
        return False