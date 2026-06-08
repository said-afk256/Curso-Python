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

#Doble iteración con zip
#Nota: Para esta función es importante que las listas tengan la misma cantidad de elementos, por que sino,
#El recorrido de la lista va a parar en la cantiadad que sea la maxima de la lista mas pequeña
#Ejemplo: lista1=5 elementos, lista 2= 3 elementos. EL resultado seria que la lista 2 sale completa pero la lista 5 solo llegaria hasta el tercer elemento
 
for numero, animal in zip(animales, numeros):
    
    print(f"Recorriendo lista 2: {animal}")
print()