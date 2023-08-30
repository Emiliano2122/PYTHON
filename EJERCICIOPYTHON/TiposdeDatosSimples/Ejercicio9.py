cantidad_invertir = float(input("Ingresa la cantidad a invertir: "))
interes_anual = float(input("Ingresa el interés anual (%): "))
numero_anios = int(input("  Ingresa el número de años: "))

capital_obtenido = cantidad_invertir * (1 + (interes_anual / 100)) ** numero_anios

print("El capital obtenido en la inversion es:", capital_obtenido)