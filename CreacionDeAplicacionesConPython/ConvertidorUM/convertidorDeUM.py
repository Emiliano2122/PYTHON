def separa():
    print("")
    print("-----------------")
    print("")

def inicio():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("\t\t\tconvertidor de unidades de medida")
    print("")
    print("")
    print("\t\t\t\t\t\t\t\t* para terminar")
    print("")
    print("")
    print("")
    print("")
    print("\t\t\t\t\tP eso")
    print("\t\t\t\t\tV olumen")
    print("\t\t\t\t\tL ongitud")
    print("")
    print("")

def sistema():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("\t\t\tconvertidor de unidades de medida")
    print("")
    print("")
    print("\t\t\t\t\t\t\t\t* para termina")
    print("")
    print("")
    print("\t\t\t\t\tsistema Metrico decimal")
    print("\t\t\t\t\tsistema Ingles")

def opcionesIngles():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("\t\t\tconvertidor de unidades de medida")
    print("")
    print("")
    print("\t\t\t\t\t\t\t\t* para termina")
    print("")
    print("")
    print("\t\t\t\t\tm\tmilla")
    print("\t\t\t\t\tyd\tyarda")
    print("\t\t\t\t\tft\tpie")
    print("\t\t\t\t\tin\tpulgadas")
    print("")
    print("")

def opcionesDecimal():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("\t\t\tconvertidor de unidades de medida")
    print("")
    print("")
    print("\t\t\t\t\t\t\t\t* para termina")
    print("")
    print("")
    print("\t\t\t\t\tsistema Metrico decimal")
    print("\t\t\t\t\tsistema Ingles")
    print("")
    print("")

# convertidor de unidades de medida

# P peso
# V volumen
# L longitud

# definir la interface
# definir las UM de los apartados
# por funciones o por objetos

# Peso

# sistema decimal
#
# kilogramos  Kg
# hectogramo  Hg
# decagramo   Dag
# gramo       g
# decigramo   dg
# centigramos cg
# miligramos   mg

# sistema ingles
#
# libras     lb  
# onzas      oz
# toneladas   t

# volumen
#
# sistema decimal
#
# kilimetro cubico
# decagramo cubico
# metro cubico
# decimetro cubico
# centimetro cubico
# milimetro cubico

# sitema ingles
#
# galon          gl
# onzas fluidas  fl

# longitud
#
# sistema decimal
#
# kilogramo    km
# metro        m
# decimetro    dm
# centimetro   cm
# milimetro    mm

# sistema ingles
#
# milla     m
# yarda     yd
# pie       ft
# pulgada   in

# 1 milla -> yardas 1760
# 1 yarda -> pies 3
# 1 pie -> pulgadas 12

# 1 kilometro -> metros 1000
# 1 metro -> decimetro 10
# 1 decimetro -> centimetros 10
# 1 centimetro -> milimetros 10

# regla para convertir unidades
#
# UM1        UM2       Cantidad
# 3.85       km          m
# =====      ====      =======

def convUM(x, umDe, umA):
    if umDe == "Km":
        if umA == "Km":
            return("{:,.2f} Km".format(x))
        if umA  == "m":
            a = x * 1000
            return("{:,.2f} m".format(a))
        elif umA == "dm":
            a = x * 10000
            return("{:,.2f} dm".format(a))
        elif umA == "cm":
            a = x * 100000
            return("{:,.2f} cm".format(a))
        elif umA == "mm":
            a = x * 1000000
            return("{:,.2f} mm".format(a))
    elif umDe == "m":
        if umA == "m":
            return("{:,.2f} m".format(x))
        if umA == "Km":
            a = x * 0.001
            return("{:,.6f} Km".format(a))
        elif umA == "dm":
            a = x * 10
            return("{:,.2f} dm".format(a))
        elif umA == "cm":
            a = x * 100
            return("{:,.2f} cm".format(a))
        elif umA == "mm":
            a = x * 100000
            return("{:,.2f} mm".format(a))
  
    elif umDe == "dm":
        if umA == "dm":
            return("{:,.2f} m".format(x))
        if umA == "Km":
            a = x * 0.0001
            return("{:,.6f} Km".format(a))
        elif umA == "m":
            a = x * 0.1
            return("{:,.2f} m".format(a))
        elif umA == "cm":
            a = x * 1000
            return("{:,.2f} cm".format(a))
        elif umA == "mm":
            a = x * 100
            return("{:,.2f} mm".format(a))   
    elif umDe == "cm":
        if umA == "cm":
            return("{:,.2f} cm".format(x))
        if umA == "Km":
            a = x * 0.0001
            return("{:,.6f} Km".format(a))
        elif umA == "m":
            a = x * 0.01
            return("{:,.2f} m".format(a))
        elif umA == "dm":
            a = x * 10
            return("{:,.2f} dm".format(a))
        elif umA == "mm":
            a = x * 10
            return("{:,.2f} mm".format(a))
    elif umDe == "mm":
        if umA == "mm":
           return("{:,.2f} mm".format(x))
        if umA == "km":
            a = x * 0.0025
            return("{:,.6f} km".format(a))
        elif umA == "m":
            a = x * 0.001
            return("{:,.2f} m".format(a))
        elif umA == "dm":
            a = x / 10
            return("{:,.2f} dm".format(a))
        elif umA == "cm":
            a = x * 0.10
            return("{:,.2f} cm".format(a))
        





# def convUMIngles(x, umDe, umA):


# print(convUM(3.5, "Km", "m"))

separa()

# print(convUM(1, "Km", "m"))

separa()

# print(convUM(1, "cm", "cm"))

# print(convUM(1, "cm", "m"))

# print(convUM(1, "cm", "dm"))

#print(convUM(1, "cm", "mm"))

#print(convUM(3.75, "cm", "Km"))

inicio()

opcion = input("\t\t\t\tOpcion : ")

sistema()

sistema = input("\t\t\t\tOpcion : ")

if sistema == "I":
    opcionesIngles()


# 1 milla = 1760 yd
# 1 yd = 3 ft
# 1 ft = 12 in
# 1 in = 2.54 cm
