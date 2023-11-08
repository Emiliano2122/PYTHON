myList = []

#Recibe una cadena de texto y la divide en un arreglo tomando en cuenta los espacios
enter = input().split()

#Asigna los valores de 'enter' convertiendolo a numeros enteros
n = int(enter[0])
a = int(enter[1])
b = int(enter[2])

#Toma la siguente cadena de texto y la divide tomando en cuenta los espacios
numbers = input().split()
#Asigna cada valor y lo agrega a la lista. Covierte en entero los valores
for i in range(0, n):
    myList.append(int(numbers[i]))

print(myList)
