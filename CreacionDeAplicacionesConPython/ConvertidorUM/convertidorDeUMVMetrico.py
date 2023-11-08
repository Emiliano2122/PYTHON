def separa():
    print("")
    print("-----------------")
    print("")

# volumen
#
# kilimetro cubico km3
# hectometro cubico hm3
# decametro cubico dam3
# metro cubico m3
# decimetro cubico dm3
# centimetro cubico cm3
# milimetro cubico mm3

# 1 kilometro cubico -> hectometro cubico 1000 hm3
# 1 hectometro cubico -> decametro cubico 1000 dam3
# 1 decametro cubico -> metro cubico 1000 m3
# 1 metro cubico -> decimetro cubico 1000 dm3
# 1 decimetro cubico -> centimetro cubico 1000 cm3
# 1 centimetro cubico -> milimetro cubico 1000 mm3

def convUMVMetrico(x, umDe, umA):
    if umDe == "Km3":
        if umA == "Km3":
            return("{:,.2f} Km3".format(x))
        if umA == "hm3":
            a = x * 1000
            return("{:,.2f} hm3".format(a))
        elif umA == "dam3":
            a = x * 1000000
            return("{:,.2f} dam3".format(a))
        elif umA == "m3":
            a = x * 1000000000
            return("{:,.2f} m3".format(a))
        elif umA == "dm3":
            a = x * 1000000000000
            return("{:,.2f} dm3".format(a))
        elif umA == "cm3":
            a = x * 1000000000000000
            return("{:,.2f} cm3".format(a))
        elif umA == "mm3":
            a = x * 1000000000000000000
            return("{:,.2f} mm3".format(a))
    elif umDe == "hm3":
        if umA == "hm3": 
            return("{:,.2f} hm3".format(x))
        if umA == "Km3":
            a = x * 1000
            return("{:,.2f} Km3".format(a))
        elif umA == "dam3":
            a = x * 1000
            return("{:,.2f} dam3".format(a))
        elif umA == "m3":
            a = x * 1000000
            return("{:,.2f} m3".format(a))
        elif umA == "dm3":
            a = x * 1000000000
            return("{:,.2f} dm3".format(a))
        elif umA == "cm3":
            a = x * 1000000000000
            return("{:,.2f} cm3".format(a))
        elif umA == "mm3":
            a = x * 1000000000000000
            return("{:,.2f} mm3".format(a))
    elif umDe == "dam3":
        if umA == "dam3":
           return("{:,.2f} dam3".format(x))
        if umA == "Km3":
            a = x * 1000
            return("{:,.2f} Km3".format(a))
        elif umA == "m3":
            a = x * 1000
            return("{:,.2f} m3".format(a))
        elif umA == "dm3":
            a = x * 1000000
            return("{:,.2f} dm3".format(a))
        elif umA == "cm3":
            a = x * 1000000000
            return("{:,.2f} cm3".format(a))
        elif umA == "mm3":
            a = x * 1000000000000
            return("{:,.2f} mm3".format(a))
    elif umDe == "m3":
        if umA == "m3":
            return("{:,.2f} m3".format(x))
        if umA == "Km3":
            a = x * 1000
            return("{:,.2f} Km3".format(a))
        elif umA == "dm3":
            a = x * 1000
            return("{:,.2f} dm3".format(a))
        elif umA == "cm3":
            a = x * 1000000
            return("{:,.2f} cm3".format(a))
        elif umA == "mm3":
            a = x * 1000000000
            return("{:,.2f} mm3".format(a))
       
print(convUMVMetrico(1, "m3", "Km3"))
print(convUMVMetrico(1, "m3", "dm3"))
print(convUMVMetrico(1, "m3", "cm3"))
print(convUMVMetrico(1, "m3", "mm3"))
print(convUMVMetrico(1, "m3", "m3"))

