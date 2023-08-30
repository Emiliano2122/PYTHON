telefono = input("Ingresa tu numero de telefono con el formato +52-XXXXXXXX-XX:")

# Eliminar el prefijo y la extencion
numero = telefono.split("-")[1]

print("Numero de telefono sin prefijo y extencion:", numero)