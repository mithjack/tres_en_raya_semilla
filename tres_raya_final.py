import utilidades

###############
# 1 - TABLERO
###############

# esto reprenta un tablero de 3x3 del 3 en raya
# y lo queremos convertir en una lista de python
linea1 = "XO-"
linea2 = "-O-"
linea3 = "XOX"

tablero_cutre = [linea1, linea2, linea3]

#######################################
# 2 - CONVERSIÓN A LISTAS DE PYTHON
#######################################

# TODO: Conviertelo en una lista (como la de abajo)
# tablero = [ [1, -1, 0], [0, -1, 0], [1, -1, 1] ]

tablero = utilidades.convertir_tablero(tablero_cutre)
utilidades.mostrar_tablero(tablero)

##########################
# 3 - COMPROBAR GANADOR
##########################
# TODO: Y ahora haz un algoritmo que, a partir de una posición, (ej. 0, 1, que contiene una O)
# compruebe si hay ganador.

# Deberiamos mirar 3 cosas:
# La propia línea ----> XO- = No hay ganador
# La propia columna --> OOO = Hay ganador
# La/s diagonales ----> En este caso esa posición no está en una diagonal
hay_ganador = utilidades.comprobar_ganador(0, 1, tablero)
print(hay_ganador)