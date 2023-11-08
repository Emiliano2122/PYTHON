"""Actividad de repaso: programa del juego de ahorcado; se debe poner la palabra en la variable adivinar y la variable muestra debe tener tantos _ como letras tiene
la palabra"""

palabra = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'a', 'r']
muestra = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
print(muestra)
faltantes = len(palabra)
intentos = 5

while(faltantes > 0 and intentos > 0):
    correcto = 0    
    letra = input("Intenta adivinar una letra ")
    if(letra in muestra):
        print("Ya dijiste esa letra, intenta con otra")
    else:
        if(letra in palabra):
            for i in range(0, len(palabra)):
                if(palabra[i] == letra):
                    muestra[i] = letra
                    faltantes -= 1
        else:
            intentos -= 1
            print("Esa letra no está en la palabra. Te quedan", intentos, "intentos.")
        print(muestra)

if(faltantes == 0):
    print("¡Lo lograste! Y te sobraron", intentos, "intentos.")
else:
    print("Mejor suerte para la próxima. La palabra era: ", palabra)
    
