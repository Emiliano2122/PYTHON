posicionOk = 0
while posicionOk > 9 or posicionOk < 1:
    posicion = input("Dime un numero entre [1 - 9]")
    if posicion == "*":
        break
    
    try:
        posicionOk = int((float(posicion)))
    except:
        posicionOk = 0
        print("")
        print("Se termina con asterisco")


print(posicionOk)
        