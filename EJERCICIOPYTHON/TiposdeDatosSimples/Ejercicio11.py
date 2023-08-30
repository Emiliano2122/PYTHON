cantidad_depositada = float(input("Ingresa la cantidad de dinero depositada en la cuenta de ahorros"))

interes_anual = 0.04 # Tasa de interes anual del 4%

ahorros_primer_anio = cantidad_depositada * (1 + interes_anual)
ahorros_segundo_anio = ahorros_primer_anio * (1 + interes_anual)
ahorros_tercer_anio = ahorros_segundo_anio * (1 + interes_anual)

ahorros_primer_anio = round(ahorros_primer_anio, 2)
ahorros_segundo_anio = round(ahorros_segundo_anio, 2)
ahorros_tercer_anio = round(ahorros_tercer_anio, 2)

print("Ahorros despues del primer año:", ahorros_primer_anio)
print("Ahorros despues del segundo año:", ahorros_segundo_anio)
print("Ahorros despues del tercer año:", ahorros_tercer_anio)