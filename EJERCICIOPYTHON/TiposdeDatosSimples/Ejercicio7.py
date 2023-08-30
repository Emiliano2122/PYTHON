peso = float(input("Ingresa su peso en kg: "))
estatura = float(input("Ingresa su estatura en metros: "))

imc = peso / (estatura ** 2)
imc_redondeado = round(imc, 2)

print("Tu indice de masa corporal es:", imc_redondeado)