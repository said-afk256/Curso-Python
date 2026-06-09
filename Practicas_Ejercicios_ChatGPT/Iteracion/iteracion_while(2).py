# ==============================================================================
# EJERCICIO 1: Saltando distractores con "continue"
# Tienes una lista de actividades. Itera sobre ellas con un bucle 'for' e imprímelas.
# Si la actividad es "Revisar redes sociales", usa 'continue' para saltártela y 
# no mostrarla en pantalla.
# ==============================================================================

actividades = ["Estudiar Python", "Hacer ejercicio", "Revisar redes sociales", "Leer un libro"]

# Escribe tu bucle for aquí abajo:
print("Ejercicio 1:")
for actividad in actividades:
    if actividad=="Revisar redes sociales":
        continue
    print(actividad)
print()


# ==============================================================================
# EJERCICIO 2: Detector de fallas con "break" e "else"
# Tienes una lista de temperaturas de un motor. Itera sobre ellas.
# Si la temperatura supera los 80 grados, imprime una alerta, usa 'break' para
# apagar el sistema y evitar que el 'else' se ejecute. Si todas las temperaturas 
# son seguras, el 'else' debe imprimir: "Sistema estable".
# ==============================================================================
print("Ejercicio 2:")
temperaturas = [45, 52, 85, 60, 30]

# Escribe tu bucle for aquí abajo:
for grado in temperaturas:
    if grado>80:
        print(f"Alerta de temperatura, {grado} °C supero los 80 °C")
        break
    print(f"{grado} °C")
else:
    print("Sistema estable")
print()


# ==============================================================================
# EJERCICIO 3: El "for" en una sola línea (List Comprehension)
# Tienes una lista con los precios de varios productos en dólares. 
# Crea una nueva lista llamada 'precios_pesos' que convierta cada precio multiplicándolo 
# por 20, usando la sintaxis de una sola línea que aprendiste.
# ==============================================================================
print("Ejercicio 3:")
precios_dolares = [5, 12, 25, 100]

# Escribe tu variable con el for en una sola línea aquí abajo:
precios_pesos = [dolares*20 for dolares in precios_dolares]


print(f"Precios en pesos: {precios_pesos}")
print()

# ==============================================================================
# EJERCICIO 4: Controlando el "while"
# Usando un bucle 'while', crea un programa que simule la descarga de un archivo.
# El porcentaje debe empezar en 0 e ir sumando de 25 en 25 en cada vuelta.
# El bucle debe detenerse cuando llegue a 100.
# ==============================================================================
print("Ejercicio 4:")
porcentaje = 0

# Escribe tu bucle while aquí abajo:
while porcentaje<100:
    porcentaje+=25
    print(porcentaje)
    
#Al ultimo el print por que en esta caso queremos que el porcentaje llegue a 100
#Si quisieramos que parara justo antes del 100, por ejemplo, en 75
#Ahi si podriamos primero print y luego la suma

#vuelta 1: 25 vuelta 2: 50 vuelta 3: 75 vuelta 4:100
#Si en la vuelta 4 da 100, para el programa, pero si lo pones antes de terminar el bloque, alcanza otra vuelta
# --- ANÁLISIS DEL ORDEN DE OPERACIONES EN EL BUCLE WHILE ---

# 1. ORDEN ACTUAL (Suma → Print):
#    - El bucle suma 25 primero y luego imprime el valor.
#    - Cuando 'porcentaje' llega a 100, se imprime inmediatamente.
#    - Recién en la siguiente iteración, la condición 'while porcentaje < 100' 
#      evalúa 100 <    