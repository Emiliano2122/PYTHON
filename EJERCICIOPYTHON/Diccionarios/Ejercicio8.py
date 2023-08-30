diccionario = {}
palabras = input("Introdusca la lista de palabras y traducciones en formato palabra:traducir separado por comas: ")
for i in palabras.split(","):
    clave, valor = i.split("hola:hello")
    diccionario[clave] = valor
frase = input("Introdusca una frase en español: ")
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=" ")
    else:
        print(i, end=" ")