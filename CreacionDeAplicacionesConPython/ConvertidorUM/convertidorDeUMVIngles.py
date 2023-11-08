def separa():
    print("")
    print("-----------------")
    print("")

# volumen
#
# 1 galon   -> onzas 128 gl     
# 1 onzas fluidas  -> 0.0078 fl


def convUMVIngles(x, umDe, umA):
    if umDe == "gl":
        if umA == "gl":
            return("{:,.2f} gl".format(x))
        if umA == "oz":
            a = x * 16.410
            return("{:,.2f} oz".format(a))
    elif umDe == "oz":
        if umA == "oz":
          return("{:,.2f} oz".format(x))
        if umA == "gl":
            a = x * 0.0078125
            return("{:,.6f} oz".format(a))


 
print(convUMVIngles(1, "oz", "gl"))
print(convUMVIngles(1, "oz", "oz"))