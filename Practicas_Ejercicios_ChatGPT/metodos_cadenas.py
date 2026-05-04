# ==============================================================================
# EJERCICIOS DE MÉTODOS DE CADENAS (STRINGS)
# ==============================================================================
# INSTRUCCIONES:
# Escribe el código necesario debajo de cada comentario para resolver el reto.
# Usa los métodos que acabas de documentar (upper, find, split, etc.)
# ==============================================================================

# --- SECCIÓN 1: CONVERSIÓN (upper, lower, capitalize) ---

# Ejercicio 1:
# Convierte la cadena "programación en python" para que la primera letra sea 
# mayúscula y el resto minúsculas.
cadena1="programación en PYTHON"
ejercicio1=cadena1.capitalize()
print(f"Ejercicio 1: {ejercicio1}")

# Ejercicio 2:
# Tienes la variable sistema = "Scada de Control". 
# Guárdala en una nueva variable totalmente en MAYÚSCULAS.
sistema="Scada de Control"
ejercicio2=sistema.upper()
print(f"Ejercicio 2: {ejercicio2}")

# --- SECCIÓN 2: BÚSQUEDA (find, index) ---

# Ejercicio 3:
# Busca en qué posición se encuentra la palabra "Said" en cadena1.
cadena1="Hola soy Said"
ejercicio3=cadena1.find("Said")
print(f"Ejercicio 3: {ejercicio3}")

# Ejercicio 4:
# Busca la posición de la letra "z" en la frase "Aprendiendo Python". 
# ¿Qué resultado te da y por qué?
frase="Aprendiendo Python"
ejercicio4=frase.find("z")
print("El resultado deberia ser '-1' por que no esta la 'z' en la frase elegida ")
print(f"Ejercicio 4: {ejercicio4}")

# --- SECCIÓN 3: CONSULTA (isnumeric, isalpha) ---

# Ejercicio 5:
# Verifica si la cadena "2026" es numérica.
cadena1="2026"
ejercicio5=cadena1.isnumeric()
print(f"Ejercicio 5: {ejercicio5}")

# Ejercicio 6:
# Verifica si la cadena "Said programador" es puramente alfabética (isalpha).
# Tip: Observa qué pasa con el espacio entre el nombre y el apellido.
cadena1="Said programador"
ejercicio6=cadena1.isalpha()
print("El siguiente resultado deberia ser 'False' ya que el espacio no es un caracter que este en los caracteres alfabéticos")
print(f"Ejercicio 6: {ejercicio6}")

# --- SECCIÓN 4: CONTEO Y VERIFICACIÓN (count, len, starts/ends) ---

# Ejercicio 7:
# Cuenta cuántas veces aparece la letra "o" en: "Hola, soy programador".
cadena1="Hola, soy programador"
ejercicio7=cadena1.count("o")
print(f"Ejercicio 7: {ejercicio7}")

# Ejercicio 8:
# Verifica si el archivo "documento.pdf" termina con la extensión ".pdf".
archivo="documento.pdf"
ejercicio8=archivo.endswith(".pdf")
print(f"Ejercicio 8: Verificación:{ejercicio8}")

# --- SECCIÓN 5: TRANSFORMACIÓN (replace, split) ---

# Ejercicio 9:
# En la cadena "Me gusta Java", reemplaza "Java" por "Python".
cadena1="Me gusta Java"
ejercicio9=cadena1.replace("Java", "Python")
print(f"Ejercicio 9: {ejercicio9}")

# Ejercicio 10:
# Convierte la frase "lunes-martes-miercoles" en una lista, 
# usando el guion (-) como separador.
frase="lunes-martes-miercoles"
ejercicio10=frase.split("-")
print(f"Ejercicio 10: {ejercicio10}")

# --- DESAFÍO FINAL (COMBINADO) ---

# Ejercicio 11:
# Tienes: datos = "100,200,300". 
# Sepáralos por comas para obtener una lista y luego suma el primer 
# elemento (convertido a entero) con el último (convertido a entero).
datos="100,200,300"
ejercicio11=datos.split(",")
ejercicio11=int(ejercicio11[0])+int(ejercicio11[2])#Nuevo: int() Transforma el dato a un int
print(f"Ejercicio 11: {ejercicio11}")

# ==============================================================================
# RESPUESTAS PARA COMPROBAR
# ==============================================================================
# 1. "Programación en python" (.capitalize())
# 2. "SCADA DE CONTROL" (.upper())
# 3. Posición 10 (en "Hola, soy Said")
# 4. Resultado: -1 (porque .find() devuelve -1 si no existe la letra)
# 5. True (.isnumeric())
# 6. False (porque el espacio NO es una letra del abecedario)
# 7. 3 veces (.count("o"))
# 8. True (.endswith(".pdf"))
# 9. "Me gusta Python" (.replace("Java", "Python"))
# 10. ["lunes", "martes", "miercoles"] (.split("-"))
# 11. 100 + 300 = 400 (Usa split, int() y los índices [0] y [2])