# ==============================================================================
# EJERCICIO 5: Encontrar Extremos y Redondear (Funciones max(), min() y round())
# Tienes una lista con las calificaciones de un alumno, algunas con decimales.
# 1. Encuentra la calificación más alta usando max() y la más baja con min().
# 2. Usa round() para redondear la calificación final (8.57) a un solo decimal.
# ==============================================================================
print("Ejercicio 5:")
notas = [7.5, 9.2, 6.8, 8.57, 10]

# Escribe tu código aquí abajo:
nota_alta=max(notas)
nota_baja=min(notas)
promedio=(sum(notas))/(5)
nota_final=round(promedio)

print(f"Nota mas alta: {nota_alta}, nota mas baja: {nota_baja}, nota promedio: {promedio}, y nota final redondeada: {nota_final}")
print()

# ==============================================================================
# EJERCICIO 6: Sumatorias y conteos rápidos (Funciones sum() y len())
# Imagina que quieres calcular el promedio de una lista de gastos sin usar bucles.
# Usa sum() para obtener el total y len() para saber cuántos gastos hay.
# Divide el total entre la cantidad para obtener el promedio.
# ==============================================================================
print("Ejercicio 6:")
gastos_viaje = [200, 450, 120, 310, 80]

# Escribe tu código aquí abajo:
total_viaje=sum(gastos_viaje)
cantidad_gastos=len(gastos_viaje) 
promedio=total_viaje/cantidad_gastos

print(f"El total del viaje es de {total_viaje} pesos, con {cantidad_gastos} gastos, en promedio constando unos {promedio} pesos")
print()

# ==============================================================================
# EJERCICIO 7: El filtro de la verdad (Función bool())
# La función bool() evalúa si un dato es considerado verdadero (True) o vacío/falso (False).
# Prueba qué devuelve bool() al pasarle: una cadena vacía "", el número 0, y una lista con datos.
# ==============================================================================
print("Ejercicio 7:")
dato_vacio = ""
cero = 0
lista_llena = ["Python"]

# Escribe tus prints usando bool() aquí abajo:
print(bool(dato_vacio))
print(bool(cero))
print(bool(lista_llena))
print()