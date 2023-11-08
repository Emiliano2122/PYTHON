#Gato
'''
Ivan Jesus Vazquez Rivera


El programa simula el juego del gato (tic tac toe)

_|_|_
_|_|_
 | |

'''

#Se importan las librearias os y sys para trabajar con la consola de comandos
from os import *
from sys import *

#Se define un arreglo bidimensional (matriz)
#Se dej un espacio para ponder crear el tablero de juego
board = [[" "," "," "],[" "," "," "],[" "," "," "]]

#Variable player para saber el turno
player = 1

#Funcion que imprime el tablero de juego
#Para recorrer una matriz se utiliza dos for anidados
def printBoard(board):
	print("   0    1    2  ")
	print(" ---------------")
	for i in range(0,3):
		print(i, end = "")
		#La función .format() sirve para entregar un String y que imprima un texto
		for j in range(0,3):
			print("| {} |".format(board[i][j]), end = "")
		print("")
		print(" ", end = "")
		for k in range(0,3):
			print("-----", end = "")
		print("")

#Funcion que revisa si se ha ganado.
#Revisa cada posible caso por las que se puede ganar

def ganador(board):
	#Filas 
	if((board[0][0]==board[0][1]==board[0][2] == "x") or (board[0][0]==board[0][1]==board[0][2] == "o")):
		return False
	elif(board[1][0]==board[1][1]==board[1][2] == "x") or (board[1][0]==board[1][1]==board[1][2] == "o"):
		return False
	elif(board[2][0]==board[2][1]==board[2][2] == "x") or (board[2][0]==board[2][1]==board[2][2] == "o"):
		return False
	#Columas
	elif(board[0][0]==board[1][0]==board[2][0] == "x") or (board[0][0]==board[1][0]==board[2][0] == "o"):
		return False
	elif(board[0][1]==board[1][1]==board[2][1] == "x") or (board[0][1]==board[1][1]==board[2][1] == "o"):
		return False
	elif(board[0][2]==board[1][2]==board[2][2] == "x") or (board[0][2]==board[1][2]==board[2][2] == "o"):
		return False
	#Cruz
	elif(board[0][0]==board[1][1]==board[2][2] == "x") or (board[0][0]==board[1][1]==board[2][2] == "o"):
		return False
	elif(board[0][2]==board[1][1]==board[2][0] == "x") or (board[0][2]==board[1][1]==board[2][0] == "o"):
		return False
	else:
		return True

#Funcion que dibuja el simbolo en el tablero
def fillPosition(board, x ,y, player):
	if(board[x][y] == " "):
		if(player == 1):
			board[x][y] = "x"
		else:
			board[x][y] = "o"
	else:
		print("No valido")

#Funcion que revisa si el tablero esta lleno
def isFull(board):
	for i in range(0,3):
		for j  in range(0,3):
			#Si la función encuentra un espacio vacio significa que todavia hay espacio en el tablero
			if(board[i][j] == " "):
				return
	
	#Si hay espacio libre se limpia la pantalla y se pone un empate. Se termina el programa
	system("cls")
	print("Empate")
	printBoard(board)
	exit()


print("Gato")

#Condicion que se cumple mientras no haga ganador
while(ganador(board)):
	printBoard(board)

	print("Jugador ", player)

	x = int(input("Ingresa el valor en x: "))
	y = int(input("Ingresa el valor en y: "))


	#Verificamos que los valores que nos den esten dentro del rango establcido
	if(x > 2 or x < 0 or y > 2 or y < 0):
		print("No valido")
	else:
		fillPosition(board,x,y,player)

	isFull(board)
	#Se cambia el jugador para que hacer turnos del jugador 1 y jugador 2
	if(player == 1):
		player = 2
	else:
		player = 1


#Hay que regresar el turno correcto antes de que se cambiara para saber quien gano 
if(player == 1):
	player = 2
else:
	player = 1

#Limpia la pantalla e imprime el tablero de juego final
system("cls")
printBoard(board)
print("Felicidades jugador ", player)