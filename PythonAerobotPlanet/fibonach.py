def fibonacci(n):
	if(n == 1 or n == 2):
		return 1
	else:
	    return fibonacci(n-1) + fibonacci(n-2)
n = int(input("ingrese el valor de n"))
if(n < 1):
    print("n no puede ser menor a 1")
else:
    print("El fibonachi de ", n , "es ", fibonacci(n))    	    

