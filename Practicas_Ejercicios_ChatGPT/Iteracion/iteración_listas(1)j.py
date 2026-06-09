#09/06/2026


# ==============================================================================
# EJERCICIO 1: Multiplicación condicional en listas
# Itera sobre la lista 'numeros'. Si el número es mayor a 50, multiplícalo por 10.
# Si es menor o igual a 50, multiplícalo por 2. Muestra los resultados.
# ==============================================================================

numeros = [10, 30, 90, 120, 150]

# Escribe tu bucle for aquí abajo:
for num in numeros:
    if num>50:
        print(f"El número {num} es mayor que 50, entonces si lo multiplicamos por 10 el resultado es: {num*10}")
    else:
        print(f"El número {num} es igual o menor que 50, entonces si lo multiplicamos por 2, el resultado sera: {num*2}")
print()


# ==============================================================================
# EJERCICIO 2: El dilema de zip() con tamaños diferentes
# Tienes dos listas de diferentes tamaños. Itera sobre ambas al mismo tiempo
# usando zip() y muestra un mensaje combinado. Observa dónde se detiene.
# ==============================================================================

colores = ["Rojo", "Azul", "Verde", "Amarillo"]
objetos = ["Carro", "Cuaderno", "Plátano"]

# Escribe tu bucle for aquí abajo:
for color, objeto in zip(colores, objetos):
    print(f"De lista colores: {color}")
    print(f"De lista objetos: {objeto}")
print("No aparece el color amarillo por que al usar zip con listas de diferente tamaño, se recorto un elemento de una para que saliera la misma cantidad de las 2 listas")
print()


# ==============================================================================
# EJERCICIO 3: Enumerate con Filtro de Índices (Desafío de Desempaque)
# Usa enumerate() y desempaqueta la tupla directamente en el 'for'.
# Imprime SOLO los elementos cuyo ÍNDICE sea un número PAR (0, 2, 4...).
# ==============================================================================

productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Audífonos"]

# Escribe tu bucle for aquí abajo:
for indice, producto in enumerate(productos):
    if indice % 2 == 0:
        print(f"Indice: {indice}, producto: {producto}")

print()


# ==============================================================================
# EJERCICIO 4: For / Else con interrupción (Break)
# Itera sobre la lista 'valores'. Si encuentras el número 0, imprime un mensaje 
# de alerta y usa 'break' para romper el bucle. Comprueba qué pasa con el 'else'.
# ==============================================================================

valores = [5, 8, 0, 12, 3]

# Escribe tu bucle for aquí abajo:
for valor in valores: 
    if valor == 0:
        print (f"Alerta: el bucle encontro el número {valor}")
        break
    print(valor) #Si pones print antes de if, este alcanzara a imprimir 0 ya que se ejecutara antes del if
    #por lo que se pone después del if, que estara verificando que el número no sea 0
else:
    print("El bucle no encontro un 0")
print()




# Para imprimir solo los elementos en índices pares (0, 2, 4...) usando enumerate,
# debes verificar si el índice es divisible por 2 utilizando el operador módulo (%).
#
# La condición correcta es: if indice % 2 == 0.
#
# productos = ["manzana", "banana", "cereza", "date", "figo"]
#
# for indice, producto in enumerate(productos):
#     # Verifica si el índice es par (0, 2, 4...)
#     if indice % 2 == 0:
#         print(f"Índice {indice}: {producto}")
#
# Salida:
# Índice 0: manzana
# Índice 2: cereza
# Índice 4: figo
#
# Si lo que necesitas es imprimir solo cuando el índice es impar (1, 3, 5...),
# cambia la condición a: if indice % 2 != 0.   


#Si queremos imprimir unicamente los números par, no pongas "else" al siguiente código:

# Escribe tu bucle for aquí abajo:
#for indice, producto in enumerate(productos):
#    if indice % 2 == 0:
#        print(f"Indice: {indice}, producto: {producto}")
#    else:
#         print(f"El indice {indice} es impar")
#print()

#Ya que el "else" se utiliza cuando tu quieres imprimir algo en caso de que no se cumpla el if
#si no quieres imprimir nada, es mejor quitar el "else" y dejar solo el "if"