def contar_palabras(url):
    from urllib import request
    from urllib.error import URLError
    try:
        f = request.urlopen(url)
    except URLError:
        return("!La url" + url + "no existe!")
    else:
        contenido = f.read()
        return len(contenido.split())