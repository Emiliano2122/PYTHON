def separa():
    print()
    print("----------")
    print()

mySet = {"lunes", "martes", "miercoles"}
print(mySet)

separa()

misColores = {"rojo", "azul", "verde", "azul"}
print(misColores)

separa()

print("Lan longuitud de set")
print(misColores)
print(len(misColores))

separa()

print(type(misColores))

separa()

# define explicitamente un set
dias = set(("Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"))
print(dias)
print(type(dias))

separa()

diasAbr = {"L", "M", "M", "J", "V", "S", "D"}
for x in diasAbr:
    print(x)

separa()

 # TAREA

#misFrutas          texto      
#misCalificaciones  numeros
#misEstatus         boolean
#misDatos           combinado

misFrutas = {"melon", "papaya", "fresa", "piña"}
print(misFrutas)

separa()

misCalificaciones = {9, 6, 8, 7,}
print(misCalificaciones)

separa()

misEstatus = {False, True, True}
print(misEstatus)

separa()

misDatos = {"Sara", 24, True, 65.500}
print(misDatos)

separa()

# defino un set explicitamente

figurasGeometricas = set(("perimetro", "área", "volumen"))
print(type(figurasGeometricas))
print(figurasGeometricas)

separa()

# agrego un item o valor a un set
semaforo = {"verde", "rojo"}

print(semaforo)

semaforo.add("amarillo")

print(semaforo)

separa()

# para agregar items de un set a otro set, usamos el metodo update()

nones = {1, 3, 5, 7, 9}
pares = {2, 4, 6, 8}

nones.update(pares)

print(nones)

separa()

# se pueden mezclar diferentes tipos de arrays

# list
citricos = ["naranja", "limon", "toronja"]
    
# set
frutas = {"kiwi", "fresa", "melon"}

frutas.update(citricos)

print(frutas)

separa()

# borrar un item o elemnto de set usando el metodo remove()

frutas.remove("limon")
print(frutas)

separa()

# error si trato de borrar un item o elemento que no existe el metodo remove

#frutas.remove("limon")

separa()

# borrar un item o elemnto usando discard()

frutas.discard("kiwi")

print(frutas)

separa()

# No hay error si trato de borrar un item o elemnto usando el metodo discard()

frutas.discard("kiwi")
print(frutas)

separa()

# puedo eliminar el ultimo item o elemnto usando el metodo pop()

print(frutas)
elemntoBorrado = frutas.pop()
print(frutas)
print(elemntoBorrado)

separa()

# para vaciar un set usamos el metodo clear()

print(frutas)
frutas.clear()
print(frutas)

separa()

# para borrar un set completamente usamos del
carabelas = {"Niña", "Pinta", "Santa Maria"}

print(carabelas)

# del carabelas

print(carabelas)

separa()

# para recorrer un set usamos el ciclo: for

print(misDatos)

for x in  misDatos:
    print(x)

separa()

# para unir dos set en un nuevo set

nones = {1, 3, 5, 7, 9}
paras = {2, 4, 6, 8}
print(nones)
print(pares)

numeros = nones.union(pares)

print(numeros)

separa()

vocales = {"a", "e", "i", "o", "u"}
abecedario = {"a", "b", "c", "d", "d", "e", "f", "g", "h", "i", "j", "k"}

vocales.intersection_update(abecedario)

print(vocales)

separa()

# para crear un nuevo set usando intersection para mostrar los repetidos

vocales = {"a", "e", "i", "o", "u"}
abecedario = {"a", "b", "c", "d", "d", "e", "f", "g", "h", "i", "j", "k"}

resultado = vocales.intersection(abecedario)

print(vocales)
print(abecedario)
print(resultado)

separa()

# para mostrar la diferencia de dos sets, o sea los NO duplicados

vocales = {"a", "e", "i", "o", "u"}
abecedario = {"a", "b", "c", "d", "d", "e", "f", "g", "h", "i", "j", "k"}

print(vocales)
print(abecedario)
vocales.symmetric_difference_update(abecedario)

print(vocales)

separa()

vocales = {"a", "e", "i", "o", "u"}
abecedario = {"a", "b", "c", "d", "d", "e", "f", "g", "h", "i", "j", "k"}
unicas = vocales.symmetric_difference(abecedario)

print(vocales)
print(abecedario)
print(unicas)

separa()