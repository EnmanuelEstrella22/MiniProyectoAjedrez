class Utilities():

    # Constructor
    def __init__(self):
        self.Lpar = [chr(9633), chr(9632), chr(9633), chr(
            9632), chr(9633), chr(9632), chr(9633), chr(9632)]
        self.Limp = [chr(9632), chr(9633), chr(9632), chr(
            9633), chr(9632), chr(9633), chr(9632), chr(9633)]
        self.Tablero = []
        self.FBlack = ['', chr(9819), chr(9823)]
        self.FWhite = ['', chr(9813), chr(9817)]
        self.columna = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.fila = [8, 7, 6, 5, 4, 3, 2, 1, 0]

        
    #metodo par
    def par(self, n):
        if n % 2 == 0:
            return True
        return False

    # imprimir tablero
    def Print_Board(self,t,LB,LW):

        print()
        for LisN in LB:
            print(LisN, end=' ')
        print()
        print("_________________")
        print()

        for items in t:
            for i in items:
                print(i, end=' ')
            print()

        print("_________________")
        for LisN in LW:
            print(LisN, end=' ')
        print()

    # Buscar esa pieza en el tablero sin piezas
    def piezaTablero(self, p,t):
        return t[p[0]][p[1]]

    # Buscar esa pieza en el tablero pero con las fichas colocadas
    def piezaAjedrez(self, p, t):
        return t[p[0]][p[1]]

#validacion al mover la ficha
    def ValidarFichas(self,f1,f2,tablero,ColorF):
        filaAct  = self.fila.index(f1[0])
        columnaAct =self.columna.index(f1[1])
        filaDest= self.fila.index(f2[0])
        columnaDest =self.columna.index(f2[1])
        if tablero[filaAct][columnaAct] not in ColorF :
            print("No es su ficha")
            return False
        elif  tablero[filaDest][columnaDest] in ColorF:
            print("no puede moverse porque hay una ficha de su equipo en esa posicion")
            return False
        return True  


# recorriendo coordenadas por donde pasara la ficha
    def cicloRecorrido(self,f1,f2,colorF,tablero):
        filaAct  = self.fila.index(f1[0])
        filaDest= self.fila.index(f2[0])
        columnaDest =self.columna.index(f2[1])
        for items in range(int(filaDest),int(filaAct)):
            if tablero[items][columnaDest] in colorF:
                print("No puede volar ficha de su equipo")
                return False
        return True 

    #Validar movimiento de la reina en diagonal secundaria
    def ValidarReinaDiagonalSecundaria(self,f1,f2,colorF,tablero):
        filaAct  = self.fila.index(f1[0])
        filaDest= self.fila.index(f2[0])
        columnaDest =self.columna.index(f2[1])
        contC = columnaDest
        if filaDest < filaAct:#para que tambien valide al moverse para atras
            for f in range(int(filaDest),int(filaAct)):
                if tablero[f][contC] in colorF:
                    print("No puede volar ficha de su equipo")
                    return False
                contC -= 1
            return True  
        else:
            for f in range(int(filaAct+1),int(filaDest+1)):
                if tablero[f][contC] in colorF:
                    print("No puede volar ficha de su equipo")
                    return False
                contC -= 1
            return True

    #Validar movimiento de la reina en diagonal principal
    def ValidarReinaDiagonalPrincipal(self,f1,f2,colorF,tablero):
        filaAct  = self.fila.index(f1[0])
        filaDest= self.fila.index(f2[0])
        columnaDest =self.columna.index(f2[1])
        contC = columnaDest
        if filaDest < filaAct:#para que tambien valide al moverse para atras
            for f in range(int(filaDest),int(filaAct)):
                if tablero[f][contC] in colorF:
                    print("No puede volar ficha de su equipo")
                    return False
                contC += 1
            return True 
        else:
            for f in range(int(filaAct+1),int(filaDest+1)):
                if tablero[f][contC] in colorF:
                    print("No puede volar ficha de su equipo")
                    return False
                contC += 1
            return True 

    #Validar movimiento de la reina en vertical
    def ValidarReinaVertical(self,f1,f2,colorF,tablero):
        filaAct  = self.fila.index(f1[0])
        filaDest= self.fila.index(f2[0])
        columnaDest =self.columna.index(f2[1])
        if filaDest < filaAct:#para que tambien valide al moverse para atras
            for f in range(int(filaDest),int(filaAct)):
                if tablero[f][columnaDest] in colorF:
                    print("No puede volar ficha de su equipo")
                    return False
            return True 
        else:
            for f in range(int(filaAct+1),int(filaDest+1)):
                if tablero[f][columnaDest] in colorF:
                    print("No puede volar ficha de su equipo")
                    return False
            return True

    #Validar movimiento de la reina en orizontal
    def ValidarReinaOrizontal(self,f1,f2,colorF,tablero):
        filaAct  = self.fila.index(f1[0])
        columnaDest =self.columna.index(f2[1])
        if filaAct < columnaDest:#para que tambien valide al moverse para atras
            for f in range(int(filaAct+1),int(columnaDest+1)):
                if tablero[filaAct][f] in colorF:
                    print("No puede volar ficha1")
                    return False
            return True  
        else:
            for f in range(int(columnaDest),int(filaAct)):
                if tablero[filaAct][f] in colorF:
                    print("No puede volar ficha2")
                    return False
            return True           