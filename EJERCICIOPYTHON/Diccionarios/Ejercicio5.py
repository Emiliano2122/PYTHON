curso = {"Matematicas": 6, "Fisica": 4, "Qimica": 5}
total_creditos = 0
for asignatura, creditos in curso.items():
    print(asignatura, "tiene", creditos, "creditos")
    total_creditos += creditos
print("Numeros de creditos de este curso: ", total_creditos)