def separa():
    print("")
    print("---------------")
    print("")

fruta = "guanabana"

for x in "banana":
    print(x)

separa()

for x in fruta:
    print(x)

separa()

espacios = ""

for x in fruta:
    print(espacios, x)
    espacios += " "

separa()

contador = 0
espacios = ""

for x in fruta:
    print(espacios,x)
    espacios += " "
    contador += 1

print("Son",contador,"caracteres.")

contador = 0

for x in fruta:
    print(x)
    contador += 1

print("La palabra", fruta, "son", contador, "caracteres")

separa()

vocales = "aeiou"

for x in vocales:
    print(x)
    
separa()

vocales = "aeiou"

for x in vocales:
    print(x)
    if x == "i":
        break
separa()

contador = 1
fruta = "guanabana"

for x in fruta:
    print(x)
    if x == "a":
        if contador == 2:
             break
        contador +=1

separa()

consonantes = "bcdfghjklmnñpqrstvwxyz"
contador = 1

for x in consonantes:
    print(contador,"-",x,"-")
    contador += 1

separa()
    
tabulador = ""
for x in vocales:
    print(tabulador, x)
    tabulador += "\t" #secuencia de escape de un tabulador
 
separa()

abcedario = "abcdefghijklmñopqrstuvwxyz"
tabulador = ""

for x in abcedario:
    print(tabulador, x)
    if x == "e":
       tabulador += "\t"
    if x == "i":
       tabulador += "\t"
    if x == "o":
       tabulador += "\t"
    if x == "u":
       tabulador += "\t"

separa()

tabulador = ""

for x in abcedario:
    print(tabulador, x)
    if x == "e" or x == "i" or x == "o" or x == "u":# se ejecuta cuando cualquiera de las condiciones es TRUE
        tabulador += "\t"

separa()

tabulador = ""
contador = 1

for x in abcedario:
    print(tabulador, x)
    if contador == 5:
        tabulador += "\t"
        contador = 0
    contador += 1

separa()

nombre = input("Dime tu nombre: ")
contador = 0
for x in nombre:
    print(x)
    contador += 1

print(contador, "caracteres es tu nombre")    

separa()

# Tarea

nombreCompleto = input("Dime tu nombre completo: ")
contador = 1
for x in nombreCompleto:
    print(x)
    if x == "a":
        if contador == 3:
            break
        contador += 1
    if x == "a":
        if contador == 3:
            break



        
        
        
      
        
            
            
            
            

            
separa()
    

     