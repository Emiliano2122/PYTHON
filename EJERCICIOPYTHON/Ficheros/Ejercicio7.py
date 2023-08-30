import csv

def leer_cotizaciones(ruta):
    try:
        with open(ruta, 'r', newline='') as archivo_csv:
            lector = csv.DictReader(archivo_csv, delimiter=';')
            columnas = next(lector)
            cotizaciones = {columna: [] for columna in columnas}
            for fila in lector:
                for columna, valor in fila.items():
                    cotizaciones[columna].append(limpiar(valor))
    except FileNotFoundError:
        print('El fichero no existe')
        return
    return cotizaciones

def limpiar(cifra):
    try:
        cifra = cifra.replace('.', '')
        cifra = cifra.replace(',', '.')
        return float(cifra)
    except ValueError:
        return 0.0

cotizaciones_dict = leer_cotizaciones('cotizacion.csv')
print(cotizaciones_dict)