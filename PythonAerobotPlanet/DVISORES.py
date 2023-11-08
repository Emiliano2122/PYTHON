def main():
	print("DIVISORES")
	numero = int(input("Escribir un numero entero mayo que cero"))

	if numero <= 0:
		print("¡Le he pedido un nuemro entero mayor que cero!")
	else:
	    print(f"Los divisore de {numero} son ", end="")
	    for i in range(1, numero // 2+1):
	        if numero % i == 0:
	            print(i, end=" ")
	    print(f"{numero}")
        
