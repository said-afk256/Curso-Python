# =========================================================================
# EJERCICIOS DE ESTRUCTURAS DE DATOS EN PYTHON
# =========================================================================

# EJERCICIO 1: Listas (Acceso)
# Crea una lista llamada 'frutas' con: "manzana", "pera", "uva".
# Imprime mediante el índice correspondiente únicamente la palabra "pera".
# Escribe tu código abajo:
frutas=["manzana","pera","uva"]
print("ejercicio 1: " + frutas[1])

# EJERCICIO 2: Listas (Modificación)
# Tienes la lista: animales = ["perro", "gato", "pez"]
# Cambia "pez" por "loro" usando su índice y luego imprime la lista completa.
# Escribe tu código abajo:
animales=["perro","gato","pez"]
animales[1]="loro"
print("ejercicio 2: ")
print(animales)
# EJERCICIO 3: Tuplas (Inmutabilidad)
# Crea una tupla llamada 'coordenadas' con los valores (10, 20).
# Intenta cambiar el 10 por el 15. ¿Qué sucede? (Comenta la línea que da error).
# Escribe tu código abajo:
coordenadas=(10,20)
#Código invalido -> coordenadas[0]=5
print("ejercicio 3: ")
print(coordenadas)
# EJERCICIO 4: Tuplas (Acceso)
# Dada la tupla: datos = ("Python", 2024, "VS Code")
# Imprime el último elemento ("VS Code") accediendo a su posición.
# Escribe tu código abajo:
datos=("Python", 2024, "VS code")
print("ejercicio 4: " + datos[2])

# EJERCICIO 5: Sets (Duplicados)
# Crea un conjunto (set) llamado 'mi_set' con los valores: 1, 2, 2, 3, 3, 3.
# Imprime el set y observa qué pasa con los números repetidos.
# Escribe tu código abajo:
mi_set={1,2,2,3,3,3}
print("Ejercicio 5:")
print(mi_set)

# EJERCICIO 6: Sets (Búsqueda)
# Dado el conjunto: colores = {"rojo", "azul", "verde"}
# Verifica si "amarillo" está dentro del conjunto (usa el operador 'in') e imprime el resultado (True/False).
# Escribe tu código abajo:
colores={"rojo","azul","verde"}
print("ejercicio 6: ")
print("amarillo" in colores)

# EJERCICIO 7: Diccionarios (Acceso)
# Crea un diccionario 'auto' con: marca: "Toyota", modelo: "Corolla", año: 2022.
# Imprime solo el valor asociado a la clave 'modelo'.
# Escribe tu código abajo
auto={
    "marca":"Toyota", "modelo":"Corolla", "año":2022
}
print("ejercicio 7: " + auto["modelo"])

# EJERCICIO 8: Diccionarios (Modificación)
# Al diccionario 'auto' anterior, cámbiale el año a 2024.
# Luego imprime el diccionario para verificar el cambio.
# Escribe tu código abajo:
auto["año"]=2024
print("ejercicio 8: ")
print(auto)

# EJERCICIO 9: Identificación de tipos
# Crea una variable 'incógnita' que use llaves {}, pero que tenga pares clave:valor.
# ¿Qué estructura es? Compruébalo usando la función print(type(incógnita)).
# Escribe tu código abajo:
incognita={"clave":"valor"}
print("ejercicio 9: ")
print(type(incognita))

# EJERCICIO 10: Mezcla de estructuras
# Crea una lista llamada 'usuarios' que contenga dos diccionarios. 
# Cada diccionario debe tener las claves 'nombre' y 'id'.
# Imprime el nombre del segundo usuario.
# Escribe tu código abajo:
usuarios=[{
    "Nombre":"Said","id":1
}, {"Nombre":"Valeria", "id":2}]
print("ejercicio 10: " + usuarios[1]["Nombre"])
#Ej10: Necesite ayuda

# =========================================================================
# EJERCICIOS ADICIONALES: ESTRUCTURAS DE DATOS (PARTE 2)
# =========================================================================

