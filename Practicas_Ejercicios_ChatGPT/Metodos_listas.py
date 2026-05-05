# ==============================================================================
# RETOS DE MÉTODOS DE LISTAS (LISTS)
# ==============================================================================
# INSTRUCCIONES:
# Resuelve cada reto aplicando los métodos: insert, append, extend, pop, etc.
# ¡No olvides los paréntesis () al llamar a los métodos!
# ==============================================================================

# --- SECCIÓN 1: AGREGAR Y POSICIONAR ---

# Ejercicio 1:
# Tienes la lista: componentes = ["PLC", "HMI", "Sensor"].
# 1. Agrega "Motor" al final de la lista.
# 2. Inserta "Actuador" justo en la posición 1 (que quede después de PLC).
componentes = ["PLC", "HMI", "Sensor"]
componentes.append("Motor")
componentes.insert(1,"Actuador")
print(f"Ejercicio 1: {componentes}")

# Ejercicio 2:
# Tienes: herramientas = ["Pinzas", "Multímetro"].
# Usa el método .extend() para agregar dos más: "Cautín" y "Soldadura" en un solo paso.
herramientas = ["Pinzas", "Multímetro"]
herramientas.extend(["Cautin", "Soldadura"])
print(f"Ejercicio 2: {herramientas}")

# --- SECCIÓN 2: ELIMINAR Y LIMPIAR ---

# Ejercicio 3:
# De la lista: tareas = ["Limpiar", "Programar", "Probar", "Entregar"].
# 1. Usa .pop() para eliminar y guardar en una variable el ÚLTIMO elemento.
# 2. Usa .remove() para quitar "Limpiar" específicamente.
tareas = ["Limpiar", "Programar", "Probar", "Entregar"]
tareas.pop(-1)
tareas.remove("Limpiar")
print(f"Ejercicio 3: {tareas}")

# Ejercicio 4:
# Crea una lista con 3 números cualesquiera y luego bórralos todos 
# usando el método que deja la lista vacía [].
numeros=[ 1234, 3453, 7654]
numeros.clear()
print(f"Ejercicio 4: {numeros}")

# --- SECCIÓN 3: ORDEN Y LÓGICA ---

# Ejercicio 5:
# Tienes: valores = [50, 10, 100, 5, 25].
# 1. Ordénalos de MENOR a MAYOR.
# 2. Ahora, usa el parámetro reverse=True dentro de sort para invertirlos (MAYOR a MENOR).
valores=[50,10,100,5,25]
valores.sort()
print(f"Ejercicio 5: Lista ordenada de manera ascendente: {valores}")
valores.sort(reverse=True)
print(f"Ahora de manera descendente: {valores}")

# Ejercicio 6:
# Tienes: nombres = ["Said", "Ana", "Zuly"].
# Aplica el método .reverse() (OJO: no sort) y explica qué pasó con el orden.
nombres = ["Said", "Ana", "Zuly"]
nombres.reverse()
print(f"Ejercicio 6: {nombres} Lo que pasa con el reverse es que invierte el orden de los elementos dentro de la lista")
# --- SECCIÓN 4: BÚSQUEDA Y VERIFICACIÓN ---

# Ejercicio 7:
# En la lista: stock = [10,
# 20, 30, 40, 50].
# Usa .index() para encontrar en qué posición está el número 40.
stock=[10,20,30,40,50]
posicion_num_40=stock.index(40)
print(f"Ejercicio 7: Posición del número 40 en la lista 'stock': {posicion_num_40}")

# --- EL DESAFÍO INTEGRADO ---

# Ejercicio 8:
# 1. Crea una lista vacía llamada 'mi_botin'.
# 2. Agrega "Oro" con append.
# 3. Agrega ["Plata", "Bronce"] con extend.
# 4. Quita el elemento de la posición 1.
# 5. Imprime el largo (len) de la lista final.
mi_botin=[]
mi_botin.append("Oro")
mi_botin.extend(["Plata", "Bronce"])
mi_botin.pop(1)
print(f"Ejercicio 8: {len(mi_botin)}")

# ==============================================================================
# RESPUESTAS PARA COMPROBAR (¡Cuidado con los índices!)
# ==============================================================================
# 1. ['PLC', 'Actuador', 'HMI', 'Sensor', 'Motor']
# 2. ['Pinzas', 'Multímetro', 'Cautín', 'Soldadura']
# 3. tarea_final = "Entregar" | lista queda: ["Programar", "Probar"]
# 4. .clear() -> resultado: []
# 5. 1ro: [5, 10, 25, 50, 100] | 2do: [100, 50, 25, 10, 5]
# 6. ["Zuly", "Ana", "Said"] (Solo voltea la lista, no alfabetiza)
# 7. Resultado: 3
# 8. Largo final: 2 (Quedaría ["Oro", "Bronce"])