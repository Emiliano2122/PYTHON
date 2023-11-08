import os
import os.path as path
from datetime import date
from datetime import datetime
from datetime import timedelta

def separa():
    print("")
    print("--------")
    print("")


# escribir un archivo en mi equipo (lap, pc, mac, cel, etc.)

# w write
# a append
# r read

file = open("archivoParaEmiliano.txt", "w")
file.write("emiliano")
file.write("stasi")
file.write("fernandez")
file.close()

file2 = open("archivoParaEmiliano2.txt", "w")
file2.write("emiliano" + os.linesep)
file2.write("stasi" + os.linesep)
file2.write("fernandez")
file2.close()

file3 = open("archivoParaEmiliano3.txt", "w")
file3.write("emiliano")
file3.write("\n") # secuencia de escape
file3.write("stasi")
file3.write("\n")
file3.write("fernandez")
file3.close()

file4 = open("archivoParaEmiliano4.txt", "w")
file4.write("emiliano")
file4.write("\t")
file4.write("stasi")
file4.write("\t")
file4.write("fernandez")
file4.close()

file4 = open("archivoParaEmiliano4.txt", "a")
file4.write("\n")
file4.write("Hello!")
file4.write("\n")
file4.write("bey!")
file4.close()

# checar la existencia de un archivo en la ubicacion definida

if path.exists("archivoParaEmiliano4.txt"):
    file5 = open("archivoParaEmiliano4.txt", "a")
    file5.write("\n")
    file5.write("Que bueno que ya existe el archivo")
    file5.close()

if path.isfile("archivoParaEmiliano4.txt"):
    print("Ya existe el archivo, esta es otra forma de verificar la existencia de un archivo")

if path.exists("saludos.txt"):
    file = open("saludos.txt", "a")
else:
    file = open("saludos.txt", "w")
file.write("Buenos dias")
file.write("\n")
file.close()

separa()

# if path.exists("guardias.txt"):
#    file = open("guardias.txt", "a")
# else:
file = open("guardias.txt", "w")

dia = date.today()

vendedores = ["Genaro", "Oscar", "Hector", "Liliana", "Salvador", "Alfonso", "Cynthia", "Demian"]
proyectos = ["Unico Coyoacan", "Park Andalucia", "Icon Roma", "Casa Roma 315", "Icon Condesa", "Park del Carmen", "Casa Roma 127", "Unico Roma"]

contadorVendedores = 0
contadorProyectos = 0

numVendedores = len(vendedores)
numProyectos = len(proyectos)

print("Total de vendedores: ", numVendedores)
print("Total de proyectos: ", numProyectos)

contador = 1
limite = 30

while contador <= limite:
    file.write(dia.strftime("%a"))
    file.write("\t")
    file.write(vendedores[contadorVendedores])
    file.write("\t")
    file.write(proyectos[contadorProyectos])
    file.write("\n")
    
    dia = dia + timedelta(days = 1)
    contadorVendedores = contadorVendedores + 1
    if contadorVendedores == numVendedores:
        contadorVendedores = 0
    
    contadorProyectos = contadorProyectos + 1
    if contadorProyectos == numProyectos:
        contadorProyectos = 0
    
    contador = contador + 1

file.close()
