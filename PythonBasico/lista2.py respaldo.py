def separa():
    print()
    print("----------")
    print()

# define una list implicita

misFrutas = ["platano", "piña", "melon", "papaya", "uva"]

print(misFrutas)

separa()

misColores = ["Black", "Read", "Blue", "Pink", "Orange"]

print(misColores)

separa()

misCalificaciones = [8, 10,10, 7, 9]

print(misCalificaciones)

separa()

estatus = [False, True, True]

print(estatus)

separa()

datosInicio = [1, "Emiliano", True, "M"] # entre corchetes

print(datosInicio)

separa()

# defino una list explicitamente
vocales = list(("a", "e", "i", "o", "u")) # entre parentesis

print(vocales)

separa()

print(type(datosInicio))
print(type(vocales))

separa()

print(len(misFrutas))

separa()

longDatosInicio = (len(datosInicio))

print(datosInicio)
print(longDatosInicio)

separa()

print(vocales)
print(vocales[0])
print(vocales[4])

separa()

vocales[2] = "melon"
print(vocales)

separa()

misColores.insert(5, "brown")
print(misColores)

separa()

misColores.insert(3, "peru")
print(misColores)

separa()

misColores.append("gris")
print(misColores)

separa()

coloresPrimarios = ["rojo", "amarillo", "azul"]
misColores.extend(coloresPrimarios)

print(misColores)

separa()

misColores.remove("gris")
print(misColores)

separa()

#misColores.remove("Azul")
print(misColores)

separa()

misColores.pop(4)
print(misColores)

separa()

misColores.pop()
print(misColores)

separa()


del misColores[3]
print(misColores)

separa()

misColores.clear()
print(misColores)

separa()

#del misColores
print(misColores)

separa()

numero = input("Dime los numeros entre el 1 al 9: ")

# print(numero)
# print(type(numero))
numero = int(numero)

if numero == 1:
    print("uno")
elif numero ==  2:
    print("dos")
elif numero == 3:
    print("tres")
elif numero == 4:
    print("cuatro")
elif numero == 5:
    print("cinco")
elif numero == 6:
    print("seis")
elif numero == 7:
    print("siete")
elif numero == 8:
    print("ocho")
elif numero == 9:
    print("nueve")
else:
    print("Fuera de rango")

separa()

unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]

numero = input("Dime un numero entre 1 al 9: ")

numero = int(numero)
print(unidades[numero])

separa()
