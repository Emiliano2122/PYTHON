def separa():
    print()
    print("----------")
    print()

myTuple = ("rojo", "rosa", "verde")
print(myTuple)

separa()

myTuple2 = ("teclado")

print(type(myTuple2))

separa()

myTuple3 = ("teclado",)
print(type(myTuple3))

separa()

tuple1 = ("ford", "nissan", "chrysler")
tuple2 = (9, 8, 9, 10)
tuple3 = (False, True, True)

print(tuple1)
print(tuple2)
print(tuple3)

separa()

alumno1 = ("Emiliano", 19, True, 68.500)
print(alumno1)

separa()

print(type(alumno1))

separa()

# explicitamente defino un tuple

datosX = tuple(("Antonio", True, 899, 87.897))

print(datosX)
print(type(datosX))

separa()

# acceso a un elemento del tuple

estados = ("Mexico", "Hidalgo", "Puebla", "Nuevo Leon", "Guadalajara")
print(estados)

print(estados[0])

print(estados[2])

print(estados[-1])

print(estados[-2])

print(estados[2:5])

print(estados[2:9])

print(estados[:3])

print(estados[2:])

separa()

frutas = ("fresa", "kiwi", "mango", "sandia")

if "manzana" in frutas:
    print("SI existe manzana es frutas")
else:
    print("NO existe manzana en frutas")
    
print(frutas)    

separa()
# tuple no se puede cambiar

# frutas[2] = "manazana"

print(frutas)

z = list(frutas)
z[2] = "manzana"
frutas = tuple(z)

print(frutas)

separa()

# tuple NO permite agregar más elementos
# frutas.appende("gallina")

z = list(frutas)
z.append("Gallina")
frutas = tuple(z)

print(frutas)

separa()

z = list(frutas)
z.remove("Gallina")
frutas = tuple(z)

print(frutas)

separa()

print(frutas)
del frutas
# print(frutas)

separa()

# desempacar un tuple
misFrutas = ("sandia", "fresa", "melon", "kiwi")
print(misFrutas)

(s, f, m, k) = misFrutas

print(s)
print(f)
print(m)
print(k)

separa()

# usando el * para los demas elementos o items del tuple

misCalificaciones = (9, 8, 7, 6, 10)
(uno, dos, *tres) = misCalificaciones

print(uno)
print(dos)
print(tres)

separa()

(uno, *dos, tres) = misCalificaciones
print(uno)
print(dos)
print(tres)

separa()

for x in misFrutas:
    print(x)

for y in misCalificaciones:
    print(y)

separa()

print(misFrutas[0])

separa()

for i in range(len(misFrutas)):
    print(misFrutas[i])
    
separa()

i = 0

while i < (len(misFrutas)):
    print(misFrutas[i])
    i += 1

separa()

diasLaborables = ("Lun", "Mar", "Mie", "Jue", "Vie")
diasNoLaborables = ("Sab", "Dom")

semana = diasLaborables + diasNoLaborables

print("Dias laborables")
print(diasLaborables)
print()

print("Dias NO laborables")
print(diasNoLaborables)
print()

print("semana completa")
print(semana)

separa()

quincena = semana * 2

print("Quincena")
print(quincena)

mes = quincena * 2

print("Mes")
print(mes)

separa()

print(mes.count("Lun"))

separa()

print(mes.index("Mar"))

separa()