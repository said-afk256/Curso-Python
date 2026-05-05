#05/05/2026
#Recordar que Python es un lenguaje interprete linea a linea, por lo que todo se va haciendo linea a linea
#Por eso podemos llamar a la lista varias veces sin que se guarde y cambien todo


#Función "list"
lista=list(["Spiderman 1", "Spiderman 2", 1, 2])
#list(Crea una lista)
print(lista)
print(dir(lista))
#Función Len
#Cuenta la cantidad de elementos existentes en la lista
metodo_len= len(lista)
print(metodo_len)

#Método append
#Agrega un elemento nuevo a la lista
lista.append("Spiderman 3")
print(f"Se agrego 'Spiderman 3' {lista} ")

#Método insert
#Inserta un elemento nuevo a la lista desde la posición que tu deseas.
#Si ya existe un elemento en esa posición, el elemento original de esa posición sera desplazado al siguiente, por ejemplo, si estaba en la posicion 0, este se pasara a la 1
#Recordar que las listas se cuentan desde el 0 cuando se habla de posiciones de los elementos, el "indice"
#lista.insert(posición_que_tomara_en_la _lista, elemento_agregado )
lista.insert(2, "Posición 3")
print(lista)
print(f"Cantidad de elementos actuales: {len(lista)}")
lista.insert(10,"Posición no existente anteriormente '10'")# se pone al final
print(lista)#Aunque con el insert hayamos puesto una posición inexistente, el resultado se fue al ultimo indice
lista.append("Hola")
print()
print(lista)#Aqui se ve que el "Hola" paso al ultimo indice, sin importar que el anterior insert se supone que esta una posición después porque el "Hola" ya fue interpretado después del insert
print(f"Cantidad de elementos en la lista en este punto: {len(lista)}")

#Método Extend
lista.extend([False, 30])
print()#Espacio entre listas
print(lista)

"Borrar y remover"

#Método pop
print()
print(f"Cantidad actual de elementos en la lista antes del pop(): {len(lista)}")
print(lista)
print()
lista.pop(0)
print(f"Cantidad de elementos despues del pop(): {len(lista)}")
print(lista)
#Nota: igual aqui en el uso del pop() se puede usar el indice -1 hacia atras para tomar el ultimo elemento de la lista.
#-1 es el ultimo elemento, -2 el penultimo, 3 el antepenultimo, y asi sucesivamente

#Método remove
print()
lista.remove("Posición 3")#Eliges un elemento a eliminar
print(f"Se removio 'Posición 3' de la lista: {lista}")

#Método clear
lista.clear()
#Borra todos los elementos de la lista

"Métodos de ordenamiento"

#Método Sort
#Este método ordena por orden del mas paqueño al mas grande(Ascendente), si hay boolenanos, iria en este orden:
#False, True, Número mas pequeño-Número mas Grandes
#Solo acepta números y booleanos (Por lo que no pueden usarse strings)
lista.append(500)
lista.append(89324)
lista.append(12435)
lista.append(True)
lista.append(False)
print(lista)
lista.sort()
print(f"Lista ordenada de menor a mayor: {lista}")
#Parametro reverse
#Con reverse=True podremos invertir el orden del sort
print()
lista.sort(reverse=True)
print(f"Sort con reverse: {lista}")

#Método reverse
#SI funciona con strings
#Este método NO ordena la lista, solamente pone todos los datos al reverse
print()
lista1=[True, 3, 2, 9, 7, 10, False, "hola"]
print(f"Nueva lista: {lista1}")
lista1.reverse()
print(f"Darle reverse a la ultima lista: {lista1}")
print()
#Para que se ordene una lista, se usa el sort
lista1.remove("hola")#No acepta strings el método sort
lista1.sort()
print(lista1)#En la lista resultante podremos ver como ordena todos los datos y luego hace su trabajo de ordenarlos de manera ascendente

#Verificación index
print()
lista1.index(10) #Buscara si existe el elemento en la lista, el parametro tendra que ser exactamente igual
#al elemento buscado en la lista para que no salte una excepción(error).
#Los index en métodos de lista ahi con solo se encuentre una coincidencia esta bien, en listas no.
