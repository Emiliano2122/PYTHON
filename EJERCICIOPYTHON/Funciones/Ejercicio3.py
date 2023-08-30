def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp
print(factorial(4))
print(factorial(25))