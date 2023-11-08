notas = ['B','B','B','A','A','B','A','C','A+','D','B','B','B','A','F','B','A','C','A+','D','B','B','B','A','F','B','A','C','A+','D','A','A+','B','D','A','C','B','B','B','A','F','B','A','C','A+',
         'D', 'B', 'A', 'F', 'C', 'B', 'A', 'A', 'D', 'A', 'C', 'B', 'C', 'D', 'C', 'B', 'B', 'B', 'A', 'F', 'B', 'A', 'C', 'A+', 'D']

print("cuantas notas hay:",len(notas))
calificaciones = (notas.count("A+"))
print("numero de calificaciones iguales a A+:" ,calificaciones)
calificaciones_1 = (notas.count("F"))
print("numero de calificaciones iguales a F:" ,calificaciones_1)
calificaciones_2 = (notas.count("B"))
print("numero de calificaciones iguales a B:" ,calificaciones_2)
calificaciones_3 = (notas.count("C"))
print("numero de calificaciones iguales a C:" ,calificaciones_3)
calificaciones_4 = (notas.count("D"))
print("numero de calificaciones iguales a D:" ,calificaciones_4)
calificaciones_5 = (notas.count("A"))
print("numero de calificaciones iguales a A:" ,calificaciones_5)

"""
for letra in"Hola":
    print (letra)
for num in range (1,10):
    print(num)
"""
for i in range(1,31):
    notas.append('randrange(60,101,1')

#listas
"""
idiomas = ["español", "ingles", "frances", "aleman", "italiano", "chino"]
print ("idiomas: ", idiomas)
print ("primer elemento: ", idiomas [0])
print ("segundo elemento: ", idiomas [1])

"""
#lista con valores numericos
"""
edades = [12,15,16,14,15,11,13]
print("Edades: ", edades)
print("primer elemnto: ",edades[0])
print("segundo elemnto: ",edades[1])

"""
#modificar valores
"""
idiomas [4] = ("Chino")
print ("idiomas:" , idiomas)

"""
#longitud se la lista
reptiles =["wiliam","emiliao", "wendy"]
print ("reptles:" ,reptiles)

print("numero de reptiles:",len(reptiles))

reptiles.append("roberta")
print ("Reptiles", reptiles)

reptiles.insert(1, "roberto")
print("reptiles: ", reptiles)

reptiles.remove("roberto")
print ("Reptiles", reptiles)

reptil = input("ingrese el nombre del reptil que quieras buscar")
if (reptil in reptiles):
    print ("el reptil", reptil, "esta en tu grupo de reptiles")
    print("indice de reptiles:", reptil.index(reptil))

else:
    print("el reptil", reptil,"no esta el tu lista de reptiles")
    
