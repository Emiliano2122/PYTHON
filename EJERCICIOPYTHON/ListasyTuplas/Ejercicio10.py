prices = [50, 75, 46, 22, 80, 65, 90, 100]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price
print("El minimo es " + str(min))
print("El maximo es " + str(max))