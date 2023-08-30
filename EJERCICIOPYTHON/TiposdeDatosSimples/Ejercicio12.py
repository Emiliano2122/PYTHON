precio_por_barra = 3.49 #Precio de barra de pam habitual en euros
descuento = 0.6 # Descuento del 60% para el pan que no es del dia

num_barras_no_frescas = int(input("Ingresa el numero de barras de pan vendidas que no son son del dia: "))

precio_habitual = precio_por_barra
descuento_aplicado = precio_por_barra * descuento
coste_final = precio_por_barra * (1 - descuento) * num_barras_no_frescas

print("Precio habitual por barra de pan: {:.2f}€".format(precio_habitual))
print("Descuento por no ser fresca: {:.2f}€".format(descuento_aplicado))
print("Coste final total: {:.2f}€".format(coste_final))