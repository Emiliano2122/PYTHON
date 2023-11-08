def separa():
    print("")
    print("-----------------")
    print("")

# Peso
#
# kilogramos  Kg
# hectogramo  Hg
# decagramo   Dg
# gramo       g
# decigramo   dg
# centigramos cg
# miligramos   mg

# 1 Kilogramo -> Hectogramo 10 Hg
# 1 Hectogramo -> Decagramo 10 Dg
# 1 Decagramo -> gramo 10 g
# 1 gramo -> decigramo 10 dg
# 1 decigramo -> centigramo 10 cg
# 1 centigramo -> miligramo 10 mg


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
            
            
                    
print(convUMPMetrico(1, "mg", "Kg"))
print(convUMPMetrico(1, "mg", "Hg"))
print(convUMPMetrico(1, "mg", "Dg"))
print(convUMPMetrico(1, "mg", "g"))
print(convUMPMetrico(1, "mg", "dg"))
print(convUMPMetrico(1, "mg", "cg"))
print(convUMPMetrico(1, "mg", "mg"))




            