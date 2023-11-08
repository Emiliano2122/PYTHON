import random
import math
import os

def separa():
    print("")
    print("--------------")
    print("")

# Regla de negocios
#
# Juego: piedra, papel y tijera
# cantidad de jugadores: 2 jugadores
# con tiros alternos
# donde sale alternativamente 3 opciones
# piedra
# papel
# tijera
# donde:
# piedra gana a tijera
# tijera gana a papel
# papael gana a piedra
#
# Por cada turno que gane el jugador gana un purnto
# el primero que acumule tres puntos gana
# las tiradas se realizan hasta que salga un ganador por tirada

opciones = ["piedra", "papel", "tijera"]

# solicitar el nombre del jugador
# sacar opcion jugador1 y luego jugador2
# determinar el ganador
# puntosJugador
# hasta que el primer jugador llegue a 3 puntos


jugador1 = input("Dime tu mombre")
jugador2 = input("Dime tu nombre")

puntosJugador1 = 0
puntosJugador2 = 0

tiradasJugador1 = []
tiradasJugador2 = []

separa()

print("El jugador1 es:", jugador1)
print("El jugador2 es:", jugador2)

separa()

# temporal = input("tirada de:" + jugador1)

# print(opciones)
print(opciones[random.randint(0,2)])

separa()

while (puntosJugador1 <= 3) or (puntosJugador2 <= 3): # hasta que el primer jugador llegue a 3 puntos
    
    temporal = input("tirada de:" + jugador1)
    opcion1 = opciones[random.randint(0,2)]
    tiradasJugador1.append(opcion1)
    print(opcion1)
    
    temporal = input("tirada de:" + jugador2)
    opcion2 = opciones[random.randint(0,2)]
    tiradasJugador2.append(opcion2)
    print(opcion2)

# determina el ganador
# piedra gana tijera
# papel gana piedra
# tijera gana papael
    if opcion1 != opcion2:
        if opcion1 == "piedr" and opcion2 == "tijera":
            puntosJugador1 += 1
        elif opcion1 == "tijera" and opcion2 == "papel":
            puntosJugador1 += 1
        elif opcion1 == "papel" and opcion2 == "piedra":
            puntosJugador1 += 1
        elif opcion2 == "piedra" and opcion1 == "tijera":
            puntosJugador2 += 1
        elif opcion2 == "tijera" and opcion1 == "papel":
            puntosJugador2 += 1
        elif opcion2 == "papel" and opcion1 == "piedra":
            puntosJugador2 += 1
        
        print(jugador1, puntosJugador1)
        print(jugador2, puntosJugador2)
        
        if puntosJugador1 == 3 or puntosJugador2 == 3:
            break

print("")
if puntosJugador1 == 3:
    print("Gano :", jugador1)
else:
    print("Gano :", jugador2)

totalTiradas = len(tiradasJugador1 )

print(totalTiradas)

contador = 0

jugador1 = "Emiliano"
jugador2 = "Antonio"
# print("Tiradas\tEmiliano")
print("Tiradas" + "\t" + jugador1 + "\t" + jugador2)
print("===================================")

while contador <= (totalTiradas - 1):
    temporal = contador + 1
    print(str(temporal) + "\t" + tiradasJugador1[contador], "\t\t" + tiradasJugador2[contador])
    contador += 1

separa()