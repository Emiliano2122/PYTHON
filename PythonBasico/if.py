# operadores logicos
# >
# <
# >=
# <=
# ==
# !=

def separa():
    print("")
    print(".........................")
    print("          -o-")
    print("")


otroEjercicio = "...................."
calificacion = 8

if calificacion >= 6:
    print("Aprobado")
    print("alumno")
    print("Sobresaliente")

if calificacion <6:
    print("No aprobado")

if calificacion >=6:
    print("ok")
    print("o sea que aprobo")
else:
    print("No ok")
    print("No aprobo")

separa()

print("Calificacion", calificacion)
print(" ")
if calificacion !=10:
    print("No es 10")

separa()


numero = 5
texto = "5"

if numero == texto:
    print("son iguales")
else:
    print("No son iguales")

separa()

if numero == int(texto):
    print("Son identicos")
    
separa()

if str(numero) == texto:
    print("son i g u a l e s")

separa()

print(True)

separa()

print(False)

separa()

if True == 1:
    print("True es 1")

separa()

if False == 0:
    print("False es 0")
separa()

if calificacion == 10:
    print("Tu calificacion es 10")
    separa()    
if calificacion == 9:
    print("Tu calificacion es 9")
    separa()    
if calificacion == 8:
    print("Tu calificacion es 8")
    separa()   
if calificacion == 7:
    print("Tu calificacion es 7")
    separa()  
if calificacion == 6:
    print("Tu calificacion es 6")
    separa()
if calificacion <6:
    print("No aprobaste")
    separa()

separa()

if calificacion < 6:
    print("No Aprobado")
else:
    print("Aprobado")
    if calificacion == 6:
        print("Tu calificacion es Seis")
    elif calificacion == 7:
        print("Tu calificacion es Siete")
    elif calificacion == 8:
        print("Tu cañificacion es Ocho")
    elif calificacion == 9:
        print("Tu calificacion es Nueve")
    else: 
        print("Tu calificacion es Diez")

separa()

a = 330
b = 200

#utilizar pass cuando en un if NO QUIERO EJECUTAR ALGO
# y pass Evita el error
if a>b:
    pass

separa()

