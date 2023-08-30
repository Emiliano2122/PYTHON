precio = float(input("Ingresa el precio de un producto en euros con dos decimales: "))

euros = int(precio)
centimos = int((precio - euros) * 100)

print("El precio es de", euros, "euros y", centimos, "centimos")