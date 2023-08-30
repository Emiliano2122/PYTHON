facturas = {}
cobrado = 0
pendiente = 0
more = ""
while more != "T":
    if more == "A":
        clve = input("Introdusca el numero de la factura: ")
        coste = float(input("Introdusca el costo de la factura: "))
        facturas[clve] = coste
        pendiente += coste
    if more == "P":
        clave = input("Introdusca el numero de la factura a pagar: ")
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste
    print("Recaudado:", cobrado)
    print("Pendiente por cobrar: ", pendiente)
    more = input("Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)")