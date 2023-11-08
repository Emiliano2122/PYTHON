import time
import socket
import platform
import os
import os.path
import sys

print("Inventario_Partes de una computadora")

#datos de Hardware
print("Hardware     :", platform.hardware())
print("Cantidad De Partes De Una Laptop      :", platform.CantidadDePartesDeUnaLaptop())
print("Numero Del Paquete     :", platform.NumeroDelPaquete())
print("Fecha del Pedido       :", platform.FechadelPedido())

# creamos el fichero excel
wb = xlwt.Workbook()
# añadimos hoja
ws = wb.add_sheet('Mi Inventario')
# escribimos encabesados
ws.write(0,0,'Hardware')
ws.write(0,1,'Cantidad De Partes De Una Laptop')
ws.write(0,2,'Numero Del Paquete')
ws.write(0,3,'Fecha del Pedido')
# escribo columnas excel
col = 1
ws.write(col,0,platform.hardware())
ws.write(col,1,platform.CantidadDePartesDeUnaLapto())
ws.write(col,2,platform.NumeroDelPaquete())
ws.write(col,3,platform.FechadelPedido())
# grabo Fichero excel.