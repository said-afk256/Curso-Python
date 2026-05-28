# ==============================================================================
# EJERCICIOS DE PYTHON: FUNDAMENTALES Y SECCIÓN BÁSICA
# ==============================================================================

# ------------------------------------------------------------------------------
# EJERCICIO 1: Variables y Operadores Aritméticos
# ------------------------------------------------------------------------------
# Enunciado:
# Crea una variable llamada 'precio_original' con el valor 120.
# Crea otra variable llamada 'descuento' con el valor 15 (que representa un 15%).
# Calcula el precio final tras aplicar el descuento y guárdalo en 'precio_final'.
# Imprime el resultado con un mensaje claro.
# Escribe tu código aquí abajo:
precio_original=120
descuento=15
precio_final=precio_original-(120*15/100)#Mejor=(precio_original*descuento/100)
print(f"Ejercicio 1: Con tu cupon del 15% de descuento para tu compra de 120, el total es de: {precio_final} pesos")

print()

# ------------------------------------------------------------------------------
# EJERCICIO 2: Condicionales y Operadores de Comparación
# ------------------------------------------------------------------------------
# Enunciado:
# Pide al usuario que introduzca su edad usando input().
# Convierte ese dato a un número entero.
# Si la edad es menor que 18, imprime "Acceso denegado".
# Si tiene entre 18 y 65 años (inclusive), imprime "Acceso concedido".
# Si es mayor de 65, imprime "Acceso premium".

# Escribe tu código aquí abajo:
edad=int(input("Introduce tu edad: "))
print("Ejercicio 2:")
if edad < 18:
    print("Acceso denegado")
elif edad >= 18 and edad<= 65:#No era necesario el and ni el "edad >=18" solamente el "edad<= 65"
#era mas que suficiente ya que se descarto los menores de edad en el primer if
    print("Acceso concedido")
else:
    print("Acceso premium")

print()


# ------------------------------------------------------------------------------
# EJERCICIO 3: Métodos de Strings y Formateo
# ------------------------------------------------------------------------------
# Enunciado:
# Dada la siguiente cadena de texto:
# "   pYtHoN eS uN lEnGuAjE gEnIaL   "
# 1. Elimina los espacios en blanco del principio y del final.
# 2. Convierte todo el texto a mayúsculas.
# 3. Reemplaza la palabra "GENIAL" por "INCREÍBLE".
# Imprime el resultado final.

# Escribe tu código aquí abajo:
texto="   pYtHoN eS uN lEnGuAjE gEnIaL   "
texto_limpio=texto.strip().upper().replace("GENIAL", "INCREIBLE")
print(f"Ejercicio 3: {texto_limpio}")
#Necesite ayuda, tuve que investigar de nuevo los metodos de cadenas y uno nuevo, el "strip"
#(creo que es nuevo)

print()

# ------------------------------------------------------------------------------
# EJERCICIO 4: Métodos de Listas
# ------------------------------------------------------------------------------
# Enunciado:
# Tienes la siguiente lista de compras: compras = ["manzana", "pera", "leche"]
# 1. Añade "pan" al final de la lista.
# 2. Añade "huevos" en la primera posición (índice 0).
# 3. Elimina "pera" de la lista.
# 4. Ordena la lista alfabéticamente.
# Imprime la lista final.

# Escribe tu código aquí abajo:
compras = ["manzana", "pera", "leche"]
compras.append("pan")
compras.insert(0, "huevos")
compras.remove("pera")#el metodo pop() es con indice, el remove se utiliza principalmente para poner el string exacto
compras.sort()
print(f"Ejercicio 4: Lista de compras final {compras}")

print()

# ------------------------------------------------------------------------------
# EJERCICIO 5: Métodos de Diccionarios
# ------------------------------------------------------------------------------
# Enunciado:
# Crea un diccionario llamado 'alumno' con las siguientes claves y valores:
# - "nombre": "Carlos"
# - "edad": 22
# - "curso": "Python"
# Luego:
# 1. Modifica la "edad" a 23.
# 2. Añade una nueva clave-valor: "nota": 9.5
# 3. Usa un método para obtener solo las llaves (keys) del diccionario e imprímelas.

# Escribe tu código aquí abajo:
alumno={
    "nombre": "Carlos",
    "edad": 22,
    "curso": "Python"
}
print("Eje5:")
print(f"Lista original: {alumno}")
alumno["edad"]=22
alumno["nota"]=9.5
llaves=alumno.keys()#No olvidar los parentesis de parametros para los metodos
print(f"Ejercicio 5: Lista actualizada {alumno}")
print(f"Llaves o keys de la lista: {llaves}")