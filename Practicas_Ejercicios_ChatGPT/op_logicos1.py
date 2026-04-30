# ==============================================================================
# EJERCICIOS DE OPERADORES LÓGICOS EN PYTHON
# ==============================================================================
# INSTRUCCIONES:
# 1. Lee cada expresión y trata de predecir si el resultado será True o False.
# 2. Escribe el código en tu editor y asígnale el resultado a una variable.
# 3. Usa print() para ver el resultado real.
#
# CONSEJOS PARA PROGRAMADORES:
# - Recuerda la precedencia: NOT se evalúa primero, luego AND, y al final OR.
# - Los paréntesis () tienen el poder total: lo que esté dentro se evalúa primero.
# - En Python, True equivale a 1 y False a 0 para operaciones matemáticas.
# - El operador "==" (comparación) se evalúa ANTES que los operadores lógicos.
# ==============================================================================

# Ejercicio 1: ¿Qué resulta de esta combinación básica?
ejercicio_1 = (True and False) or True #False or true
#R= True
print(ejercicio_1)

# Ejercicio 2: El efecto del NOT.
ejercicio_2 = not (True and False) #not (False)= True
#R=True
print(ejercicio_2)

# Ejercicio 3: Comparaciones numéricas con AND.
ejercicio_3 = (10 > 5) and (3 < 1)#(True) and (False)=False
#R=False
print(ejercicio_3)

# Ejercicio 4: Uso del OR con comparaciones.
ejercicio_4 = (7 <= 7) or (5 > 10)#(True)or(False)=True
#R=True
print(ejercicio_4)

# Ejercicio 5: Combinando varios operadores (Cuidado con el orden).
ejercicio_5 = True or False and False#True or  (false and false) = true or false
#R=False
print(ejercicio_5)

# Ejercicio 6: Paréntesis cambiando la prioridad del ejercicio anterior.
ejercicio_6 = (True or False) and False#True and False=False
#R=False
print(ejercicio_6)

# Ejercicio 7: Operaciones mixtas.
ejercicio_7 = not True or (10 != 10)#not true or (False)= false or false= false
#R=False
print(ejercicio_7)

# Ejercicio 8: ¿Qué pasa cuando comparamos el mismo valor con NOT?
ejercicio_8 = not (5 == 5) and (100 > 99)#not(true) and (True)= false and true=False
#R=False
print(ejercicio_8)

# Ejercicio 9: Lógica anidada.
ejercicio_9 = (True and (not False)) or (False and True)#(true and (true) or (false))=(true and true)=true
#R=True
print(ejercicio_9)

# Ejercicio 10: El "intruso". ¿Qué pasa si comparamos números directamente?
# (Recuerda que cualquier número distinto de 0 se considera True)
ejercicio_10 = (5 > 3) and (not 0)#(true)and(not false)= true and true= True
#R=True
print(ejercicio_10)

# ==============================================================================
# ESPACIO PARA TUS PRINTS (Usa el multicursor para escribirlos rápido):
# ==============================================================================

# print(f"Resultado 1: {ejercicio_1}")
# ... escribe los demás aquí ...
print()
print()
print()

print(f"Resultado del ejercicio:1 {ejercicio_1}")
print(f"Resultado del ejercicio:2 {ejercicio_2}")
print(f"Resultado del ejercicio:3 {ejercicio_3}")
print(f"Resultado del ejercicio:4 {ejercicio_4}")
print(f"Resultado del ejercicio:5 {ejercicio_5}")
print(f"Resultado del ejercicio:6 {ejercicio_6}")
print(f"Resultado del ejercicio:7 {ejercicio_7}")
print(f"Resultado del ejercicio:8 {ejercicio_8}")
print(f"Resultado del ejercicio:9 {ejercicio_9}")
print(f"Resultado del ejercicio:10 {ejercicio_10}")

#10/10 Todo Correcto
# ==============================================================================
# RESPUESTAS (Míralas solo después de terminar)
# ==============================================================================
# 1. True  (False or True = True)
# 2. True  (not False = True)
# 3. False (True and False = False)
# 4. True  (True or False = True)
# 5. True  (True or (False and False) -> True or False = True)
# 6. False ((True) and False = False)
# 7. False (False or False = False)
# 8. False (False and True = False)
# 9. True  (True or False = True)
# 10. True (True and True = True)