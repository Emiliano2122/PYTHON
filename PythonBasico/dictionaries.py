def separa():
    print()
    print("----------")
    print()

# dictionaries

print("d i c t i o n a r i e s")

separa()

myDictionary = {
    "laptop": "Dell",
    "Pluma": "Mont Blanc",
    "Celular": "Huawei",
    }

print(myDictionary)

separa()

# dictionary no permite datos duplicados, son remplazados

myStyle = {
    "Laptop": "Dell",
    "Pluma": "Mont Blanc",
    "Celular": "Huawei",
    "Celular": "Motorola",
    }

print(myStyle)

separa()

# para determinar la longitud de los elemntos del dictionary usamos el metodo len

print(len(myStyle))

separa()

# varios tipos de datos en dictionary

myCar = {
    "Marca": "Nisan",
    "Electrico": True,
    "Año": 2020,
    "Colores": ["rojo","gris","azul"]
    }

print(myCar)

separa()

# imprimir el tipo de dato

print(myCar)

print(type(myCar))

separa()

# accesar a los datos del dictionary

myCell = {
    "Marca": "iPhone",
    "Modelo": "6+",
    "Capacidad": "64 GB",
    "Color": "Dorado",
    "Funda": True,
    }

print(myCell["Color"])
print(myCell["Marca"])
HD = myCell["Capacidad"]
funda = myCell.get("Funda")# usamos el metodo get para accesar datos del dictionary

print(HD)
print(funda)

separa()

# imprimir las keys del dictionary

print(myCell.keys())

estructura = myCell.keys()
print(estructura)

separa()

# para agregar otra key
myCell["Camara"] = True

print(myCell)

separa()



    