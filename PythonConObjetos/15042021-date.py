from datetime import date
from datetime import datetime

def separa():
    print("")
    print("-------------------")
    print("")

print("módulo de fecha")

separa()

#datetime
ahora = datetime.now()

print("Fecha y hora", ahora)

separa()
#date
fecha = date.today()
print("Dia actual: ", fecha)

separa()

dia = fecha.day
mes = fecha.month
anio = fecha.year

print("Hoy es: ", dia)
print("Del mes: ", mes)
print("Del año: ", anio)

separa()

print("El dia actual es {}".format(fecha.day))
print("El mes actual es {}".format(fecha.month))
print("El año actual es {}".format(fecha.year))

separa()

print("La hora actual es: {}".format(ahora.hour))
print("El minuto actual es: {}".format(ahora.minute))
print("El segundo actual es: {}".format(ahora.second))

separa()

#definimos un fecha en particular

nuevaFecha = datetime(2001, 9, 16, 9, 24, 56, 00000)

print("Mi fecha y hora de nacimiento: ", nuevaFecha)

separa()

miFechaNacimiento = date(2001, 9, 16)

print("Mi fecha de nacimiento: ", miFechaNacimiento)

separa()

print("El dia actual es: {}".format(fecha.day))
print("El mes actual es: {}".format(fecha.month))
print("El año actual es: {}".format(fecha.year))

separa()

print("La hora actual es: {}".format(ahora.hour))
print("El minuto actual es: {}".format(ahora.minute))
print("El segundo actual es: {}".format(ahora.second))

separa()

# operaciones con fechas
from datetime import timedelta

print("timedelta importado")

separa()

hoy = fecha.today()

print("Hoy es: ", hoy)

ayer = hoy - timedelta(days = 1)

print("Ayer fue: ", ayer)

manana = hoy + timedelta(days = 1)

print("Mañana sera: ", manana)

separa()

antier = hoy - timedelta(days = 2)

print("Antier fue: ", antier)

pasadoManana = hoy + timedelta(days = 2)

print("PasadoMañana sera: ", pasadoManana)

separa()

contador = 1
dia = fecha.today()

while contador <= 90:
    print(dia)
    dia = dia + timedelta(days = 1)
    contador +=1

separa()

# formato a las fechas
# Converting Datw to String with strftime

hoy = fecha.today()

print("Hoy es: ", hoy.strftime("%a"))
print("Hoy es: ", hoy.strftime("%A"))
print("Mes actual: ", hoy.strftime("%b"))
print("Mes actual: ", hoy.strftime("%B"))
print("Mes actual: ", hoy.strftime("%m"))
print("Dia de la semana: ", hoy.strftime("%w"))
separa()

# L   M   X   J   V   S    D
#             1   2   3    4
# 5   6   7   8   9   10   11
# 12  13  14  15  16  17   18
# 19  20  21  22  23  24   25
# 26  27  28  29  30

dia = date.today()

vendedores = ["Alfonso", "Cynthia", "Karla", "Salvador", "Liliana", "Genaro", "Oscar", "Héctor", "Carlos", "Demian"]
lenVendedores = len(vendedores)
contVendedores = 0

contador = 1
limite = 101
print("Total de vendedores: ", lenVendedores)

while contador <= limite:
    print(dia, "\t", vendedores[contVendedores], "\t", contador)
    contador += 1
    contVendedores += 1
    if contVendedores == lenVendedores :
        contVendedores = 0
        dia = dia + timedelta(days = 1)
        print("")

proyectos = ["Unico Coyoacan", "Park Andalucia", "Icon Roma", "Casa Roma 315", "Descanso 1", "Icon Condesa", "Park del Carmen", "Casa Roma 127", "Único Roma", "Descanso 2"]
lenProyectos = len(proyectos)
contProyectos = 0

contador = 1
limite = 30
print("Total de proyectos: ", lenProyectos)

while contador <= limite:
    print(dia, "\t", proyectos[contProyectos])
    contador += 1
    contProyectos += 1
    if contProyectos == lenProyectos:
        contProyectos = 0
        dia = dia + timedelta(days = 1)
        print("")

Direcciones = ["Popocatépetl 164", "Andalucia No.214", "Sinaloa No.10", "Bajio 315", "Chicontepec No.57", "Laguna del Carmen 38", "Tlacotlalpan No.127", "Coahuila No.28"]
lenDirecciones = len(Direcciones)
contDirecciones = 0

contador = 1
limite = 30
print("Total de Direcciones: ", Direcciones)

while contador <= limite:
    print(dia, "\t", Direcciones[contDirecciones])
    contador += 1
    contDirecciones += 1
    if contDirecciones == lenDirecciones:
        contDirecciones = 0
        dia = dia + timedelta(days = 1)
        print("")


DiaSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
lenDiaSemana = len(DiaSemana)
contDiaSemana = 0

contador = 1
limite = 30
print("Total de DiaSemana: ", DiaSemana)

while contador <= limite:
    print(dia, "\t", DiaSemana[contDiaSemana])
    contador += 1
    contDiaSemana += 1
    if contDiaSemana == lenDiaSemana:
        contDiaSemana = 0
        dia = dia + timedelta(days = 1)
        print("")



Numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
lenNumeros = len(Numeros)
contNumeros = 0

contador = 1
limite = 30
print("Total de Numeros: ", Numeros)

while contador <= limite:
    print(dia, "\t", Numeros[contNumeros])
    contador += 1
    contNumeros += 1
    if contNumeros == lenNumeros:
        contNumeros = 0
        dia = dia + timedelta(days = 1)
        print("")

            
        

separa()