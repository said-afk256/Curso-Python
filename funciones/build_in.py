#10/06/2026

numeros=[4,7,1,42,15]

#Encontrando el número mas grande de la lista
#La función max() nos dara el número mas grande de un conjunto numerico
numero_mas_alto=max(numeros)
print(numero_mas_alto)

#Encontrando el número mas chico de la lista
#La función min() nos dara el número mas pequeño de un conjunto numerico
numero_mas_bajo=min(numeros)
print(numero_mas_bajo)

print()
#Redondeando las decimales de un número
numero= round(12.345678,2) #(numero, cantidad de decimales a mostrar)

print(numero)


#Función bool()
#retorna False si --->   0, vacio (como una lista vacia), False, None(ninguno)
#retorna True si --->    Distinto a 0, True, una cadena
resultado_bool_false=bool([])
resultado_bool_true=bool("Hola") #Los números negativos también da True, como -1
print(f"Función bool para una lista vacia: {resultado_bool_false}")
print(f"Función bool para una cadena de texto: {resultado_bool_true}")

#bool() comprueba un elemento

print()

#Función all()
#retorna true si todos los valores dentro de la función son verdaderos
resultado_all_true=all([12, "true", True, [123, 321]])#Pon una lista dentro de los corchetes para evitar errores
resultado_all_false=all([True, False, 0, [None, 0], []])#Aunque tenga True, lo demás es False
#Recordar poner dentro del parentesis del all sea una lista
print(resultado_all_true)
print(resultado_all_false)

#all() comprueba todos los elementos de una iterable
#Diferencia de bool() y all() de manera sencilla.
#bool es para un solo elemento, all es para una lista de elementos
print()

#Función sum()
#Suma todos los números o variables dentro del parentesis (no se si se puede mas de una variable a la vez, probablemete si)
suma=sum(numeros)

print(suma)



print()
print()
print()
print("Viendo las funciones de formato fstrings de :g y :.1f")
#:g funciona para que una variable numerica se muestre tal como es o de manera cientifica
#Se muestra de la ultima manera si el numero es extremadamente grande o chico
#Si se topa con número enteros como este: 1199249839222222222222222889, entonces mostrara esto:1.19925e+27
#Si es decimal, lo mas probable es que redonde de manera optima


#:.1f funciona para limitar la cantidad de decimales que se muestran
# el ".1" es la cantidad de decimales que quieres mostrar, puede ser cualquier número
# el "f" indica float, osea, python ya sabe que estas trabajando con números flotantes
#Pasa de esto 119.9249839222222222222222889 a esto: 119.9


# 1. Asigna el número a una variable (sin comillas)
numero_grande = 119.9249839222222222222222889

# 2. Aplica el formato :g dentro del f-string usando la variable
print(f"{numero_grande:g}")   