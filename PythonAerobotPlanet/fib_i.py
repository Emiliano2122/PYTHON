def fib_i(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -=1
    return a
n = int(input("n"))
if(n < 1):
    print("N no puede ser menor a 1")
else:
    print("El", n, "º elemnto de la secuencia de Fibonacci es" , fib_i(n))    