from datetime import date
from datetime import datetime
import os
import os.path as path

def separa():
    print("")
    print("--------------")
    print("")

print("módulo de fecha")

# print("La hora actual es {}".format(fecha.hour))

# es posible definir una fecha en particular
nuevaFecha = datetime(1960, 6, 9, 6, 23, 35, 00000)
 
print("Nueva fecha: ", nuevaFecha)

# operaciones con fechas
from datetime import timedelta

separa()

dia = date.today()

vendedores = ["Carlos", "Salvador", "Alfonso", "Cynthia", "Karla", "Genaro", "Oscar",  "Héctor", "Demian", "Liliana"]
complejos = ["Unico Coyoacan", "Park Andalucia", "Icon Roma", "Casa Roma 315", "Icon Condesa", "Park Del Carmen", "Casa Roma 127", "Unico Roma"]

mon = ["Cynthia", "Héctor"]
tue = ["Alfonso", "Oscar"]
wed = ["Salvador", "Genardo"]
thu = ["Carlos", "Karla"]
fri = ["Liliana", "Demian"]
sat = ["Héctor", "Cynthia"]
sun = ["Oscar", "Alfonso"]

numVendedores = len(vendedores)
numComplejos = len(complejos)

limite = 100
inicia = 1

contaVendedores = 0
contaComplejos = 0

print("Mis vendedores son: ", numVendedores)
print("Mis complejos son: ", numComplejos)

print("Fecha", "\t", "Día", "\t", "Vendedor" , "\t", "Complejo")

file = open("rolDeGuardias.txt", "w")

while inicia <= limite:
    
    file.write(str(dia))
    file.write("\t")
    file.write(dia.strftime("%a"))
    file.write("\t")
    file.write(vendedores[contaVendedores])
    file.write("\t")
    file.write(complejos[contaComplejos])
    file.write("\n")
    
    contaVendedores = contaVendedores + 1
    if contaVendedores == numVendedores:
        contaVendedores = 0
        
    contaComplejos = contaComplejos + 1
    if contaComplejos == numComplejos:
        contaComplejos = 0
        dia = dia + timedelta(days = 1)
        
    inicia = inicia + 1

file.close()


separa()

#  (comma-separeted values)
#Fecha,Dia,Vendedor,Complejo
#2021-04-21."Wed","Carlos","Unico Coyoacan"
#2021-04-21,"Wed","Salvador","Park Andalucia"
#2021-04-21,"Wed","Alfonso","Icon Roma"

separa()

dia = date.today()

vendedores = ["Carlos", "Salvador", "Alfonso", "Cynthia", "Karla", "Genaro", "Oscar",  "Héctor", "Demian", "Liliana"]
complejos = ["Unico Coyoacan", "Park Andalucia", "Icon Roma", "Casa Roma 315", "Icon Condesa", "Park Del Carmen", "Casa Roma 127", "Unico Roma"]

mon = ["Cynthia", "Héctor"]
tue = ["Alfonso", "Oscar"]
wed = ["Salvador", "Genardo"]
thu = ["Carlos", "Karla"]
fri = ["Liliana", "Demian"]
sat = ["Héctor", "Cynthia"]
sun = ["Oscar", "Alfonso"]

numVendedores = len(vendedores)
numComplejos = len(complejos)

limite = 100
inicia = 1

contaVendedores = 0
contaComplejos = 0

print("Mis vendedores son: ", numVendedores)
print("Mis complejos son: ", numComplejos)

# archivo .csv separado por comas

file = open("rolDeGuardias.csv", "w")
#2021-04-21."Wed","Carlos","Unico Coyoacan"

file.write("Fecha,Día,Vendedor,Complejo")
file.write("\n")

while inicia <= limite:
    
    tempo = str(dia)
    tempo1 = dia.strftime("%a")
    tempo2 = vendedores[contaVendedores]
    tempo3 = complejos[contaComplejos]
     
    linea = tempo + ",\"" + tempo1 + "\",\"" + tempo2 + "\",\"" + tempo3 + "\""
    file.write(linea)
    file.write("\n")
    
    
    contaVendedores = contaVendedores + 1
    if contaVendedores == numVendedores:
        contaVendedores = 0
        
    contaComplejos = contaComplejos + 1
    if contaComplejos == numComplejos:
        contaComplejos = 0
        dia = dia + timedelta(days = 1)
        
    inicia = inicia + 1

file.close()


separa()