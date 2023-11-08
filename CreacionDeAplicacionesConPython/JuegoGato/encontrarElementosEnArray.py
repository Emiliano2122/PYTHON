def separa():
    print("")
    print("--------------")
    print("")

# buscar un elemento dado dentro de un array
#

vocales = ["a", "e", "i", "o", "u"]

print(vocales)

# print(vocales.index("e"))

# encontrar = input("Letra a buscar: ")

# print(vocales.index(encontrar))

buscar = input("Letra a buscar: ")

try:
    existe = vocales.index(buscar)
    existe = True
except:
    existe = False

print(existe)

opcionesJugador1 = [5, 4]
opcionesJugador2 = [1, 2]

try:
    existe = opcionesJugador1.index(4)
    existe = True
except:
    existe = False

print(existe,"en el jugador1")

try:
    existe = opcionesJugador2.index(4)
    existe = True
except:
    existe = False

print(existe,"en el jugador2")

separa()

buscar = 4

try:
    existe = opcionesJugador1.index(buscar)
    existe = True
except:
    existe = False

print(existe, "en el jugador1")

try:
    existe = opcionesJugador2.index(buscar)
    existe = True
except:
    existe = False

print(existe, "en el jugador2")

def buscarEnArray(elemento, arreglo):
    try:
        existe = arreglo.index(elemento)
        existe = True
    except:
        existe = False
    return existe




