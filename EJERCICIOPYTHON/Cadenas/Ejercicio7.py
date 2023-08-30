correo = input("Ingresa un correo electronico: ")

nombre = correo.split("@")[0]
correo_modificado = nombre + "@gmail.com"

print("Correo electronico modificado:", correo_modificado)