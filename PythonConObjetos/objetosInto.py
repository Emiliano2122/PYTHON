# Importamos math Library
import math

# Print the value of pi
print(math.pi)

def separa():
    print("")
    print("-------------")
    print("")

# oop in python
# object oriented programming
# class

# class es un conductor de objeto
# y por lo tanto "modela" o crea un objeto

class MiClase:
    x = 5

class MiObjeto:
    y = 25.8902

separa()

# los objetos modeloados no se pueden manipular
# tengo que hacer una instancia (Copia) del objeto para manipular

objeto1 = MiClase()

objeto2 = MiObjeto()

print(objeto1.x)
print(objeto2.y)

# objeto propiede
# clase.propiede

separa()

# un objeto puede tener n propiedes

class MiClase2:
    x = 179.75
    a = "OEVA"

objeto3 = MiClase2()

print(objeto3.x)
print(objeto3.a)

separa()

# estufa.alto
# estufa.ancho
# estufa.largo
# estufa.color
# estufa.NoQemaduras
# estufa.precio
# estufa.peso

# todas las clases tienen una funcion llamada __int__()
# y siempre se ejecuta al crear el objeto o al hacer la instancia (Copia)
# doble guion bajo antes y despues del init
# doble espacio entes y despues __init__

class Persona:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

# las propiedades del objeto persona son:
# name
# age

persona1 = Persona("Sebastian", 30)

print(persona1.name)
print(persona1.age)

persona2 = Persona("Emiliano", 19)

print(persona2.name)
print(persona2.age)

separa()

class Usuario:
    def  __init__  (self, nombre, paterno, materno):
         self.nombre = nombre
         self.paterno = paterno
         self.materno = materno
         self.estatus = True

# metodos (funciones) de una clase

    def nombreCompleto(self):
        print(self.nombre + " " + self.paterno + " " + self.materno)
    
    def nombreListado(self):
        print(self.paterno + " " + self.materno + " "  + self.nombre)
    
    def estatusUsuario(self):
        print(self.estatus)


usuario1 = Usuario("Emiliano", "Stasi", "Fernandez")
usuario1.nombreCompleto()
usuario1.nombreListado()
usuario1.estatusUsuario()

separa()

usuario1.estatus = False
usuario1.estatusUsuario()

separa()

# en algebra usamos las literles x, y, z
# para literiales que no conocemos

# usamos a, b, c etc.
# para literales que SI CONOCEMOS
class Triangulo:
    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        print(self.a + self.b + self.c)
    
    def area(self):
        print(self.a  *  self.c / 2)
# triangulo equilatero
# aquel triangulo que todos sus lados son inguales

# triangulo escaleno
# aquel triangulo que todos sus lados no son iguales
triangulo1 = Triangulo(5, 6, 7)
triangulo1.perimetro()
triangulo1.area()

separa()

# triangulo isoseles
# aquel triangulo que tiene 2 lados iguales
triangulo2 = Triangulo(10, 10, 1)
triangulo2.perimetro()
triangulo2.area()

separa()

triangulo3 = Triangulo(3, 3, 3)
triangulo3.perimetro()
triangulo3.area()

separa()

class Cuadrado:
    def __init__ (self, a):
        self.a = a
        print("Clase Cuadrado")
    
    def perimetro(self):
        print(self.a * 4)
    
    def area(self):
        print(self.a * self.a)

cuadrado1 = Cuadrado(12)
cuadrado1.perimetro()
cuadrado1.area()

separa()
    
cuadrado2 = Cuadrado(1)
cuadrado2.perimetro()
cuadrado2.area()

separa()

class Rectangulo:
    def __init__ (self, a, b):
        self.a = a
        self.b = b
  
    
    def perimetro(self):
        # print((self.a * 2) + (self.b * 2))
        return ((self.a * 2) + (self.b * 2))
    
    def area(self):
        return (self.a * self.b)
    
    
rectangulo1 = Rectangulo(2, 5)

perim = rectangulo1.perimetro()
area1 = rectangulo1.area()

print("El perimetro es: ", perim, "m")
print("El perimetro de mis dos terrenos es: ", perim * 2, "cm")
print("El área es: ", area1, "m2")

# cm, m, km
# cm2, m2 ha

separa()

class Circulo:
    def __init__ (self, radio):
        self.radio = radio
    
    def perimetro(self):
        return( 2 * 3.1416 * self.radio)
    
    def area(self):
        return(self.radio ** 2)* math.pi

circulo1 = Circulo(1)
print("Circulo")
perimetro = circulo1.perimetro()
area = circulo1.area()
    
    
print(perimetro)
print(area)

separa()

class Elipse:
    def __init__ (self, a, b):
        self.a = a
        self.b = b
    
    def perimetro(self):
        return((self.a * 2) + (self.b * 2))
    
    def area(self):
        return(self.a  +  self.b / 2)

elipse1 = Elipse(5, 2)

perimetro = elipse1.perimetro()
area = elipse1.area()

print(perimetro)
print(area)

separa()

class Hexagono:
    def __init__ (self, apotema, lado):
        self.apotema = apotema
        self.lado = lado
    
    def perimetro(self):
        return((self.apotema * 2) + (self.lado * 2))
    
    def area(self):
        return(self.apotema * self.lado)

hexagono1 = Hexagono(3, 2)

perimetro = hexagono1.perimetro()
area = hexagono1.area()

print(perimetro)
print(area)

separa()

# herencia
# Sirve para crear nuevas clases a partir de clases preexistentes

# clase cuadrado

class Cubo(Cuadrado):
    pass

cubo1 = Cubo(12)
cubo1.perimetro()
cubo1.area()



# primaEliptico
# prismaHexagonal

class PrismaRectangular(Rectangulo):
    pass

prismaRectangular1 = PrismaRectangular(2, 5)
prismaRectangular1.perimetro()
prismaRectangular1.area()

separa()

# clase Circulo

class Cilindro(Circulo):
    pass

print("Clase Cilindro")
cilindro1 = Cilindro(1)
variable = cilindro1.area()
print(variable)

