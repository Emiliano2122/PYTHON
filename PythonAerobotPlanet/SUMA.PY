#Suma

opcion = "si"

def suma(a, b):
	resultado = a + b
	return resultado

while(opcion != "no"):
    print("Suma")
    a= int(input("Ingrese el primer numero "))
    b= int(input("Ingrese el segundo valor "))
    print("El resultado es " , suma(a, b))

    opcion = input("Desea hacer otra suma [si/no] ")
