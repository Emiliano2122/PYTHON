#Bola Magica

from random import *
from os import *

respuestas = ["Si", "No", "Tal ves", "Probablemente", "Jamas", "Puede ser"]

option = "si"

def calcularRespuesta():
	resultado = choice(respuestas)
	return resultado

while(option != "no"):
	print("Este programa adivina tu futuro")
	aux = input("Ingresa tu pregunta: \n")
	print(calcularRespuesta())

	option = input("Desea hacer otra pregunta: [si/no]")
	
	system("cls")

print("Gracias por jugar!")
		
