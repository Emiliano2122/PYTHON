#Merge Sort Algoritmo

from random import *

#MergeSort
def mergeSort(miLista):
    #Funcion que divide la lista en mitades recursivamente y las regeresa ambas partes unidas
    
    if(len(miLista) == 1):
    	return miLista
    
    #Calcula la mitad de la lista
    mid = len(miLista)//2
    
    #Creamos las dos listas que almacenan las mitades	
    lista1 = miLista[:mid]
    lista2 = miLista[mid:]
    
    #Llamamos recursivamente a MergeSort para subdivir nuestra lista
    lista1 = mergeSort(lista1)
    lista2 = mergeSort(lista2)
    
    #Usamos merge para ordenar
    return merge(lista1, lista2)


#Merge
def merge(A, B):
    #Funcion que recive lasmitades de la lista y las une en orden recursivamente
    C = []
    i = 0
    j = 0
    #Recorrer las listas
    while(i < len(A) and j < len(B)):
        if(A[i] < B[j]):
           C.append(A[i])
           i += 1
        else:
            C.append(B[j])
            j += 1

    while(i < len(A)):
        C.append(A[i])
        i += 1
    
    while(j < len(B)):
        C.append(B[j])
        j += 1

    return C

#----------------------------------------------------------
miLista = []
#Empieza del 1 hasta 101, para 1
#Llamar la lista con numeros 
for i in range(1,11): 
    miLista.append(randrange(1, 101, 1))

print("Lista original: ", miLista)

#Usamos mergeSort para ordenar la lista
miLista = mergeSort(miLista) 

#Imprimir la lista ordenada
print("Lista Ordenada. ", miLista)                          