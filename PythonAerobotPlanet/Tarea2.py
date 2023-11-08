#---------------------Tarea 2-----------------------------------------
"""Medical application program: A medical study about breast cancer has collected data for the diagnosis of malign or benign cancer at early stages.
Code a program that asks the following data:
Area: decimal value of the area of the cell mass.
Concavity: decimal value of the concavity of the cell mass.
Smoothness: categorical value of the smoothness of the cell mass. Three possible values; Soft, Moderate, Hard.
...And determines whether the cell mass is benign or malign.

The provided tree diagram shows the values of the variables that determine the path to follow for the diagnosis. Use such diagram for your program."""
usuario="Emiliano19"
passw="153429"
cont=0
while cont<3:
    us=input("Bienvenido por favor ingrese usuario");
    co=input("ingrese contreaseña");
    if us==usuario or passw==co:
        print ("Bienvenido  ")
        conectado=True
        break
    else:
        cont=cont+1;
        print ("Usuario y contraseña incorreta")
        conectado=False

while conectado==True:
    print ("cual es la magnitud?:")
    print ("1._Menor que 880")
    print ("2._Mayor que 880")
    choi=int(input("Es Menor o Mayor?:"))
    if choi==1:
        print ("que concavidad tiene")
        print ("1._Menor que 0.14")
        print ("2._Mayor que 0.14")
        hola=int(input("Es Menor o Mayor?:"))
        if hola==1:
            print ("Tu celulas son benignas :)")
            print ("hasta luego que cures jeje")
            break
        elif hola==2:
              print ("que tan duro esta la zona ?")
              print ("1.- suave")
              print ("2.- moderado")
              print ("3.- duro")
              hola=int(input("Es Menor o Mayor?:"))
              if hola==1:
                  print ("Tu celulas son benignas :)")
              elif hola==2:
                  print ("Tu celulas son benignas :)")
              elif hola==3:
                  print ("Tu celulas son malignas :(")
                  break
        
    elif choi==2:
        print ("que concavidad tiene")
        print ("1._Menor que 0.716")
        print ("2._Mayor que 0.716")
        negro=int(input("Es Menor o Mayor?"))
        if negro==1:
            print ("que tan duro esta la zona ?")
            print ("1.- suave")
            print ("2.- moderado")
            print ("3.- duro")
            negro=int(input("Es Menor o Mayor?:"))
            if negro==1:
                  print ("Tu celulas son benignas :)")
            elif negro==2:
                  print ("Tu celulas son malignas :(")
            elif negro==3:
                  print ("Tu celulas son malignas :(")
                  break
        elif negro==2:
            print ("Tu celulas son malignas :(")
            break
