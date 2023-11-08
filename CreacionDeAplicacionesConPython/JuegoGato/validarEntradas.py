def separa():
    print("")
    print("-------------------")
    print("")

# este es un numero
a = 5

# este es un texto
b = "5"

# las operaciones matematicas SOLO SON ENTRE NUMEROS (enteros y/o con decimales)
# print("suma ", a + b)

# TODO LO QUE ESCRIBE EL USUSARIO ES TEXTO
#                                    =====

# numero = input("Dime un número: ") # lo que escriba el usuario es TEXTO

# numeroOk = int(numero) # convierto el TEXTO que escribio el usuario a NUMERO ENTEROS sin desimales
# numeroOk = float(numero) # convierto el TEXTO que escribio el usuario a NUMERO CON DECIMALES

# print(int(numeroOk)) # convierto FLOAT a INT

# print(numeroOk / 3) # realizo un operacion con NUMEROS

# posicionOk = int(posicion)

# print(posicionOk)

posicion = input("Dime un numero entre [1 - 9]")

try:
    posicionOk = (float(posicion))
except:
    print("")
    print("Ingresa un numero entre [1 - 9]")
    posicion = input("Dime un numero entre [1 - 9]")

if posicionOk > 9 or posicionOk < 1:
    print("")
    print("Ingresa un numero entre [1 - 9]")
    posicion = input("Dime un numero entre [1 - 9]")
    