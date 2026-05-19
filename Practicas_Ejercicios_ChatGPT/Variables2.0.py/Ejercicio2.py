# ==============================================================================
# MINIPROYECTO 2: CONTROL DE ENTRADA Y VALIDACIÓN EN EL PUNTO DE VENTA
# ==============================================================================

# 1. EVITAR ERRORES DE CONVERSIÓN (Manejo de Excepciones)
# Cuando el usuario ingresa un precio, si escribe letras por error, el sistema truena.
# Completa el bucle 'while True' con un bloque 'try...except ValueError' para pedir
# un número flotante. Si la conversión falla, muestra un mensaje de error y vuelve a pedirlo.
# Si es correcto, rompe el bucle con 'break'.

# 2. DESEMPAQUETADO AVANZADO CON OPERACIONES
# Tienes una lista con los datos de un cliente: cliente_datos = ["Said", "Burciaga", 18]
# Desempaqueta los datos en las variables: nombre, apellido, edad.
# Luego, usando un condicional 'if', verifica si 'edad' es mayor o igual a 18 para
# imprimir si es "Mayor de edad" o "Menor de edad".

# 3. COMPROBACIÓN DE DESCUENTOS ÚNICOS (Sets)
# Tienes dos conjuntos de cupones. Queremos saber qué cupones del 'conjunto_b'
# no están en el 'conjunto_a' (es decir, cupones completamente nuevos y diferentes).
# cupones_sistema = {"DESC10", "PROMO20", "BIENVENIDA"}
# cupones_nuevos = {"DESC10", "VIP50", "LIQUIDACION"}
# Usa la función '.isdisjoint()' o investiga la resta de conjuntos (-) para ver cuáles son únicos.
# Para este ejercicio, usa '.isdisjoint()' para verificar si 'cupones_nuevos' es completamente
# diferente a 'cupones_sistema' (debería dar False porque comparten "DESC10").

# ------------------------------------------------------------------------------
# EJERCICIO PARA TRABAJAR (Copia y completa):
# ------------------------------------------------------------------------------

# --- TAREA 1 ---
# while True:
#     try:
#         precio = float(input("Ingresa el precio del producto: "))
#         # (Tu código aquí...)
#     except ValueError:
#         # (Tu código de error aquí...)

# --- TAREA 2 ---
# cliente_datos = ["Said", "Burciaga", 18]
# # (Desempaqueta aquí...)
# # (Escribe el condicional 'if' aquí...)

cliente_datos = ["Said", "Burciaga", 18]
nombre, apellido, edad=cliente_datos
if edad>=18:
    print("Es mayor de edad")
else:
    print("Es mayor de edad")
    
print()

# --- TAREA 3 ---
# cupones_sistema = {"DESC10", "PROMO20", "BIENVENIDA"}
# cupones_nuevos = {"DESC10", "VIP50", "LIQUIDACION"}
# son_completamente_diferentes = 

cupones_sistema = {"DESC10", "PROMO20", "BIENVENIDA"}
cupones_nuevos = {"DESC10", "VIP50", "LIQUIDACION"}

verificacion_cupones=cupones_sistema.isdisjoint(cupones_nuevos)
print(verificacion_cupones)

# ------------------------------------------------------------------------------
# MOSTRAR RESULTADOS (Usa f-strings):
# ------------------------------------------------------------------------------
# print(f"Precio guardado con éxito: ${precio}")
# print(f"Cliente: {nombre} {apellido} - Estado: {estado_edad}")
print(f"Cliente: {nombre} {apellido} - edad: {edad}")   
# print(f"¿Los cupones nuevos son totalmente diferentes?: {son_completamente_diferentes}")
print(f"¿Los cupones nuevos son totalmente diferentes? {verificacion_cupones}")
# ==============================================================================