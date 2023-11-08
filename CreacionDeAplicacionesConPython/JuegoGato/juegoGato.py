import random
import math
import os

def separa():
    print("")
    print("--------------")
    print("")

def interface():
    print(" "+ posiciones[1] +  "  | " + posiciones[2] +" | " + posiciones[3] +" ")
    print(" ---+---+---")
    print(" "+ posiciones[4] + "  | " + posiciones[5] +" | " + posiciones[6] +" ")
    print(" ---+---+---")
    print(" "+ posiciones[7] + "  | " + posiciones[8] +" | " + posiciones[9] +" ")
    

def ubicaciones():
    print("Posible ubicaciones")
    print("")
    print(" 1 | 2 | 3 ")
    print(" --+---+---")
    print(" 4 | 5 | 6 ")
    print(" --+---+---")
    print(" 7 | 8 | 9 ")
    
def buscarEnArray(elemento, arreglo):
    try:
        existe = arreglo.index(elemento)
        existe = True
    except:
        existe = False
    return existe

def buscarGanador(opciones):
    # print(opciones)
    if buscarEnArray(1, opciones) and buscarEnArray(2, opciones) and buscarEnArray(3, opciones):
        return True
    elif buscarEnArray(4, opciones) and buscarEnArray(5, opciones) and buscarEnArray(6, opciones):
        return True
    elif buscarEnArray(7, opciones) and buscarEnArray(8, opciones) and buscarEnArray(9, opciones):
        return True
    elif buscarEnArray(1, opciones) and buscarEnArray(4, opciones) and buscarEnArray(7, opciones):
        return True
    elif buscarEnArray(2, opciones) and buscarEnArray(5, opciones) and buscarEnArray(8, opciones):
        return True
    elif buscarEnArray(3, opciones) and buscarEnArray(6, opciones) and buscarEnArray(9, opciones):
        return True
    elif buscarEnArray(1, opciones) and buscarEnArray(5, opciones) and buscarEnArray(9, opciones):
        return True
    elif buscarEnArray(3, opciones) and buscarEnArray(5, opciones) and buscarEnArray(7, opciones):
        return True
    else:
        return False

posiciones = [10]
posiciones = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " ]
#              0    1    2    3    4    5    6    7    8    9    10





# Regla de negocios
#
# Juego: X, O
# Cantidad de jugadores: 2 personas
# Con tiros alternos
# En donde se ponene 3 x en tres recuadros
# X
# O
# POSICIONES
#
# 1 | 2 | 3
# --+---+--
# 4 | 5 | 6
# --+---+--
# 7 | 8 | 9
# --+---+--
#
# Posiciones ganadoras
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# 1, 4, 7
# 2, 5, 8
# 3, 6, 9
# 1, 5, 9
# 3, 5, 7

# PROCESOS
# imprimir interface OK
# posiciones OK
# solicitar el nombre del jugador ** OK
# solicitar opciones de los jugadores **** OK
# no permitir posiciones ya selecionados por el otro jugador ***
# no permitir posiciones ya selecionadas por mi ***
# mostrar las opciones de los jugadores despues de cada seleccion OK
# guardar las seleciones de los jugadores ******* OK
# definir el ganador ***
#

# PROGRAMACION

ubicaciones()

separa()

interface()

separa()

jugador1 = ""
jugador2 = ""

print("\t\t\t\t\t * para terminar el juego")
while jugador1 == "" and jugador2 == "":
    if jugador1 == "":
        jugador1 = input("Jugador 1 dame tu nombre ")
        if jugador1 == "*":
            quit()
    if jugador2 == "":
        jugador2 = input("Jugador 2 dame tu nombre ")
        if jugador2 == "*":
            quit()
    print("")


opcionesJugador1 = []
opcionesJugador2 = []

# print(poscion)
tiradas = 1
while tiradas <= 4:
    # ubicacion = input(jugador1 + " Dime tu posicion: ")
    
    ubicacionOk = 0
    while ubicacionOk > 9 or ubicacionOk < 1:
        ubicacion = input(jugador1 +" dame un numero entre [1 - 9] ")
        if ubicacion == "*":
            break
    
        try:
            ubicacionOk = int((float(ubicacion)))
        except:
            ubicacionOk = 0
            print("")
            print("Se termina con asterisco")
        if buscarEnArray(ubicacionOk, opcionesJugador1):
            print("No se puede escojer una ubicacion ya seleccionada por ti.")
            ubicacionOk = 0
        if buscarEnArray(ubicacionOk, opcionesJugador2):
            print("No se puede escojer una ubicacion ya seleccionada por el otra jugador.")
            ubicacionOk = 0
        print("")
    
    posiciones[int(ubicacion)] = "x"
    opcionesJugador1.append(int(ubicacion))
    if buscarGanador(opcionesJugador1):
        print(jugador1 + "- = G A N A S T E = -")
    
    ubicacionOk = 0
    while ubicacionOk > 9 or ubicacionOk < 1:
        ubicacion = input(jugador2 +" dame un numero entre [1 - 9] ")
        if ubicacion == "*":
            break
    
        try:
            ubicacionOk = int((float(ubicacion)))
        except:
            ubicacionOk = 0
            print("")
            print("Se termina con asterisco")
    posiciones[int(ubicacion)] = "o"
    opcionesJugador2.append(int(ubicacion))
    if buscarGanador(opcionesJugador2):
        print(jugador2 + "- = G A N A S T E = -")
    
    
    tiradas += 1
    ubicaciones()
    interface()

print("")
print("posiciones del Jugador1")
print(opcionesJugador1)
print("")
print("posiciones del Jugador2")
print(opcionesJugador2)


# print(posiciones)






    
   
