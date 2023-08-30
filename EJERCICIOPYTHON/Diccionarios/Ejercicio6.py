persona = {}
continuar = True
while continuar:
    clave = input("Qque dato quieres poner")
    valor = input(clave + "")
    persona[clave] = valor
    print(persona)
    continuar = input("Que quieres añadir mas informacion (Si/No)? ") == "Si"