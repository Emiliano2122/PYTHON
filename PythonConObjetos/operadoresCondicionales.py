def separa():
    print("")
    print("-----------")
    print("")

x1 = 0
x2 = 0

if x1 == 0:
    print("x1 es igual a cero")
    
separa()

if x2 == 0:
    print("x2 es igual a cero")
    
separa()

if x1 == 0 and x2 == 0:
    print("x1 y x2 son iguales a cero")

separa()

def porcentaje(x):
    print("{:,.2f}%".format(x))

def porcentajeX(x1, x2):
    tempo = (x2 * 100 / x1) - 100
    print("{:,.2f}%".format(tempo))

def porcentajeX2(x1, x2):
    print("{:,.2f}%".format((x2 * 100 / x1) - 100))

print(porcentaje(x1))

separa()

porcentaje(x1)

separa()

porcentajeX(245, 689)
porcentajeX2(567, 789)

separa()

