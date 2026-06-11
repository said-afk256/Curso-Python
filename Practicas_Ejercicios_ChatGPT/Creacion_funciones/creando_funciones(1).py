# ==============================================================================
#                      NUEVOS EJERCICIOS PARA PRACTICAR
# ==============================================================================

# ------------------------------------------------------------------------------
# TAREA 1: La Calculadora de Descuentos (Parámetros y Lógica)
# ------------------------------------------------------------------------------
# Instrucciones:
# Crea una función llamada: calcular_precio_final(precio_base, tipo_cliente)
#
# 1. Debe convertir el parámetro "tipo_cliente" a minúsculas usando ".lower()".
# 2. Usa condicionales (if, elif, else) para aplicar los siguientes descuentos:
#    - Si el cliente es "vip", el descuento es del 20%.
#    - Si el cliente es "miembro", el descuento es del 10%.
#    - Si es cualquier otra cosa (como "normal"), el descuento es del 0%.
# 3. La función debe calcular el precio final con el descuento aplicado.
# 4. Al final, la función debe IMPRIMIR (print) el desglose en la pantalla:
#    el precio original, el descuento aplicado y el total a pagar.
#
# Al terminar de crearla, pruébala llamando a la función un par de veces:
# calcular_precio_final(1000, "VIP")
# calcular_precio_final(500, "normal")

# Escribe el código de tu Tarea 1 aquí abajo:
def calcular_precio_final(precio_base, tipo_cliente):
    tipo_cliente=tipo_cliente.lower()
    descuento=0
    if tipo_cliente=="vip":
        descuento=20
    elif tipo_cliente=="miembro":
        descuento=10
    else:
        descuento=0
    precio_final=precio_base*(1-descuento/100)
    return f"Total del producto sin desc: {precio_base}, descuento: {descuento}%, Total a pagar: {precio_final}"

Pago_tienda=calcular_precio_final(100, "VIp")
print(Pago_tienda)



# ------------------------------------------------------------------------------
# TAREA 2: El Validador de Números Primos (Uso de "return" Booleano)
# ------------------------------------------------------------------------------
# Instrucciones:
# Crea una función llamada: es_primo(numero)
#
# 1. Un número primo es el que solo se divide de forma exacta entre 1 y sí mismo.
# 2. Pista: Puedes usar un bucle "for i in range(2, numero):" junto al operador
#    módulo (%) para verificar si el número es divisible por algún otro valor.
# 3. Si encuentras un número que lo divida exactamente, usa "return False"
#    inmediatamente (recuerda que el return corta la ejecución de la función).
# 4. Si el bucle termina por completo sin encontrar divisores, haz un "return True".
# 5. FUERA de la función, guarda el resultado en una variable (ej: resultado_primo).
# 6. Haz un condicional "if" que verifique esa variable e imprima un mensaje
#    personalizado indicando si el número es primo o no lo es.
#
# Escribe el código de tu Tarea 2 aquí abajo:




# ------------------------------------------------------------------------------
# TAREA 3: Estadísticas de una Lista (return Múltiple y Desempaquetado)
# ------------------------------------------------------------------------------
# Instrucciones:
# Crea una función llamada: analizar_numeros(lista_de_numeros)
#
# 1. Dentro de la función, calcula tres cosas usando funciones integradas:
#    - El número más grande utilizando la función max()
#    - El número más chico utilizando la función min()
#    - La suma total de los elementos utilizando la función sum()
# 2. Haz que la función retorne los tres valores calculados en un solo "return",
#    separándolos por comas (exactamente igual a tu función de contraseñas).
# 3. FUERA de la función, crea una lista de prueba. Ejemplo: notas = [15, 20, 12, 18, 9]
# 4. Llama a la función DESEMPAQUETANDO los tres valores en tres variables distintas:
#    mayor, menor, suma = analizar_numeros(notas)
# 5. Imprime de forma organizada los resultados en la terminal.
#
# Escribe el código de tu Tarea 3 aquí abajo:




# ==============================================================================
# RESULTADOS ESPERADOS EN TU CONSOLA AL EJECUTAR EL ARCHIVO:
# ==============================================================================
# Precio original: $1000, Cliente: vip
# Descuento aplicado: 20%
# Total a pagar: $800.0

# Precio original: $500, Cliente: normal
# Descuento aplicado: 0%
# Total a pagar: $500.0
# 
# ¿El número 7 es primo?: True
# ¡Genial! El número es un número primo.
# 
# Analizando la lista: [15, 20, 12, 18, 9]
# El número mayor es: 20
# El número menor es: 9
# La suma total es: 74
# ==============================================================================