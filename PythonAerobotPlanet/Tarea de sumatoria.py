#Sumatora

# 5 = 5+4+3+2+1

def sumatoria(n):
	if( n == 0):
		return 0
	else:
	    return n + sumatoria(n-1)

n = int(input("Ingresar n"))
if(n < 1):
    print("N no puede ser menor a 1")
else:
    print("La sumatoria  de 1 hasta ", n, " es", sumatoria(n))    	    	