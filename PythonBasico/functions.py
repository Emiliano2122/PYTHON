def separa():
    print()
    print("----------")
    print()

def bienvenida():
    print("Hola, bienvenida al curso de python")
    print(":)")
    print()

def saludarA(usuario):
    print("Hola " + usuario + ", bienvenida(o) al curso de python")
    
def nombreCompleto(nom, pat, mat):
    nombre = nom + " " + pat + " " + mat
    return nombre

def nombreCompletoEscuela(nombre, paterno, materno):
    nombre = paterno + " " + materno + " " + nombre
    return(nombre)

print("hola")
separa()
print("asd")
separa()
print("qwe")
separa()

bienvenida()
bienvenida()
bienvenida()

saludarA("Antonio")
saludarA("Emiliano")
saludarA("Eosamelia")

separa()

nc = nombreCompleto("Emiliano", "Stasi", "Fernandez")

print(nc)

separa()

nc = nombreCompletoEscuela("Emiliano", "Stasi", "Fernandez")

print(nc)

separa()

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

asd = suma(5, 8)

print(asd)

separa()

def resta(num1, num2):
    resultado = num1 - num2
    return resultado

asd = resta(4, 7)

print(asd)

separa()


def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

asd = multiplicacion(20, 50)

print(asd)

separa()

def division(num1, num2):
    resultado = num1 / num2
    return resultado

asd = division(7, 9)

print(asd)

separa()







