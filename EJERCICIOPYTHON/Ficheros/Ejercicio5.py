def pib_pais(url, pais = "ES"):
    '''
    Función que muestra por pantalla el pib per cápita un país dado de los años disponibles en un fichero dado.
    Parámetros:
        url: Es una cadena con la url del fichero de texto que contiene el pib per cápita.
        pais: Es una cadena con el código del país. 
    Devuelve:
        Un diccionario con pares año:pib del país dado que hay en el fichero con la url dada.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(url) as f:
            datos = f.read().decode('utf-8').split('\n') # Leer los datos y guardar cada línea en una lista
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        datos = [i.split('\t') for i in datos] # Dividir cada línea por el tabulador
        datos = [list(map(str.strip, i)) for i in datos] # Eliminar espacios en blanco
        for i in datos:
            i[0] = i[0][-2:] # Obtener el código del país de los dos últimos caracteres del primer elemento de la lista
        datos[0][0] = 'años'
        # Creamos un diccionario con claves los códiogos de los países y valores la lista de sus pibs (a excepción del primer par que contiene los años).
        datos = {i[0]:i[1:] for i in datos}
        # Creamos y devolvemos el diccionario con los pibs del país
        return {datos['años'][i]:datos[pais][i] for i in range(len(datos['años']))}

pais = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', pais)
print("Año\tPIB")
for i, j in pib_pais("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true", pais).items():
    print(i, '\t', j)