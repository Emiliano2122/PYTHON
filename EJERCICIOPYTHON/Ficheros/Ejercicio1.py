n = int(input("Introdusca un numero entero entre 1 y 10: "))
nombre_fichero = "tabla-" + str(n) + ".txt"
f = open(nombre_fichero, "w")
for i in range(1, 11):
    f.write(str(n) + "x" + str(i) + " = " + str(n * i) + "\n")
f.close()