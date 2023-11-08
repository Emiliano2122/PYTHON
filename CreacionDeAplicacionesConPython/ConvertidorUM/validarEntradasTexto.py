def separa():
    print("")
    print("-----------------")
    print("")

def espacios(i):
    if i<0:
        i = 1
    contador = 1
    while contador <= i:
        print("")
        contador += 1

def inicio():
    espacios(3)
    print("\t\t\tconvertidor de unidades de medida")
    espacios(2)
    print("\t\t\t\t\t\t\t\t* para terminar")
    espacios(2)
    print("\t\t\t\t\tP eso")
    print("\t\t\t\t\tV olumen")
    print("\t\t\t\t\tL ongitud")
    espacios(2)

def sistema():
    espacios(3)
    print("\t\t\tconvertidor de unidades de medida")
    espacios(2)
    print("\t\t\t\t\t\t\t\t* para termina")
    espacios(2)
    print("\t\t\t\t\tsistema Metrico decimal")
    print("\t\t\t\t\tsistema Ingles")
    espacios(2)

def opcionesIngles():
    espacios(3)
    print("\t\t\tconvertidor de unidades de medida")
    espacios(2)
    print("\t\t\t\t\t\t\t\t* para termina")
    espacios(2)
    print("\t\t\t\t\tm\tmilla")
    print("\t\t\t\t\tyd\tyarda")
    print("\t\t\t\t\tft\tpie")
    print("\t\t\t\t\tin\tpulgadas")
    espacios(2)

def opcionesMetrico():
    separa()
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
    print("\t\t\t\t\tKm\tkilometro")
    print("\t\t\t\t\tm\tmetro")
    print("\t\t\t\t\tdm\tdecimetro")
    print("\t\t\t\t\tcm\tcentimetro")
    print("\t\t\t\t\tmm\tmilimetro ")
    print("")
    print("")

def opcionesMetrico():
    separa()
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
    print("\t\t\t\t\tKm\tkilometro")
    print("\t\t\t\t\tm\tmetro")
    print("\t\t\t\t\tdm\tdecimetro")
    print("\t\t\t\t\tcm\tcentimetro")
    print("\t\t\t\t\tmm\tmilimetro ")
    print("")
    print("")

def opcionesIngles():
    espacios(3)
    print("\t\t\tconvertidor de unidades de medida")
    espacios(2)
    print("\t\t\t\t\t\t\t\t* para termina")
    espacios(2)
    print("\t\t\t\t\tlb\tlibra")
    print("\t\t\t\t\toz\tonza")
    print("\t\t\t\t\tT\tTonelada")
    espacios(2)
    
def convUMIngles(x, umDe, umA):
    if umDe == "m":
        if umA == "m":
            return("{:,.2f} m".format(x))
        if umA  == "yd":
            a = x * 1760
            return("{:,.2f} yd".format(a))
        elif umA == "ft":
            a = x * 5280
            return("{:,.2f} ft".format(a))
        elif umA == "in":
            a = x * 63360
            return("{:,.2f} in".format(a))        
    elif umDe == "yd":
        if umA == "yd":
            return("{:,.2f} yd".format(x))
        if umA == "m":
            a = x * 0.0005682
            return("{:,.6f} m".format(a))
        elif umA == "ft":
            a = x * 3
            return("{:,.2f} ft".format(a))
        elif umA == "in":
            a = x * 36000
            return("{:,.2f} in".format(a))
    elif umDe == "ft":
        if umA == "ft":
            return("{:,.2f} ft".format(x))
        if umA == "m":
            a = x * 0.0001894
            return("{:,.6f} m".format(a))
        elif umA == "yd":
            a = x * 0.333333
            return("{:,.2f} yd".format(a))
        elif umA == "in":
            a = x * 1200
            return("{:,.2f} in".format(a))   
    elif umDe == "in":
        if umA == "in":
            return("{:,.2f} in".format(x))
        if umA == "m":
            a = x / 63360
            return("{:,.6f} m".format(a))
        elif umA == "yd":
            a = x / 1760
            return("{:,.6f} yd".format(a))
        elif umA == "ft":
            a = x / 5280
            return("{:,.6f} ft".format(a))

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

