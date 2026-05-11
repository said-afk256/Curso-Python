#Por mi 11/05/2026 Termine el código a las 12:47 pm

#Ejercicio 2: 
""" a)Pedirle al usuario que diga cualquier texto real y:
-Calcular cuanto tardaría en decir esa frase
-¿Cuántas palabras dijo?

b)Si se tarda más de 1 minuto:
-Decirle 'para flaco, tampoco te pedí un testamento

c)Dalto habla un 30% más rapido:
-¿Cuánto tardaría él en decirlo? 
Dato extra= 1seg=2 palabras"""

#Datos
#2 palabras=1 segundo
Texto=input("Ingrese un texto: ")
#Si preguntas que pasa con los int, los números pasan a ser strings por el input

list(Texto)#Texto a lista
palabras=Texto.split(" ")#Separar elementos por espacios
conteo_palabras=len(palabras)

segundo_palabra=1/2#Tiempo en decir una sola palabra (0.5 seg)
timpo_promedio_pronunciacion=conteo_palabras*segundo_palabra

#Demostración del ejercicio A
print()
print(f"Texto introducido: {Texto}")
print("-")
print(f"Te tardas en decir el texto unos {timpo_promedio_pronunciacion:.1f} seg")
print("-")
print(f"El total de palabras utilizadas son: {conteo_palabras}")
print()
print("------")

#Código para responder a textos que duren mas de 1 minuto en pronunciarse (ejercicio B)
print()
if conteo_palabras>=120:
    print("Para flaco, tampoco te pedi un testamento")
else:
    print("Buen escrito") #O se puede poner "("")" para que la respuesta este vacia

print("-------")
print()
#Calculo para saber cuanto tarda Dalto en decirlo si es un 30% más rapido
porcentaje_1seg=1-(1*(30/100)) #Lo que tarda Dalto decir 2 palabras (0.7 seg)

segundo_palabra_dalto=porcentaje_1seg/2

Dalto_tiempo_pronunciacion=conteo_palabras*segundo_palabra_dalto

#Demostración del ejercicio c
print(f"Dalto puede pronunciar tu texto en {Dalto_tiempo_pronunciacion} seg")