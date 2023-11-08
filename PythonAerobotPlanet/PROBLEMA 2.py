#------------------Problema 2-----------------------------------------
"""Una empresa realiza encuestas a sus clientes para conocer su satisfacción e identificar puntos de oportunidad. Las preguntas que realizan son:

Pregunta 1: ¿Qué tanto te gustó el contenido de los talleres (electrónica/ programación)?
Pregunta 2: Evalúa a tus instructores de los talleres de electrónica/programación
Pregunta 3: ¿Qué tanto te gustaron los talleres recreativos y deportivos?
Pregunta 4: Evalúa a tus instructores de los talleres recreativos/deportivos
Pregunta 5: ¿Te volverías a inscribir al Electro Camp?

En donde las respuestas para las preguntas 1 a 4 son del 1 al 5 donde 1 es lo peor y 5 lo mejor.
Las respuestas para la quinta pregunta pueden ser: "Sí", "No" y "Tal vez".

Escribe un programa que despliegue un resumen de las encuestas aplicadas. Tu resumen deberá incluir:
1. Total de clientes que respondieron
2. Promedio de cada una de las preguntas 1 a 4

3. Conteo de cada una de las 3 respuestas categóricas de la pregunta 5

Puntos extra:
*Mostrar los promedios con 2 decimales.
"""

respuestas1 = [5, 5, 5, 5, 5, 5, 4, 5, 4, 4, 5, 5, 3, 5, 5, 4, 3, 4, 5, 5, 5, 4, 5, 5, 5, 4, 5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 5, 4, 5, 5, 5, 4]
respuestas2 = [5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 4, 4, 4, 5, 5, 1, 5]
respuestas3 = [4, 3, 2, 5, 5, 5, 3, 5, 4, 4, 5, 4, 5, 5, 4, 5, 4, 5, 5, 5, 5, 4, 5, 3, 5, 4, 4, 5, 4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5, 5, 5]
respuestas4 = [4, 5, 2, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
respuestas5 = ["Sí", "Sí", "Tal vez", "Sí", "Sí", "Tal vez", "Sí", "Sí", "Tal vez", "Sí", "Sí", "Sí", "No", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí", "Tal vez", "Sí", "Sí", "Sí", "Sí", "Sí", "Tal vez", "Tal vez", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí", "Tal vez", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí", "Tal vez"]

hola = len(respuestas1)
hola1 = sum(respuestas1)
hola2 = hola1/hola
 
print ("¿Qué tanto te gustó el contenido de los talleres (electrónica/ programación)?",(hola2))
stasi = len(respuestas2)
stasi1 = sum(respuestas2)
stasi2 = stasi1/stasi
 
print ("Evalúa a tus instructores de los talleres de electrónica/programación",(stasi2))
lama = len(respuestas3)
lama1 = sum(respuestas3)
lama2 = lama1/lama
 
print ("¿Qué tanto te gustaron los talleres recreativos y deportivos?",(lama2))
prida = len(respuestas4)
prida1 = sum(respuestas4)
prida2 = prida1/prida
 
print ("Evalúa a tus instructores de los talleres recreativos/deportivos",(prida2))
"""
ian = len(respuestas5)
ian1 = sum(respuestas5)
ian2 = ian1/ian
 
print ("¿Qué tanto te gustó el contenido de los talleres (electrónica/ programación)?",(ian2))
"""
calificaciones = (respuestas5.count("Sí"))
print("numero de calificaciones iguales si:" , calificaciones)
calificaciones_1 = (respuestas5.count("No"))
print("numero de calificaciones iguales no:" , calificaciones_1)
calificaciones = (respuestas5.count("Tal vez"))
print("numero de calificaciones iguales tal vez:" , calificaciones)
