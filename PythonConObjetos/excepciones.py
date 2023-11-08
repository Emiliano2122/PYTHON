def separa():
    print("")
    print("---------")
    print("")

# departamento
# QA

# puesto
# tester

# manejo de excepciones

a = 8
b = 0

# ZeroDivisionError: division by zero
# c = a / b

# NameError: name 'd' is not defined
# c = a * d

genaros = ["femenino", "masculino"]

# IndexError: list index out of range
# print(genaros[2])

# FileNotFoundError: [Errno 2] No such file or directory: 'demoFile.txt'
# file = open("demoFile.txt")
# file.write("Lorem Ipsum")



# para el manejo de excepciones utilizamos
# try

a = 8
b = 0

try:
    c = a / b
except:
    print("Error al tratar de  realiza la division")
    c = 0

print(c)

try:
    generoActual = generos[2]
except:
    generoActual = "N/A"

print(generoActual)

separa()

# d = 77228879

try:
    file = open("demoFile.txt")
    file.write("Lorem Ipsum")
except:
    print("No se puede escribir el archivo. Contactar con el administrador del sistema")

separa()

try:
    print(d)
except:
    print("Variable no definida")
    d = 0
    print("Defino variable con valor inicial de: 0")
finally:
    print("Termina bloque de experiencia")

separa()

importe = 1000
IVA = 0.16


if importe > 0:
    importeIVA = importe * IVA
    total = importe + importeIVA
else:
    importe = 0
    importeIVA = 0
    total = 0

print(importe)
print(importeIVA)
print(total)

separa()

x = -1

# puedo genarar un error
if x < 0:
    raise Exception("Lo siento no se permiten valores negativos")

y = "Emiliano"

if not type(y) in int:
    raise TypeError("Solo se permiten numeros")


