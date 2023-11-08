def separa():
    print("")
    print("-------------")
    print("")

# desgolosar el IVA de una contidad dada

total = 107.50
IVA = .16

importe = total / (1 + IVA)

print(importe)
importeIVA = total - importe
print(importeIVA)
print(total)

separa()

def desglosarIVA(total):
    return(total/1.16)

importe = desglosarIVA(107.50)

print(importe)

separa()

ingresos2019 = 176520
ingresos2020 = 198765

# ingresos2019 - 100%
# ingresos2020 -   x

x = (ingresos2020 * 100 / ingresos2019) - 100

print(x)

separa()

def porcentajeX(x1, x2):
    if x1 == 0 and x2 == 0:
        print("{:,.2f}%".format(0))
    elif x1 == 0:
        print("{:,.2f}%".format(100))
    else:
        print("{:,.2f}%".format((x2 * 100 / x1) - 100))

porcentajeX(176520, 198765)

porcentajeX(116, 100)

porcentajeX(100, 116)

porcentajeX(4, 2)

porcentajeX(2, 4)

porcentajeX(500, 500)

porcentajeX(0, 0)

porcentajeX(100, 0)
porcentajeX(50, 0)

porcentajeX(0, 100)

porcentajeX(450, 789)