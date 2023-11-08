opciones = ["piedra", "papel", "tijera"]

print(opciones)

tiradas = []

print(tiradas)

tiradas.append("papel")

print(tiradas)

tiradas.append("piedra")

print(tiradas)

tiradas.append("tijera")

print(tiradas)

tiradas.append("tijera")

print(tiradas)

tiradas.append("papel")

print(tiradas)

tiradas.append("piedra")

print(tiradas)

tiradas.append("tijera")

print(tiradas)

print(tiradas[0])
print(tiradas[1])
print(tiradas[2])

totalTiradas = len(tiradas)

print(totalTiradas)

contador = 0

jugador1 = "Emiliano"
jugador2 = "Antonio"
# print("Tiradas\tEmiliano")
print("Tiradas" + "\t" + jugador1 + "\t" + jugador2)
print("===================================")

while contador <= (totalTiradas - 1):
    temporal = contador + 1
    print(str(temporal) + "\t" + tiradas[contador], "\t\t" + tiradas[contador])
    contador += 1


    
    