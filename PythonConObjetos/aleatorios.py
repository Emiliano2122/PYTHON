import random
import math

def separa():
    print("")
    print("----------")
    print("")

print(random.random())

separa()

print(random.random())
print(random.random())
print(random.random())

separa()

# random.seed(10)

print(random.random())
print(random.random())
print(random.random())

separa()

i = 1
limite = 5

while i <= limite:
    print(random.random())
    i += 1

separa()

# randrange genera un numero entre un rango determinado
# 4, 5, 6, 7, 8
print(random.randrange(3, 9))
print(random.randrange(3, 9))

separa()

i = 0

while i <= limite:
    print(random.randrange(2, 9))
    i += 1

separa()

# randrange genera un numero entre un rango determinado
# 3, 4, 5, 6, 7, 8, 9
print(random.randint(3, 9))

separa()

# genero numeros aleatorios con decimales

print(random.uniform(20, 60))

i = 1

while i <= limite:
    print(random.uniform(20, 60))
    i += 1

separa()

a = 1.23456
print(a)

print("Redondea hacia ariba")
print(math.ceil(a))

separa()

print("Redondea hacia abajo")
print(math.floor(a))

separa()

print("Trunca los decimales")
print(math.trunc(a))