def convUMPMetrico(x, umDe, umA):
    if umDe == "Kg":
        if umA == "Kg":
            return("{:,.2f} Kg".format(x))
        if umA == "Hg":
            a = x * 100
            return("{:,.2f} Hg".format(a))
        elif umA == "Dg":
            a = x * 100
            return("{:,.2f} Dg".format(a))
        elif umA == "g":
            a = x * 1000
            return("{:,.2f} g".format(a))
        elif umA == "dg":
            a = x * 10000
            return("{:,.2f} dg".format(a))
        elif umA == "cg":
            a = x * 100000
            return("{:,.2f} cg".format(a))
        elif umA == "mg":
            a = x / 1000000
            return("{:,.6f} mg".format(a))
    elif umDe == "Hg":
        if umA == "Hg":
           return("{:,.2f} Hg".format(x))
        if umA == "Kg":
            a = x / 0.1
            return("{:,.2f} Kg".format(a))
        elif umA == "Dg":
            a = x * 10
            return("{:,.2f} Dg".format(a))
        elif umA == "g":
            a = x * 100
            return("{:,.2f} g".format(a))
        elif umA == "dg":
            a = x * 1000
            return("{:,.2f} dg".format(a))
        elif umA == "cg":
            a = x * 10000
            return("{:,.2f} cg".format(a))
        elif umA == "mg":
            a = x * 100000
            return("{:,.6f} mg".format(a))
    elif umDe == "Dg":
        if umA == "Dg":
            return("{:,.2f} Dg".format(x))
        if umA == "Kg":
            a = x / 0.01
            return("{:,.2f} Kg".format(a))
        elif umA == "Hg":
            a = x / 0.1
            return("{:,.2f} Hg".format(a))
        elif umA == "g":
            a = x * 10
            return("{:,.2f} g".format(a))
        elif umA == "dg":
            a = x * 100
            return("{:,.2f} dg".format(a))
        elif umA == "cg":
            a = x * 1000
            return("{:,.2f} cg".format(a))
        elif umA == "mg":
            a = x * 10000
            return("{:,.6f} mg".format(a))
    elif umDe == "g":
        if umA == "g":
            return("{:,.2f} g".format(x))
        if umA == "Kg":
            a = x / 0.001
            return("{:,.2f} Kg".format(a))
        elif umA == "Hg":
            a = x / 0.01
            return("{:,.2f} Hg".format(a))
        elif umA == "Dg":
            a = x / 0.1
            return("{:,.2f} Dg".format(a))
        elif umA == "dg":
            a = x * 10
            return("{:,.2f} dg".format(a))
        elif umA == "cg":
            a = x * 100
            return("{:,.2f} cg".format(a))
        elif umA == "mg":
            a = x * 1000
            return("{:,.2f} mg".format(a))
    elif umDe == "dg":
        if umA == "dg":
            return("{:,.2f} dg".format(x))
        if umA == "Kg":
            a = x / 0.0001
            return("{:,.2f} Kg".format(a))
        elif umA == "Hg":
            a = x / 0.001
            return("{:,.2f} Hg".format(a))
        elif umA == "Dg":
             a = x / 0.01
             return("{:,.2f} Dg".format(a))
        elif umA == "g":
            a = x / 0.1
            return("{:,.2f} g".format(a))
        elif umA == "cg":
            a = x * 10
            return("{:,.2f} cg".format(a))
        elif umA == "mg":
            a = x * 100
            return("{:,.2f} mg".format(a))
    elif umDe == "cg":
        if umA == "cg":
            return("{:,.2f} cg".format(x))
        if umA == "Kg":
            a = x * 1e-5
            return("{:,.6f} Kg".format(a))
        elif umA == "Hg":
            a = x / 0.0001
            return("{:,.2f} Hg".format(a))
        elif umA == "Dg":
            a = x / 0.001
            return("{:,.2f} Dg".format(a))
        elif umA == "g":
            a = x / 0.01
            return("{:,.2f} g".format(a))
        elif umA == "dg":
            a = x / 0.1
            return("{:,.2f} dg".format(a))
        elif umA == "mg":
            a = x * 10
            return("{:,.2f} mg".format(a))
    elif umDe == "mg":
        if umA == "mg":
            return("{:,.2f} mg".format(x))
        if umA == "Kg":
            a = x * 1e-6
            return("{:,.6f} Kg".format(a))
        elif umA == "Hg":
            a = x * 1e-5
            return("{:,.6f} Hg".format(a))
        elif umA == "Dg":
            a = x * 1e-4
            return("{:,.6f} Dg".format(a))
        elif umA == "g":
            a = x / 0.001
            return("{:,.2f} g".format(a))
        elif umA == "dg":
            a = x / 0.01
            return("{:,.2f} dg".format(a))
        elif umA == "cg":
            a = x / 0.1
            return("{:,.2f} cg".format(a))

