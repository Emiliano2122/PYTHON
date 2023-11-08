# loops o ciclos
#
#python solo tiene dos comandos para ciclos
#
# while
# for
# ========================

limite = 10
contador = 1

while contador <= 10: # este ciclo se ejecuta mientras esta condicion ser verdadera
    print (contador)
    contador += 1 # contador = contador +1

# -=
# *=
# /=
desde = 1
hasta = 10

while desde <= hasta:
    print(desde)
    desde +=1

desde = 1
limite = 10
while desde <= limite:
    print(desde)
    desde +=2

# en ciclos los nombre de las variables a utilizar son:
# i, j, k, ...

# ciclos desendente

i = 10
while i >= 1:
    print(i)
    i -= 1
    
# obtener la suma de los 3 primeros numeros naturales tarea

suma = 0
i = 1

while i <= 3:
    suma = suma + i
    print(i)
    i += 1
print("La suma es", suma)

# obtener la suma de los 10 primeros numeros naturales

i = 1
tabla = 10

while i <= 10:
    print(tabla, "x" ,i, "=" ,tabla * i)
    i += 1

i = 1
ahorro = 0

while i <= 7:
    ahorro += i
    print(i)
    i += 1
print("Ahorrado", ahorro)

i = 1
ahorro = 0

while i <= 365:
    ahorro += i
    print(i)
    i += 1
print("Ahorrado en un año", ahorro)    

# muesta los numeros nones menores de 10
# 1, 3, 5, 7, 9, 11, 13, 15, 17
i = 1

while i <= 10:
    print(i)
    i += 2
    
# muestra los numeros pares menores de 10
# 2, 4 ,6 , 8, 10
i = 2

while i <= 10:
    print(i)
    i += 2

# la suma de los nones  1 al 10
suma = 0
i = 1

while i <= 10:
    suma += i
    print(i)
    i += 2
print("la suma es", suma)


# suma de los  pares del 1 al 10
suma = 0
i = 2

while i <= 10:
    suma += i
    print(i)
    i += 2
print("la suma es", suma)


# suma de los nones menores que 100
suma = 0
i = 1

while i <= 100:
    suma += i
    print(i)
    i += 2
print("la suma es", suma)

# suma de los pares menores que 100
suma = 0
i = 2

while i <= 100:
    suma += i
    print(i)
    i += 2
print("la suma es ", suma)

# break rompe o interrumpe el ciclo
i = 1

while i <= 100:
    print(i)
    if i == 20: # pregunta si i es igual a 20
        break   # 
    i += 1

# muestra el numero mayor
a = 50
b = 89

print("De los numeros", a, "y", b)
if a > b:
    print("El mayor",a)
else:
    print("El mayor",b)

# muestra el numero menor
a = 9
b = 18

if a < b:
    print("El menor es", a)
else:
    print("El mayor es", b)
    
# muestra el numeros mayor
a = 100
b = 20
c = 3

if a > b:
    if a > c:
        print("El mayor es", a)
    else:
        if b > c:
            print("El mayor es", b)
        else:
            print("El mayor es", c)

# Detectar el numero menor de 3 numeros tarea
a = 30
b = 5
c = 20

if a < b:
    if a < c:
        print("El menor es", a)
    else:
        print("El menor es", c)
else:
    if b < c:
        print("El menor es", b)
    else:
        print("El menor es", c)
    

