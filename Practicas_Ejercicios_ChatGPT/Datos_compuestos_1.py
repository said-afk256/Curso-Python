# 1.- Crea una lista con 4 elementos (nombre, edad, si estudias, altura)
# Imprime el segundo elemento de la lista
Lista=['Said', 18, 'Si estudio', 1.72]
print(Lista[1])#Recordar que el indice cuenta desde el 0, el elemento 2 seria el 1 en este caso(si me lo se)

# 2.- Crea una lista con 5 números
# Cambia el tercer valor por otro número y luego imprime la lista completa
Lista=[1,2,3,4,5]
Lista[2]=100
print(Lista[2])
# 3.- Crea una tupla con 4 datos (marca, modelo, año, eléctrico=True/False)
# Imprime el último elemento
Auto=("BYD", "Dolphin Mini", "2022", True)
print(Auto[3])

# 4.- Intenta modificar un valor dentro de una tupla
# ¿Qué sucede? Escribe el error como comentario
#Auto[2]=2025   Error: No se puede modificar una Tupla, esa es su diferencia importante con un List


# 5.- Crea un set con 5 elementos (pueden ser nombres)
# Intenta agregar un elemento repetido y luego imprime el set
nombres={'Phrolova','Cantarella','Qiyuan','Roccia','Shorekeeper','Phrolova'}
print(nombres)
#Nota: En los sets no se puede repetir datos y no llevan orden
# 6.- Crea un set con diferentes tipos de datos
# Imprime el set y observa el orden
set={'Zani', 2.2, 'Phoebe', 2, 'Shorekeeper',1.8}
print(set)
#observación: Se ordeno con números primero de pequeño a grande, luego ya los nombres
# 7.- Crea un diccionario con las claves: nombre, edad, carrera
# Imprime solo el valor de "carrera"
alumno={
    'nombre': 'Said',
    'edad':18,
    'carrera':'programación'
}
print(alumno["carrera"])
# 8.- Crea un diccionario con 4 elementos
# Cambia el valor de una clave existente e imprime todo el diccionario
personaje={
    "nombre":"Hiyuki",
    "elemento":"Glacio",
    "arma":"Espada Ligera",
    "arquetipo":"ToneBreaker o Roptura de Tonalidad"
}
print(personaje)
print()
personaje['arquetipo']= "Dots"

print(personaje)
# 9.- Crea una lista con 3 elementos
# Luego crea una tupla con los mismos elementos
# Imprime ambos
nuevos_personajes=["Hiyuki", "Denia", "Lucilla"]
nuevosPersonajes=("Hiyuki", "Denia", "Lucilla")
print(nuevos_personajes)
print()
print(nuevosPersonajes)
# 10.- Crea un diccionario que tenga un dato duplicado en los valores
# Imprime el diccionario y observa si hay problema
Denia={
    "nombre":"Denia",
    "elemento":"Fusion",
    "arma":"Desconocido",
    "arquetipo":"ToneBreaker o Dots",
    "nombre":"Den"
}
print()
print(Denia)
#Observación: se puede redefinir la variable indice dentrod del diccionario

#💡 Consejos sobre el tema
#Las listas son las más usadas porque puedes modificar, agregar y eliminar elementos fácilmente.
#Las tuplas se usan cuando quieres proteger datos que no deben cambiar (como configuraciones).
#Los sets son útiles para eliminar duplicados automáticamente, pero no sirven si necesitas acceder por posición.
#Los diccionarios son clave cuando necesitas relacionar datos (como nombre → valor).
#Recuerda:
#Lista → [] (modificable)
#Tupla → () (inmutable)
#Set → {} (sin orden ni duplicados)
#Diccionario → {clave: valor}