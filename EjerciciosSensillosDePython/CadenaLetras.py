# Leer una cadena de caracteres y ordernarlas poniendolas en una lista en el orden que aparecen
# Ejemplo: Anita lava la tina
# Resultado:
#1. Anita
#2. lava
#...
#4. tina
# Al final lo guardamos en un archivo

# Leer la cadena de caracteres
cadena = input("Escribe una cadena: ")

# Dividir la cadena en palabras
palabras = cadena.split()

# Crear una lista ordenadas
lista_ordenadas = sorted(set(palabras), key=palabras.index)

# Mostrar en consola 
for i, palabras in enumerate(lista_ordenadas, 1):
    print(f'{i}. {palabras}')

# Guardar en un archivo de texto
with open("palabras_ordenas.txt", "w") as colum:
    for i, palabras in enumerate(lista_ordenadas, 1):
        colum.write(f'{i}. {palabras}\n')