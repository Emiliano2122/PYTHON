def buscarEnArray(elemento, arreglo):
    try:
        existe = arreglo.index(elemento)
        existe = True
    except:
        existe = False
    return existe

opcionesJugador1 = [5, 4]
opcionesJugador2 = [1, 2]

print(opcionesJugador1)
print(opcionesJugador2)

buscar = int(float(input("Elemnto a buscar: ")))

print(buscarEnArray(buscar, opcionesJugador1))

print(buscarEnArray(buscar, opcionesJugador2))