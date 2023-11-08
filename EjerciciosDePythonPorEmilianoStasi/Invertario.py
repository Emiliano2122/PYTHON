from datetime import date
from datetime import datetime

from datetime import timedelta

dia = date.today()

HardwareYSoftware = ["Pantalla", "Teclado", "Mousepad o Trackpad", "Adaptador de corriente", "Puertos E/S", "Altavoces", "Webcam", "CPU", "Tarjeta Madre", "Memoria RAM", "Unidad óptica (CD/DVD/Blu-Ray)",  "Disco Duro o SSD", "Batería", "Antena BT/WiFi", "Ventiladores", "Tarjeta de Video"]
lenHardwareYSoftware = len(HardwareYSoftware)
contHardwareYSoftware = 0

contador = 1
limite = 101
print("Hardware y Software: ", lenHardwareYSoftware)

while contador <= limite:
    print(dia, "\t", HardwareYSoftware[contHardwareYSoftware], "\t", contador)
    contador += 1
    contHardwareYSoftware += 1
    if contHardwareYSoftware == lenHardwareYSoftware :
        contHardwareYSoftware = 0
        dia = dia + timedelta(days = 1)
        print("")

CantidadDePartesDeUnaLaptop = ["Pantalla 300", "Teclado 200", "Mousepad o Trackpad 400", "Adaptador de corriente 500", "Puertos E/S 100", "Altavoces 200", "Webcam 700", "CPU 800", "Tarjeta Madre 600", "Memoria RAM 400", "Unidad óptica (CD/DVD/Blu-Ray) 300", "Disco Duro o SSD 700", "Batería 500", "Antena BT/WiFi 200", "Ventiladores 800", "Tarjeta de Video 400"]
lenCantidadDePartesDeUnaLaptop = len(CantidadDePartesDeUnaLaptop)
contCantidadDePartesDeUnaLaptop = 0

contador = 1
limite = 100
print("Cantidad de Partes de una Laptop: ", CantidadDePartesDeUnaLaptop)

while contador <= limite:
    print(dia, "\t", CantidadDePartesDeUnaLaptop[contCantidadDePartesDeUnaLaptop])
    contador += 1
    contCantidadDePartesDeUnaLaptop += 1
    if contCantidadDePartesDeUnaLaptop == lenCantidadDePartesDeUnaLaptop:
        contCantidadDePartesDeUnaLaptop = 0
        dia = dia + timedelta(days = 1)
        print("")


NumeroDelPaquete = ["Pantalla 12678", "Teclado 12789", "Mousepad o Trackpad 12890", "Adaptador de corriente 12467", "Puertos E/S 12444", "Altavoces 13567", "Webcam 13890", "CPU 14678", "Tarjeta Madre 15890", "Memoria RAM 17654", "Unidad óptica (CD/DVD/Blu-Ray)18234", "Disco Duro o SSD 18555", "Batería 19256", "Antena BT/WiFi 19780", "Ventiladores 20934", "Tarjeta de Video 20457"]
lenNumeroDelPaquete = len(NumeroDelPaquete)
contNumeroDelPaquete = 0

contador = 1
limite = 30
print("Numero del Paquete: ", NumeroDelPaquete)

while contador <= limite:
    print(dia, "\t", NumeroDelPaquete[contNumeroDelPaquete])
    contador += 1
    contNumeroDelPaquete += 1
    if contNumeroDelPaquete == lenNumeroDelPaquete:
        contNumeroDelPaquete = 0
        dia = dia + timedelta(days = 1)
        print("")