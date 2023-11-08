#TERCER PROGRAMA
gasto = int(input("Ingresa el consumo total: "))
propina = int(input("Ingresa el porcentaje de propina: "))
total = gasto + (propina*gasto)/100
print("El total a pagar es: " ,total)