def convUMPIngles(x, umDe, umA):
    if umDe == "lb":
        if umA == "lb":
            return("{:,.2f} lb".format(x))
        if umA == "oz":
            a = x * 16
            return("{:,.2f} oz".format(a))
        elif umA == "T":
            a = x * 0.0004536
            return("{:,.6f} T".format(a))
    elif umDe == "oz":
        if umA == "oz":
            return("{:,.2f} oz".format(x))
        if umA == "lb":
            a = x * 0.06
            return("{:,.2f} lb".format(a))
        elif umA == "T":
            a = x * 0.00002835
            return("{:,.6f} T".format(a))
    elif umDe == "T":
        if umA == "T":
           return("{:,.2f} T".format(x))
        if umA == "lb":
            a = x * 2205
            return("{:,.2f} lb".format(a))
        elif umA == "oz":
            a = x * 35274
            return("{:,.2f} oz".format(a))


separa()

opcion = ""

# P / V / L
while opcion != "P" and opcion != "V" and opcion != "L":
    if opcion == "*":
        break
    
    inicio()
    opcion = input("\t\t\t\tOpcion : ")
    
    if opcion == "L":
        opcion2 = ""
        while opcion2 != "M" and opcion2 != "I":
            if opcion2 == "*":
                # inicializo la variable del loop anterior para que regrese
                opcion2 = ""
                break
            
            sistema()
            opcion2 = input("\t\t\t\t¿Que sistema deseas trabajar? : ")
            
            if opcion2 == "I":
                opcion3 = ""
                while opcion3 != "m" and opcion3 != "yd" and opcion3 != "ft" and opcion3 != "in":
                    if opcion3 == "*":
                        # inicializo la variable del loop anterior para que regrese
                        opcion2 = ""
                        break
                    
                    opcionesIngles()
                    opcion3  = input("                             convertir : ")
                    
                    if opcion3 == "*":
                        # inicializo la variable del loop anterior para que regrese
                        opcion2 = ""
                        break
                    
                    opcion4  = input("                                     A : ")
                    cantidad  = input("                             cantidad : ")
                    
                    
                    cantidad = float(cantidad)
                    
                    resultado = convUMIngles(cantidad, opcion3, opcion4)
                    print("")
                    print("")
                    print("                                Resultado : ", resultado)
                    
                    opcion3 = input("Enter para continuar")
            elif opcion2 == "M":
                opcion3 = ""
                while opcion3 != "Km" and opcion3 != "m" and opcion3 != "dm" and opcion3 != "cm" and opcion3 != "mm":
                    if opcion3 == "*":
                        # inicializo la variable del loop anterior para que regrese
                        opcion2 = ""
                        break
                    
                    opcionesMetrico()
                    opcion3  = input("                             convertir : ")
                    
                    if opcion3 == "*":
                        # inicializo la variable del loop anterior para que regrese
                        opcion2 = ""
                        break
                    
                    opcion4  = input("                                     A : ")
                    cantidad  = input("                             cantidad : ")
                    
                    
                    cantidad = float(cantidad)
                    
                    resultado = convUM(cantidad, opcion3, opcion4)
                    print("")
                    print("")
                    print("                                Resultado : ", resultado)
                    
                    opcion3 = input("Enter para continuar")
            
opcion = ""

# P / V / L
while opcion != "P" and opcion != "V" and opcion != "L":
    if opcion == "*":
        break
    
    inicio()
    opcion = input("\t\t\t\tOpcion : ")
    
    if opcion == "P":
        opcion2 = ""
        while opcion2 != "M" and opcion2 != "I":
            if opcion2 == "*":
                # inicializo la variable del loop anterior para que regrese
                opcion2 = ""
                break
            
            sistema()
            opcion2 = input("\t\t\t\t¿Que sistema deseas trabajar? : ")
            
            if opcion2 == "I":
                opcion3 = ""
                while opcion3 != "lb" and opcion3 != "oz" and opcion3 != "T":
                    if opcion3 == "*":
                        # inicializo la variable del loop anterior para que regrese
                        opcion2 = ""
                        break
                    
                    opcionesIngles()
                    opcion3  = input("                             convertir : ")
                    
                    if opcion3 == "*":
                        # inicializo la variable del loop anterior para que regrese
                        opcion2 = ""
                        break
                    
                    opcion4  = input("                                     A : ")
                    cantidad  = input("                             cantidad : ")
                    
                    
                    cantidad = float(cantidad)
                    
                    resultado = convUMIngles(cantidad, opcion3, opcion4)
                    print("")
                    print("")
                    print("                                Resultado : ", resultado)
                    
                    opcion3 = input("Enter para continuar")
            
            
                