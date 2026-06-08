#08/06/2026
#Creación de un dict con una función
diccionario= dict(nombre= "Said", apellido="Burciaga")
print(diccionario)
print()

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario={frozenset(["Dalto","Rancio"]):"jajaja"}
print(diccionario)
print()

#Creando llaves con fromkeys() con valor por defecto: none
diccionario= dict.fromkeys(["Nombre","Apellido"])# se pone el dict por que la variable es un diccionario y un "." por usar un método de diccionario
#El resultado es que Las llaves de la lista no tienen un valor asignado
#Con ("nombre","apellido") el nombre se itera con el apellido, por eso se agregan los [] para evitar esto
print(diccionario)
print(diccionario["Nombre"])
print()

#Creando llaves con fromkeys(). Sin el "[]"
diccionario= dict.fromkeys("ABCD" , "Valor1")
#El primer valor es iterable (se desglosa)
#El segundo valor es la igualación para el primer valor (El valor para el desglose)
print(diccionario)
print()

#Creando llaves con fromkeys() con valor por defecto: No se
diccionario= dict.fromkeys(["Nombre","Apellido"], "No se")  
print(diccionario["Nombre"])
print()