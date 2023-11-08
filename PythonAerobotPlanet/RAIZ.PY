#Raiz

# a es el numero que quiero obtener la raiz
# b es el numero de la potencia de la raiz
opcion = "si"

#16^1/2
#16^1/3
#Funcion que calcule la raiz
def raiz(a, b):
	aux = 1/b
	resultado = a**aux
	return resultado


while(opcion != "no"):
	print("Raiz")
	a = int(input("Ingrese el n umero base "))
	b = int(input("Ingrese la potensia de la raiz "))
	print("El resultado es " , raiz(a, b))

	ocpion = input("Desea hacer otra operacion [si/no] ")
