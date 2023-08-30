nombre_completo = input("Ingresa tu nombre completo: ")

nombre_minusculas = nombre_completo.lower()
nombre_mayusculas = nombre_completo.upper()

nombre_dividido = nombre_completo.split()
nombre_capitalizado = " ".join([nombre.capitalize() for nombre in nombre_dividido])

print("Nombre completo en minusculas:", nombre_minusculas)
print("Nombre completo en mayusculas:", nombre_mayusculas)
print("Nombre completo capitalizado:", nombre_capitalizado)