nombre_producto = input("Ingresa el nombre del producto: ")
precio_unitario = float(input("Ingresa el precio unitario del producto: "))
unidades = int(input("Ingrese el número de unidades: "))

costo_total = precio_unitario * unidades

cadena_resultado = f"Producto: {nombre_producto}\nPrecio unitario: {precio_unitario:6.2f}\nUnidades: {unidades:3d}\nCosto total: {costo_total:8.2f}"

print(cadena_resultado)