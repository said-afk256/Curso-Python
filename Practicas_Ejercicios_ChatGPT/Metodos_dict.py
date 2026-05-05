# ==============================================================================
# RETOS DE MÉTODOS DE DICCIONARIOS
# ==============================================================================
# INSTRUCCIONES:
# Usa el diccionario 'equipo' para resolver los siguientes puntos.
# ==============================================================================

equipo = {
    "id": 101,
    "tipo": "PLC",
    "marca": "Siemens",
    "estado": "Activo"
}

# --- SECCIÓN 1: EXTRACCIÓN Y SEGURIDAD ---

# Ejercicio 1:
# Intenta obtener el valor de la llave "ubicacion" usando .get(). 
# Si no existe, que el programa te devuelva el texto "No asignada".
ubicacion=equipo.get("ubicacion", "No asignada")
print(f"Ejercicio 1: {ubicacion}")
print()

# Ejercicio 2:
# Imprime únicamente las llaves (keys) del diccionario 'equipo'.
keys_equipo=equipo.keys()
print(f"Ejercicio 2: {keys_equipo}")
print()

# --- SECCIÓN 2: ELIMINACIÓN ---

# Ejercicio 3:
# 1. Usa .pop() para eliminar la llave "id".
# 2. Intenta usar .pop() con una llave que NO existe llamada "serie" 
#    y guarda el mensaje de error "Llave no encontrada" en una variable. 
#    Luego imprime esa variable.
equipo.pop("id")
resultado=equipo.pop("serie", "Llave no encontrada")
print(f"Ejercicio 3: {equipo} y mensaje del pop: {resultado}")
print()

# --- SECCIÓN 3: ITERACIÓN ---

# Ejercicio 4:
# Usa el método .items() para mostrar todos los pares llave-valor del equipo. 
# ¿Qué tipo de estructura te devuelve Python (una lista, una tupla, etc.)?
items=equipo.items()
print(f"Ejercicio 4: {items}")
print(f"Tipo de dato: {type(items)}")
print()

# --- DESAFÍO INTEGRADO ---

# Ejercicio 5:
# 1. Agrega una nueva llave al diccionario: equipo["voltaje"] = 24
# 2. Verifica si "voltaje" es una de las llaves usando "in" (ejemplo: "voltaje" in equipo.keys())
# 3. Al final, limpia todo el diccionario.
equipo.update({"voltaje":24})
print("voltaje" in equipo)#Tambien funciona "voltaje" in equipo.keys()
#Recordar que el in se usa para comprobar si algo esta dentro de una variable o matriz
#El not in es para lo contrario
equipo.clear()
print(f"Resultado final del ejercicio 5: {equipo}")



# ==============================================================================
# RESPUESTAS PARA COMPROBAR
# ==============================================================================
# 1. resultado = equipo.get("ubicacion", "No asignada") -> "No asignada"
# 2. print(equipo.keys())
# 3. msg = equipo.pop("serie", "Llave no encontrada") | print(msg) -> "Llave no encontrada"
# 4. Devuelve un dict_items (que parece una lista de tuplas).
# 5. equipo.clear() -> el resultado final debe ser {}