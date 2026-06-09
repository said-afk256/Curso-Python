#08/06/2026

#Recorriendo una lista
animales= ["perro", "gato", "loro", "cocodrilo"]

for animal in animales:
    print(f"El valor de animal cambio a {animal}")

print()

#Recorriendo lista de números y multiplicando cada número de la lista por 2
numeros=[10, 30, 90, 120, 150]

for numero in numeros:
    print(numero*2)
    #resultado= numero*2
    #print(resultado)
print()
 
#Iterando 2 listas del mismo tamaño al mismo tiempo
for numero, animal in zip(animales, numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")
print()
#Doble iteración con zip
#Nota: Para esta función es importante que las listas tengan la misma cantidad de elementos, por que sino,
#El recorrido de la lista va a parar en la cantiadad que sea la maxima de la lista mas pequeña
#Ejemplo: lista1=5 elementos, lista 2= 3 elementos. EL resultado seria que la lista 2 sale completa pero la lista 5 solo llegaria hasta el tercer elemento

#Forma no optima de recorrer una lista por su indice
print("Forma no optima de imprimir resultados con código:")
for num in range(len(numeros)):
    print(numeros[num])
print()
#Forma correcta de recorrer una lista por indice
print("Forma correcta de imprimir una lista por su indice")
for num in enumerate(numeros):#Estos números son considerados tuplas
    print(num)#Puedes hacer un print(type(num)) para ver que si son considerados tuplas
#El resultado tendra "(0,10)", el primer número es el indice y el segundo el valor que esta en ese indice
print()

#Manera mas visual de como funciona el enumerate
for num in enumerate(numeros):
    indice=num[0]#El "[0]" toma el indice 0 de la tupla, osea, el primer elemento, como el de "(0,10)"
    valor=num[1]#El "[1]" toma el elemento 2 de la tupla, por ejemplo, el segundo elemento de "(0,10)"
    print(f"El indice es {indice} y el valor es {valor}")
print()

#Desafio: Desempaquetar la tupla directamente en el for
for indice, num in enumerate(numeros):
    print(f"Desafio de desempaque: El indice es {indice} y su valor es {num}")
print()

#Usando el "for/else"
for num in numeros:
    print(f"Ejecutandose el bucle, número actual: {num}")
else:
    print("Se termino el bucle")
    #El else en un "for" siempre se ejecutara y solo aparece una vez, al menos que haya un "break" en el código
    #Esto es por que el else se ejecuta si ya se acaba el código del for, haciendo que practicamente se ejecute siempre una vez terminado el bucle

#Estos códigos también funcionan con tuplas aparte de las listas