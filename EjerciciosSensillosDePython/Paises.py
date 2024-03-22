# Crear una lista con los nombres de 5 países. pedirle al usuario que ingrese dos países y que se guarde todo en un archivo
# El reto debe tener la opción de borrar Un pais

paises = ["Panama", "Argentina", "Chile", "España", "Francia"]
paises.sort()
print("Estos son los paises dados de alta")
print(paises)
print("Ingresa dos nuevos paises: ")
primerpais = input("Escribe el nombre del primer pais:")
segundopais = input("Escribe el nombre del segundo pais:")
paises.append(primerpais)
paises.append(segundopais)
paises.sort()
print(paises)
print("Estos son los paises cual quieres borrar")
primerpais = input("Escribe el pais:")
paises.remove(primerpais)
#paises.remove(segundopais)
print(paises)