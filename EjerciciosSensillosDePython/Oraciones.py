# Verificar si una oracion esta dentro de oración
# Ejemplo: La vida es bella si trabajas mucho
# bella existe dentro de la oracion grande?

oracion_grande = input("Escribe una oracion grande:")
oracion_pequeña = input("Existe la oracion pequeña en la grande:")

esta_dentro = oracion_pequeña.lower() in oracion_grande.lower()

#print(str(esta_dentro))
if esta_dentro:
    print("Verdadero")
else:
    print("Falso")