# EJERCICIO 11: Listas (Índices Negativos)
# Dada la lista: lenguajes = ["Python", "Java", "C++", "JavaScript", "Rust"]
# Imprime el penúltimo elemento ("JavaScript") utilizando un índice negativo.
# Escribe tu código abajo:
lenguajes=["Python", "Java", "C++", "JavaScript", "Rust"]
print("Ejercicio 11: ")
print(lenguajes[-2])
#requirio investigación



# EJERCICIO 12: Listas (Slicing básico)
# Tienes la lista: numeros = [10, 20, 30, 40, 50]
# Crea una nueva lista llamada 'sub_lista' que contenga solo el 20 y el 30.
# Pista: usa numeros[1:3]. Luego imprímela.
# Escribe tu código abajo:
numeros=[10,20,30,40,50]
sub_lista= numeros[1:3]
print("Ejercicio 12: ")
print(sub_lista)
#investigado


# EJERCICIO 13: Tuplas (Empaquetado)
# Crea una tupla llamada 'punto' que contenga tres valores: x, y, z (usa 5, 10, 15).
# Intenta imprimir solo el valor de 'y' usando su índice.
# Escribe tu código abajo:
punto=(5,10,15)
print("Ejercicio 13: ")
print(punto[1])


# EJERCICIO 14: Tuplas (Conversión)
# Convierte la lista: colores_lista = ["cian", "magenta"] en una tupla.
# Pista: usa la función tuple(). Imprime el tipo de dato resultante.
# Escribe tu código abajo:
colores_lista=["cian","magenta"]
tuple(colores_lista)
print("Ejercicio 14: ")
print(type(colores_lista))#El resultado seguira siendo una lista porque para guardar el cambio se necesita una nueva variable 

# EJERCICIO 15: Sets (Eliminar duplicados)
# Tienes esta lista con errores: ids = [101, 102, 101, 103, 102, 104]
# Conviértela a un set para eliminar los duplicados y luego vuelve a imprimirla.
# Escribe tu código abajo:
ids=[101, 102, 101, 103, 102, 104]
ids=set(ids)#Aqui si se guarda la modificación por que guardamos el cambio en una variable
print("Ejercicio 14: ")
print(type(ids))

# EJERCICIO 16: Sets (Método add)
# Crea un set vacío llamado 'nombres'. 
# Agrega el nombre "Ana" usando el método .add() e intenta agregarlo dos veces.
# Imprime el set final.
# Escribe tu código abajo:
nombre= set()
nombre.add("Ana")
nombre.add("Ana")
print("Ejercicio 14: ")
print(nombre)
print(type(nombre))


# EJERCICIO 17: Diccionarios (Nuevas llaves)
# Crea un diccionario 'capitulo' con: 'titulo': 'Introducción'.
# Agrega una nueva clave 'paginas' con el valor 15. Imprime el diccionario.
# Escribe tu código abajo:
capitulo={
    "titulo":"introducción"
}
capitulo["paginas"]=15
print("Ejercicio 17: ")
print(capitulo)

# EJERCICIO 18: Diccionarios (Método keys)
# Del diccionario: pc = {'procesador': 'i7', 'ram': '16GB', 'ssd': '512GB'}
# Imprime solo las llaves (keys) del diccionario.
# Escribe tu código abajo:
pc={"procesador":"i7",
    "ram":"16GB",
    "ssd":"512GB"}
print("Ejercicio 18: ")
print(pc.keys())


# EJERCICIO 19: Diccionarios (Eliminar)
# Tienes: datos = {'id': 1, 'secreto': '1234', 'rol': 'admin'}
# Elimina la clave 'secreto' usando 'del' o '.pop()'. Imprime el resultado.
# Escribe tu código abajo:
datos = {'id': 1, 'secreto': '1234', 'rol': 'admin'}
datos.pop("secreto")
print("Ejercicio 19: ")
print(datos)


# EJERCICIO 20: El reto final (Estructuras anidadas)
# Crea un diccionario llamado 'inventario'.
# La clave 'productos' debe tener como valor una LISTA con: "teclado", "mouse".
# Imprime el primer producto de esa lista accediendo desde el diccionario.
# Escribe tu código abajo:
inventario={"productos":["teclado", "mouse"]
}
print("Ejercicio 20: ")
print(inventario["productos"][0])