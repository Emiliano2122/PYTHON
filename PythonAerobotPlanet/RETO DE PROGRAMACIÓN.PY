#hay N monedas, cada una con cara o cruz. Nos gustaría que todas las monedas fueran iguales. ¿Cuál es el número mínimo de monedas que deben invertirse?

#Dada una matriz A de N enteros que representan las monedas, devuelve el número mínimo de monedas que deben invertirse. Los elementos consecutivos de 
#la matriz A representan monedas consecutivas y contienen solo un 0 (caras) o un 1 (colas). Por ejemplo, dada la matriz A = [1,0,0,1,0,0], hay 4 monedas 
#que muestran caras y 2 monedas que muestran colas. La función debe devolver 2, ya que después de invertir 2 monedas (en las posiciones 0 y 3), todas las 
#monedas mostrarán la misma cara (caras).

#Asumir que:
#N is an integer within range [1,100]
#each elements of A is an integer that can have one of the
#following valuesl: 0, 1:

M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(M[-1][0])
print(M[-1][-1])
print("-")
for i in range(0, 3):
	print(M[i])
print("-")
for i in range(0, 3):
    for j in range(0, 3):
         print(M[i][j])
M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
s = 0.0
for i in range(0, 3):
    for j in range(0, 3):
         s += M[i][j]
print(s / 9)         	
