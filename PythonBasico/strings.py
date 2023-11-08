def separa():
    print()
    print("----------")
    print()
    
mensaje = "¡Hola Mundo"

print(mensaje)

separa()

frase = "Las mejores cosas en la vida son gratis"

print("gratis" in frase)

separa()

print("free" in frase)

separa()

if "gratis" in frase:
    print("Si existe la palabra en la frase")

if "free" not in frase:
    print("No existe la palabre en la frase")
    
separa()

frase = "Las mejores cosas en la vida son GRATIS"

print(frase.upper())

separa()

print(frase.lower())

separa()

# format para concatenar texto con numeros

tipoDeCambio = 21.33
leyenda = "El tipo de cambio del USD es de {}"

print(leyenda.format(tipoDeCambio))

separa()

cantidad = 8
idProducto = 876
precio = 123.456

orden = "Mi orden es de {} pzas. del producto {} con precio unitario de {}"
print(orden.format(cantidad, idProducto, precio))

separa()

miPago = "Voy a pagar {2} por {0} pza. del producto {1}"
print(miPago.format(cantidad, idProducto, precio))

separa()