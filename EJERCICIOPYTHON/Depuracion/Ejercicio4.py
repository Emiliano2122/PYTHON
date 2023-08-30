listin = {'Juan': 123456789, 'Pedro' : 987654321}

def elimina(listin, usuario):
    return listin.pop(usuario, '')

print(elimina(listin, 'Pablo'))