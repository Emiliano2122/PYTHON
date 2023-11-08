def separa():
    print("")
    print("------------")
    print("")

nombreCompleto = "emiliano stasi fernandez"

print(nombreCompleto.capitalize())

separa()

print(nombreCompleto.upper())

separa()

saludos = "MUY BUENOS DÍAS"

print(saludos.lower())

separa()

# 2021-04-23
# 01234567890

fechaActual = "2021-04-23"

print(fechaActual[0:4])
anio = fechaActual[0:4]
mes = fechaActual[5:7]
dia = fechaActual[8:10]

nuevaFecha = dia + "-" + mes + "-" + anio

print(nuevaFecha)

separa()

def fechaParaPC(fecha):
# 2021-04-23  -> 23-04-2021

    anio = fecha[0:4]
    mes = fecha[5:7]
    dia = fecha[8:10]
    
    nueva = dia + "-" + mes + "-" + anio
    return(nueva)

hoy = fechaParaPC("2021-04-23")

print(hoy)

separa()