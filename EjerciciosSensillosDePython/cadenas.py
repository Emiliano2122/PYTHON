#En un archivo guardar el resultado de leer una cadena de caracteres
#Y contar las vocales e indicar si tenemos la letra e en la ultima palabra

cadena = input("introduce tu texto: ")
#for i in cadena:
#print(cadena[1])
#print(cadena)
contador_de_vocales = 0
palabras = cadena.split()
#print(palabras[0])
for palabra in palabras:
    for letra in palabra:
        if letra == "e" or letra == "E":
            contador_de_vocales = contador_de_vocales + 1
        if letra == "a" or letra == "A":
            contador_de_vocales = contador_de_vocales + 1
        if letra == "i" or letra == "I":
            contador_de_vocales = contador_de_vocales + 1
        if letra == "o" or letra == "O":
            contador_de_vocales = contador_de_vocales + 1
        if letra == "u" or letra == "U":
            contador_de_vocales = contador_de_vocales + 1
print("El numero de vocales es:")
print("Contar todas las vocales en mayusculas:")
print(contador_de_vocales)
#print(palabras[len(palabras)-1])
for letra in palabras[len(palabras)-1]:
    if letra == "e" or letra == "E":
        print("si hay una e minuscula y una E mayuscula en la ultimapalabra")
        break