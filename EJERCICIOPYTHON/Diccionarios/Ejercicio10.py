clientes = {}
opcion = ""
while opcion != "6":
    if opcion == "1":
        nif = input("Introdusca el NIF del cliente: ")
        nombre = input("Introdusca el nombre del cliente: ")
        direccion = input("Introdusca la direccion el cliente: ")
        telefono = input("Introdusca el numeo de telefono del cliente: ")
        email = input("Introdusca el correo electronico del cliente: ")
        vip = input("Es un cliente preferente (S/N)")
        cliente = {"nombre": nombre, "direccion": direccion, "telefono": telefono, "email": email, "preferente":vip=="S"}
        clientes[nif] = cliente
    if opcion == "2":
        nif = input("Introdusca el NIF  del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("No existe el cliente con el nif", nif)
    if opcion == "3":
        nif = input("Introdusca el NIF del cliente: ")
        if nif in clientes:
            print("NIF:", nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ":", valor)
            else:
                print("No existe el cliente con el nif", nif)
    if opcion == "4":
        print("Lista clientes")
        for clave, valor in clientes.items():
            print(clave, valor["nombre"])
    if opcion == "5":
        print("Lista de clientes preferentes")
        for clave, valor in clientes.items():
            if valor["preferentes"]:
                print(clave, valor["nombre"])
    opcion = input("Menu de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Lista cliente\n(5) Lista clientes preferentes\n(6) Terminar\nElige una opcion")