# Crear un fichero en donde guardemos los numeros del 1 al 10
with open("numeros.txt", "w") as colum:
    for i in range(1, 11):
        colum.write(str(i) + " ")