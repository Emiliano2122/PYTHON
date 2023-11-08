def separa():
    print("")
    print("-----------------")
    print("")

# 1 milla = 1760 yd
# 1 yd = 3 ft
# 1 ft = 12 in
# 1 in = 2.54 cm

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
    

print(convUMIngles(1, "m", "yd"))
print(convUMIngles(1, "yd", "ft"))
print(convUMIngles(1, "ft", "in"))
print(convUMIngles(1, "m", "ft"))
print(convUMIngles(1, "m", "in"))
print(convUMIngles(1, "in", "m"))
print(convUMIngles(1, "in", "yd"))
print(convUMIngles(1, "in", "ft"))
