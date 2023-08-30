cesta_compra = input("Ingresa los productos de la canasta de compra drparados por comas: ")

productos = cesta_compra.split(",")

for producto in productos:
    print(producto.strip())