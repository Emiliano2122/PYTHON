def factorial(n):
	fact = 1
	while n > 1:
		fact = fact*n
		n = n +1
	return fact
n = int(input("ingresa el valor de n"))
if(n < 0):
    print("N no puede ser menor a 0")
else:
    print("factorial de ", n, "es ", factorial(n))    		