frutas = {'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input("Que fruta necesitas").title()
kg = float(input("Cuantos kilos "))
if fruta in frutas:
    print(kg, "kilos de", fruta, "valen", frutas[fruta]*kg, "$")
else:
    print("Lo sentimos, la fruta", fruta, "no la teneos disponble")