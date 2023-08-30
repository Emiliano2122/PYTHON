cesta = {}
continuar = True
while continuar:
    item = input("Introduce un articulo: ")
    precio = float(input("Introduce el precio de " + item + ":"))
    cesta[item] = precio
    continuar = input("Quieres añadir un articulo mas a tu lista (Si/No) ") == "Si"
coste = 0
print("Lista de compra")
for item, precio in cesta.items():
    print(item, "\t", precio)
    coste += precio
print("Costo total: ", coste)