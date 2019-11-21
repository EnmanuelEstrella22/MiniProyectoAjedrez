from utilities import *

#metodos del tablero
class Chessboard(Utilities):

    # Generando el tablero sin piezas
    def Empty_Board(self):
        for row in range(0,8):
            Lpar=[chr(9633),chr(9632),chr(9633),chr(9632),chr(9633),chr(9632),chr(9633),chr(9632)]
            Limp=[chr(9632),chr(9633),chr(9632),chr(9633),chr(9632),chr(9633),chr(9632),chr(9633)]
            if self.par(row):
                Lpar.insert(0,8-row)
                self.Tablero.append(Lpar)
            else:
                Limp.insert(0,8-row)
                self.Tablero.append(Limp)
        self.Tablero.append(self.columna) 
        return self.Tablero

    # asignandole las piezas al tablero
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


    # mover pizas de posiciones
    def Piece_Move(self, t, f1, f2):
        filaAct  = self.fila.index(f1[0])
        columnaAct =self.columna.index(f1[1])
        filaDest= self.fila.index(f2[0])
        columnaDest =self.columna.index(f2[1])
        posicion = [filaAct, columnaAct]
        pieza1 = self.piezaTablero(posicion, self.Empty_Board())
        pieza2 = self.piezaAjedrez(posicion, t)
        t[filaAct][columnaAct] = pieza1
        t[filaDest][columnaDest] = pieza2
        return t        
