import pandas as pd
import os
from datetime import datetime

class Proyecto:
    def __init__(self, nombre, descripcion, inicio, finalizacion, estado, responsable, prioridad, comentarios):
        self.nombre = nombre
        self.descripcion = descripcion
        self.inicio = inicio
        self.finalizacion = finalizacion
        self.estado = estado
        self.responsable = responsable
        self.prioridad = prioridad
        self.comentarios = comentarios

proyectos = []

# Cargar proyectos desde el archivo CSV si existe
if os.path.exists("proyectos.csv"):
    proyectos_df = pd.read_csv("proyectos.csv")
    for _, row in proyectos_df.iterrows():
        proyectos.append(Proyecto(*row))

def agregar_proyecto():
    nombre = input("Nombre del proyecto: ")
    descripcion = input("Descripción: ")
    inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    finalizacion = input("Fecha de finalización (YYYY-MM-DD): ")
    estado = input("Estado: ")
    responsable = input("Responsable: ")
    prioridad = input("Prioridad: ")
    comentarios = input("Comentarios: ")

    proyecto_nuevo = Proyecto(nombre, descripcion, inicio, finalizacion, estado, responsable, prioridad, comentarios)
    proyectos.append(proyecto_nuevo)
    
    proyectos_data = []
    for proyecto in proyectos:
        proyectos_data.append(vars(proyecto))
    
    proyectos_df = pd.DataFrame(proyectos_data)
    proyectos_df.to_csv("proyectos.csv", index=False)
    print("Proyecto agregado y guardado.")

def mostrar_proyectos():
    for idx, proyecto in enumerate(proyectos, start=1):
        print(f"\nProyecto #{idx}")
        print(f"Nombre: {proyecto.nombre}")
        print(f"Descripción: {proyecto.descripcion}")
        print(f"Fecha de inicio: {proyecto.inicio}")
        print(f"Fecha de finalización: {proyecto.finalizacion}")
        print(f"Estado: {proyecto.estado}")
        print(f"Responsable: {proyecto.responsable}")
        print(f"Prioridad: {proyecto.prioridad}")
        print(f"Comentarios: {proyecto.comentarios}")

while True:
    print("\n*** Agenda de Proyectos ***")
    print("1. Agregar Proyecto")
    print("2. Mostrar Proyectos")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_proyecto()
    elif opcion == "2":
        mostrar_proyectos()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente nuevamente.")