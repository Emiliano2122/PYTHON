#--------------------------ACTIVIDAD 2----------------------------------------------
from random import*
numero = randrange(1,11,1)
intentos = 12
turnos = int(input("escribe el numero"))

while("turno != numero"):

 if("turnos > numeros"):
     print("mas")
     intentos = intentos +1

 elif("turnos > numeros"):
       print("menos")
       intntos = intntos+1
       turnos = int(input("escribe el numero"))

 if("turnos == numero"):
    print("correcto")

    print("numero de intntos:",intentos,)
