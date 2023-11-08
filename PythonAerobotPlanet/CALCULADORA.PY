option = "si"
operation = 9
x = 0
while (option == "si"):
	if (operatio == 0 or operation or operation == 0):
		print("***Calculadora***")
		print("1) Suma")
		print("2) Resta")
		print("3) Division")
		print("4) Multiplicacion")
		print("5) potencia")
		print("6) Raiz")
		operation = int(input("Eliga la operacion que desee "))
	if (operation == 1):
	    suma = []
	    x= int(input("cuantos números quieres que este programe sume? "))
	    y= 1

	    while(x != 0):
	    	print(("cual sera el"), end = " ")
	    	print((y), end = " ");
	    	print(("numero que"), end = " ")
	    	num = int(input("quieres que este programa sume? "))
	    	sumas.append(num)
	    	y+=1
	    	x-=1
	    suma(sumas)
	    print(sum(sumas))
	    option = input("Queres continuar realiznado operaciones en este programa? ")
	    if( option == "si"):
                operation = 8
if (operation == 2):
        
        r = []
        numbers = int(input("Cuantos numeros quieres restar? ")-1)
        y = 2
        k = int(input("cual es el primero número que quieres que este programa reste? ")) 
        while (numbers > 0):
                print(("cual será el"), end = " ")
	            print((y), end = " ");
	            print(("número que"), end = " ")
	            n = int(input("quieres que este prorama reste? "))
	            r.append(n)
	            y+=1 
		        numbers -=1
	    print(("el resultado es: "), end = " ")
	    print(k-sum(r))
	    option = input("Quieres continuar realizando operaciones en este programa? ")
	    if( option == "si"):
		    operation = 8
if(operation == 4): 

	    x = int(input("cuantos números quieres que este programa multiplique? ")-1)
		y = 2
		k = int(input("cual es el primer número que quieres que este programa multiplique? "))
		
		while(x != 0):
			
			print(("cual será el"), end = " ")
			print((y), end = " ")
			print(("número que"), end = " ")
			num = int(input("quieres que este programa multiplique? "))
			k*=num
			y+=1
			x-=1
		print(k)
		option = input("Quieres continuar realizando operaciones en este programa? ")
		if( option == "si"):
			operation = 8
	if(operation == 3):
		x = int(input("cuantos números quieres que este programa divida? ")-1)
		y = 2
		k = int(input("cual es el primer número que quieres que este programa divida? "))
		
		while(x != 0):
			
			print(("cual será el"), end = " ")
			print((y), end = " ")
			print(("número que"), end = " ")
			num = int(input("quieres que este programa divida? "))
			k/=num
			y+=1
			x-=1
		print(k)
		option = input("Quieres continuar realizando operaciones en este programa? ")
		if( option == "si"):
			operation = 8
	if(operation == 5):
		def potencia(num1, num2):
			return pow(num1, num2)
		num1 = int(input("ingresa el número base: "))
		num2 = int(input("ingresa la potencia de tu numero base: "))
		print(potencia(num1, num2))
		option = input("Quieres continuar realizando operaciones en este programa? ")
		if( option == "si"):
			operation = 8
	if(operation == 6):
		def raiz(num1, num2):
			aux = 1/num2
			result = num1**aux
			return resultado
		num1 = int(input("Ingresa el número base: "))
		num2 = int(input("Ingresa la potencia de la raíz"))
		print("el reultado es ", raiz(a, b))
		option = input("Quieres continuar realizando operaciones en este programa? ")
		if( option == "si"):
			operation = 8
