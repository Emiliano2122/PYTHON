def separa():
    print("")
    print("--------------")
    print("")

# Emiliano Stasi Fernandez
# 012345678901234567890123

# para buscar un caracter en una cadena se ustiliza
# .find()
# find is sensitive case
# f <> F
# regresa -1 cuando no se encuentra
nombreCompleto = "Emiliano Stasi Fernandez"
caracter = "e"

posicion = nombreCompleto.find(caracter)


if posicion < 0:
    print("No se encuentra ", caracter, "en: ", nombreCompleto, "\"")
else:
    print(posicion)

    print("La primera incidencia del caracter buscado está en: ", posicion)

    posicion = posicion + 1

    psicion = nombreCompleto.find(caracter, posicion)

    print(posicion)

    print("La segunda incidencia del caracter buscado está en: ", posicion)

    #string.find(value, start, end)

    print("La primera incidencia del caracter ", caracter, "buscado en ", nombreCompleto, "esta en: ", posicion)

separa()

nombreCompleto = "Emiliano Stasi Fernandez"
caracter = "F"

posicion = nombreCompleto.index(caracter)

print(posicion)

separa()

longitud = len(nombreCompleto)

print(longitud)

# cuenta la cantidad de veces que aparece en una cadena un texto
cuenta = nombreCompleto.count("t")

print(cuenta)

separa()

# eliminar espacios en blanco al inicio y al final de la cadena
# terapeuta
# 012345678

puesto = "             terapeuta   "

print(puesto)
print(len(puesto))

nuevoPuesto = puesto.strip()
print(len(nuevoPuesto))
print(nuevoPuesto)

nombre = "                  Emiliano Stasi Fernandez           "
print(nombre)
print(len(nombre))

nuevoNombre = nombre.strip()
print(len(nuevoNombre))
print(nuevoNombre)

noPedido = "    -#-#-#-,012#345-#-,,,   "

print(noPedido)
numeroPedido = noPedido.strip("-,#")
print(numeroPedido)

separa()

departamento = "Facturscion"
print(departamento)

departamentoCorregido = departamento.replace("s", "a")
print(departamentoCorregido)

separa()

numeroPedido = numeroPedido.replace("#", "")

print(numeroPedido)

separa()

saludo = "¡Hola Mundo!"

print(saludo)

nuevoSaludo = saludo.replace("Mundo", "Emiliano")

print(nuevoSaludo)

nombre = "Emiliano Stasi Fernandez"

# replace lo ejecuta para todas las incidencias en forma predeterminada
print(nombre)
nombre2 = nombre.replace("e", "hbf")
print(nombre2)

# replace lo ejecuta para las incidencias que determine
nombre3 = nombre.replace("E", "gdfrt", 2)
print(nombre3)

separa()

nombrecompleto = "Emiliano Stasi Fewrnandez"
pedazos = nombreCompleto.split()

print(pedazos)

fecha = "2021-04-26"
pedazosFecha = fecha.split("-")

# el primer elemento es el elemento 0
print(pedazosFecha)

print(pedazosFecha[2], pedazosFecha[1], pedazosFecha[0])

fechaNueva = pedazosFecha[2] + "/" +pedazosFecha[1] + "/" + pedazosFecha[0]

print(fechaNueva)

separa()

frutas = "toronja - mamey - naranja - platano - piña - sandia"
piezasFrutas = frutas.split("-")

print(frutas)
print(piezasFrutas)

timestamp = "2017-07-08 08:53:51"

timestampPedazos = timestamp.split()

print(timestampPedazos)

print("Parte fecha:", fecha)

hora = timestampPedazos[1]

print("Parte hora", hora)

fecha = timestampPedazos[0]

fechaPedazos = fecha.split("-")

print(fechaPedazos)

diaFecha = fechaPedazos[2]
mesFecha = fechaPedazos[1]
anioFecha = fechaPedazos[0]

fechaOk = diaFecha + "/" + mesFecha + "/" + anioFecha

print("Fecha ok", fechaOk)

separa()


