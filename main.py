from piece import *

# clase de iniciar el juego
class Play(Piece):
    cont = 0
    tablero = Piece().Piece_Board(Piece().Empty_Board())
    colum =['','a','b','c','d','e','f','g','h']
    fil =[8,7,6,5,4,3,2,1,0]
    jugador1 = input("Introduzca nombre del jugador 1: ")
    jugador2 = input("Introduzca nombre del jugador 2: ")
    lb = []
    lw = []
    Piece().Print_Board(tablero,lb,lw)

    while True:
        try:
            if cont % 2 == 0:
                print("Turno: "+jugador1)
                print("Fichas: Blancas")
            else:
                print("Turno: "+jugador2)
                print("Fichas: Negras")
            a1 =input("Seleccionar ficha: ")
            a2 =input("Movimiento: ")    
            columna=a1[0]
            fila1=int(a1[1])
            columna1=a2[0]
            fila2=int(a2[1])
            pos=[fila1,columna]
            pos1=[fila2,columna1]
            tab1 = tablero
            if cont % 2 == 0:
                #PARA FICHAS BLANCAS
                
                if tablero[fil.index(pos[0])] [colum.index(pos[1])] == chr(9817):

                    tablero =  Piece().Peon(pos,pos1,tablero,Piece().FWhite,Piece().FBlack,6,9,13)
                    if tablero != False:
                        cont += 1
                        if tablero[1] != "":
                            lw.append(tablero[1])
                        tablero = tablero[0]    
                    else:
                        tablero = tab1  

                elif  tablero[fil.index(pos[0])] [colum.index(pos[1])] == chr(9813):
                
                    tablero = Piece().Reina(pos,pos1,tablero,Piece().FWhite,Piece().FBlack)
                    if tablero != False:
                        cont += 1
                        if tablero[1] != "":
                            lw.append(tablero[1])
                        tablero = tablero[0]  
                    else:
                        tablero = tab1 
                else:
                    print("No es una ficha blanca")  
            else:   
                #PARA FICHAS NEGRAS
                
                if tablero[fil.index(pos[0])] [colum.index(pos[1])] == chr(9823):

                    tablero =  Piece().Peon(pos,pos1,tablero,Piece().FWhite,Piece().FBlack,1,1,5)
                    if tablero != False:
                        cont += 1
                        if tablero[1] != "":
                            lb.append(tablero[1])
                        tablero = tablero[0]  
                    else:
                        tablero = tab1 
                elif  tablero[fil.index(pos[0])] [colum.index(pos[1])] == chr(9819):

                    tablero = Piece().Reina(pos,pos1,tablero,Piece().FBlack,Piece().FWhite)
                    if tablero != False:
                        cont += 1
                        if tablero[1] != "":
                            lb.append(tablero[1])
                        tablero = tablero[0]  
                    else:
                        tablero = tab1 
                else:
                    print("No es una ficha Negra")    

            Piece().Print_Board(tablero,lb,lw)
        except (ValueError,IndexError):print("Coordenada incorrecta. Intente nuevamente...")     


Play()

