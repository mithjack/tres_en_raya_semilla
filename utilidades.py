# TODO: Y ahora haz un algoritmo que, a partir de una posición, (ej. 0, 1, que contiene una O)
# compruebe si hay ganador.

# Deberiamos mirar 3 cosas:
# La propia línea ----> XO- = No hay ganador
# La propia columna --> OOO = Hay ganador
# La/s diagonales ----> En este caso esa posición no está en una diagonal
def comprobar_ganador(x, y, tablero):

    # ¿Qué casilla tenemos que comprobar?
    jugador = tablero[x][y]
    print(f"Voy a comprobar {jugador} en  {x},{y}")

    ##########################################
    # Miramos hacia la izquierda y derecha
    victoria_lateral = True

    for num in range(0,3,1):
        if tablero[x][num] != jugador:
            victoria_lateral = False

    if victoria_lateral:
        print("Tres en raya, Linea")
        return True
    
    print("No hay Linea")

    ##########################################
    # Miramos hacia abajo
    victoria_columna = True

    # TODO: comprobacion
    for num in range(0,3,1):
        if tablero[num][y] != jugador:
            victoria_columna = False

    if victoria_columna:
        print("Tres en raya, Columna")
        return True
    print("No hay Columna")
    
    ##########################################
    # Diagonal
    victoria_diagonal = True

    if (x == y) or (x + y == 2):
        print("Compruebo diagonal")
        encontrado = True
        for num in range(0,3,1):
            if tablero[num][num] != jugador:
                encontrado = False
        if encontrado == False:
            for num in range(0,3,1):
                if tablero[2-num][num] != jugador:
                    victoria_diagonal = False
                else:
                    encontrado = True

    else:
        victoria_diagonal = False
        print("No hay Diagonal")

    return victoria_diagonal


def mostrar_tablero(tablero):
    for linea in tablero:
        print(linea)


def convertir_tablero(tablero):
    nuevo_tablero = []
    for x in tablero:
        tablero_format=[]
        for y in x:
            tablero_format.append(1 if y == "X" else (-1 if y == "O" else 0 ))
        nuevo_tablero.append(tablero_format)

    return nuevo_tablero
