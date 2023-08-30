peso_payaso = 112
peso_muñecas = 75

num_payasos = int(input("Ingresa el numero de payasos vendidos: "))
num_muñecas = int(input("Ingresa el numero de muñecas vendidas: "))

peso_total = (peso_payaso * num_payasos) + (peso_muñecas * num_muñecas)

print("El peso total del paquete a enviar es:", peso_total, "gramos")