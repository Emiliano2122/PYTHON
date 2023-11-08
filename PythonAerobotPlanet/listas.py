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
