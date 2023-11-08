from random import *

def bubbleSort(miLista):
    for long in range (len(miLista)-1,0,-1):
        for i in range (0, long):
            if miLista[i]>miLista[i + 1]:
               temp = miLista[1]
               miLista[i] = miLista[i+1]
               miLista[i+1] = temp
        print(miLista)

miLista = []

for i in range (1,11):
    miLista.append(randrange(1,101,1))

print("lista original ", miLista)
bubbleSort(miLista)
print("lista original  ",miLista)                        
