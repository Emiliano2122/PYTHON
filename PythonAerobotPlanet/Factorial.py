def factorial(n):
	if(n == 0):
		return 1
	else:
	    return n * factorial (n-1)
n = int(input("ingrese el valor de n"))
if (n >= 0):
	print("factorial de ", n , "es" , factorial(n))
else:
    print("n no puede ser menor que 0")	


