# Posiciones ganadoras
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# 1, 4, 7
# 2, 5, 8
# 3, 6, 9
# 1, 5, 9
# 3, 5, 7

opcionesJugador1 = [5, 3, 6]

opcionesJugador2 = [1, 7, 4]

def buscarEnArray(elemento, arreglo):
    try:
        existe = arreglo.index(elemento)
        existe = True
    except:
        existe = False
    return existe

buscar = 1
print(buscarEnArray(buscar, opcionesJugador2))

buscar = 4
print(buscarEnArray(buscar, opcionesJugador2))

buscar = 7
print(buscarEnArray(buscar, opcionesJugador2))

buscar1 = 1
buscar2 = 4
buscar3 = 7

print("")

if buscarEnArray(buscar1, opcionesJugador2) and buscarEnArray(buscar2, opcionesJugador2) and buscarEnArray(buscar3, opcionesJugador2):
    print("- = G A N A S T E = -")

if buscarEnArray(buscar1, opcionesJugador2) and buscarEnArray(buscar2, opcionesJugador2) and buscarEnArray(buscar3, opcionesJugador2):
    print("- = G A N A S T E = -")

def buscarGanador(opciones):
    print(opciones)
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

opcionesJugador1 = [5]

opcionesJugador2 = [1]

print(buscarGanador(opcionesJugador1))
print(buscarGanador(opcionesJugador2))

opcionesJugador1 = [5, 3]

opcionesJugador2 = [1, 7]

print(buscarGanador(opcionesJugador1))
print(buscarGanador(opcionesJugador2))

opcionesJugador1 = [5, 3, 6]

opcionesJugador2 = [1, 7, 4]

print(buscarGanador(opcionesJugador1))
print(buscarGanador(opcionesJugador2))
