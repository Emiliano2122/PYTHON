import random

def generar_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, lugar_nacimiento):
    homoclave = str(random.randint(10,99))

    primera_letra = apellido_paterno[:2].upper() + apellido_materno[:1].upper() + nombre[:1].upper()
    
    anio_nacimiento = str(fecha_nacimiento.year)[-2:]

    mes_nacimiento = str(fecha_nacimiento.month).zfill(2)
    dia_nacimiento = str(fecha_nacimiento.day).zfill(2)

    genero = genero[0].upper()

    consonantes_lugar = [c for c in lugar_nacimiento[1:] if c not in "AEIOU"]
    primera_consonante_lugar = consonantes_lugar[0].upper() if consonantes_lugar else "X"