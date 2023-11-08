def separa():
    print("")
    print("-----------------")
    print("")
    
# 1 Tonelada = 2204.63 lb
# 1 libra = 16 oz
# 1 onza = 28.3495 gr 


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
           
print(convUMPIngles(1, "oz", "T"))
print(convUMPIngles(1, "oz", "lb"))
print(convUMPIngles(1, "oz", "oz"))

      