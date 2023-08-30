n = int(input("Introduce un numero entero del 1 y 10: "))
m = int(input("Introduce otro numero entro del 1 y 10: "))
nombre_fichero = "tabla-" + str(n) + ".txt"
try:
    with open(nombre_fichero, "r") as f:
        lineas = f.readline()
    print(lineas[m - 1])
except FileNotFoundError:
    print("No existe el fichero con la tabla del ", n)