#------------------Programa 6.1-----------------------------------------
#Programa para conocer la estrucutra de datos diccionario y sus funciones mивs comunes.

car = {
    "brand": "Audi",
    "model": "A4",
    "year": 2006}

print("Brand:", car["brand"])
print("Model:", car["model"], "\n")

#Recorrer diccionarios
for key in car:
    print(key,":", car[key])

#Verificar si existe una llave
if "year" in car:
    print("Year data exists.\n")
else:
    print("Year data not available.\n")

#Verificar si existe un valor
if "A5" in car.values():
    print("Model exists.\n")
else:
    print("Model not available.\n")

#Contar elementos totales
print("Number of data from the car:", len(car), "\n")

#Agregar elementos
car["color"] = "Silver"
print(car, "\n")

#Eliminar elementos
car.pop("year")
print("After deleting year:", car, "\n")

#Modificar elementos
car["color"] = "Red"
print("Color:", car["color"], "\n")
