#------------------Actividad 5-----------------------------------------
"""Problema de programación: Escribir un programa que genere una lista de 20 números aleatorios entre 1 y 100.
Escribir dos funciones "minimo" y "maximo" que reciban una lista como parámetro y regresen el número mínimo y máximo respectivamente de la lista."""
from random import *

notas = [ ]

for i in range(1,21):
    notas.append(randrange(1,100))
     
