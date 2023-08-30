nombre = input("Introduce tu nombre?")
edad = input("Cual es tu edad")
direccion = input("Introduce tu direccion")
telefono = input("Cual es tu numero de telefono")
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su numero de telefono es', persona['telefono'])