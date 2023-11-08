#----------------------PROGRAMA 5.3-------------------------------------

#PROGRAMA QUE OBTIENE EL PROMEDIO DE UNA LISTA DE NUMEROS
from random import *

def promedio(notas):
    suma = 0
    for nota in notas:
        suma = suma + nota

    promedio = suma/len(notas)
    return promedio

#----------------------------------------------------------------------
notas = [ ]

for i in range(1,31):
    notas.append(randrange(60,101,1))

print("La nota media del grupo es: ", promedio(notas))    
    

