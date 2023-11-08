#------------------Actividad 4-----------------------------------------
"""Programa de administración financiera: Una tienda almacena todos los precios de sus productos en una lista llamada precios.
Debido a efectos inflacionarios el dueño ha decidido incrementar sus precios un 4%.
Escribe un programa que genere una lista con los nuevos precios y que imprima los precios anteriores y los nuevos en el siguiente formato:
$10.00 -> $10.40
"""
precios = [990, 1305, 615, 895, 1100, 695, 505, 965, 200, 545, 235, 1405, 1320, 965, 880, 1240, 1210, 1395, 660, 610, 515, 210, 525, 600, 110, 275, 1375, 1415, 55, 75, 910, 165, 1085, 1415, 520, 110, 1405, 450, 740, 275, 1115, 655, 615, 990, 1185, 900, 390, 1260, 155, 1060, 450, 875, 355, 435, 410, 305, 560, 1495, 355, 1255, 305, 535, 155, 1170, 225, 585, 1175, 590, 1435, 1050, 1440, 160, 915, 1090, 1150, 955, 730, 445, 450, 735, 1360, 485, 965, 760, 1240, 1210, 600, 370, 710, 950, 665, 1195, 600, 240, 415, 990, 1355, 430, 65, 1495]
nuevosprecios = [ ]
for item in precios:
   nuevosprecios.append(item*1.04)
   print(f"$ {item:2f} -> $ {item*1.04: 2f}")
