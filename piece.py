from board import *

# metodos de la reina y el peon
class Piece(Chessboard):

    #metodo para establecer las reglas y los movimientos del peon
    def Peon(self,posActual,AdondeVa,tablero,ColorFicha,ColorFichaEne,num1,num2,num3):
        fiA = self.fila.index(posActual[0])
        coA = self.columna.index(posActual[1])
        fiVa = self.fila.index(AdondeVa[0])
        coVa = self.columna.index(AdondeVa[1])
        listado = (tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])])
        if AdondeVa[1] != posActual[1]:
            if fiA + coA == fiVa + coVa or fiA - coA == fiVa - coVa and abs(self.fila.index(AdondeVa[0]) - self.fila.index(posActual[0])) == 1:
                if self.ValidarFichas(posActual,AdondeVa,tablero,ColorFicha):
                    if tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])] in ColorFichaEne:
                         print("comio ficha") 
                         return [self.Piece_Move(tablero,posActual,AdondeVa),listado]
                    else:
                        print("No tiene ficha para comer")
            else:  
                print("El Peon solo se mueve verticalmente")
        elif self.fila.index(posActual[0]) == num1 :
            if self.fila.index(posActual[0])+self.fila.index(AdondeVa[0]) > num2 and self.fila.index(posActual[0])+self.fila.index(AdondeVa[0]) < num3 and  tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])] not in ColorFichaEne:  
                if self.cicloRecorrido(posActual,AdondeVa,ColorFichaEne,tablero):
                    return [self.Piece_Move(tablero,posActual,AdondeVa),""]      
            else: 
                print("Movimiento invalido")
        else:#validar que se mueva solo un paso a delante si ya salio de su posicion
            if num1 != 6: #Si no es ficha blanca
                if self.fila.index(AdondeVa[0]) > self.fila.index(posActual[0]) and self.fila.index(AdondeVa[0]) - self.fila.index(posActual[0]) == 1 and  tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])] not in ColorFichaEne:       
                    if self.ValidarFichas(posActual,AdondeVa,tablero,ColorFicha):
                        return [self.Piece_Move(tablero,posActual,AdondeVa),""]
                else: 
                    print("Movimiento invalido")
            else: 
                if self.fila.index(AdondeVa[0]) < self.fila.index(posActual[0]) and abs(self.fila.index(AdondeVa[0]) - self.fila.index(posActual[0])) == 1 and  tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])] not in ColorFichaEne:       
                    if self.ValidarFichas(posActual,AdondeVa,tablero,ColorFicha):
                        return [self.Piece_Move(tablero,posActual,AdondeVa),""]
                else: 
                    print("Movimiento invalido")   
        return False 


    #metodo para establecer las reglas y los movimientos de la reina
    def Reina(self,posActual,AdondeVa,tablero,ColorFicha,ColoFichaE):

        fiA = self.fila.index(posActual[0])
        coA = self.columna.index(posActual[1])
        fiVa = self.fila.index(AdondeVa[0])
        coVa = self.columna.index(AdondeVa[1])
        listado = (tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])])
        if fiA == fiVa  or coA == coVa   or fiA + coA == fiVa + coVa or fiA - coA == fiVa - coVa:      
            if fiA + coA == fiVa + coVa and self.ValidarReinaDiagonalSecundaria(posActual,AdondeVa,ColorFicha,tablero):
                 if tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])] in ColoFichaE:
                    print("comio ficha")
                    return [self.Piece_Move(tablero,posActual,AdondeVa),listado]
                 return [self.Piece_Move(tablero,posActual,AdondeVa),""]   
            if fiA - coA == fiVa - coVa and self.ValidarReinaDiagonalPrincipal(posActual,AdondeVa,ColorFicha,tablero):
                if tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])] in ColoFichaE:
                    print("comio ficha")
                    return [self.Piece_Move(tablero,posActual,AdondeVa),listado]
                return [self.Piece_Move(tablero,posActual,AdondeVa),""]     
            if fiA == fiVa and self.ValidarReinaOrizontal(posActual,AdondeVa,ColorFicha,tablero):
                if tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])] in ColoFichaE:
                    print("comio ficha")
                    return [self.Piece_Move(tablero,posActual,AdondeVa),listado]
                return [self.Piece_Move(tablero,posActual,AdondeVa),""]     
            if coA == coVa and self.ValidarReinaVertical(posActual,AdondeVa,ColorFicha,tablero):
                if tablero[self.fila.index(AdondeVa[0])] [self.columna.index(AdondeVa[1])] in ColoFichaE:
                    print("comio ficha")
                    return [self.Piece_Move(tablero,posActual,AdondeVa),listado]
                return [self.Piece_Move(tablero,posActual,AdondeVa),""]     
        else:
            print("Coordenada invalina")
        return False