#Recordar que Python es un lenguaje interprete linea a linea, por lo que todo se va haciendo linea a linea
#Por eso podemos llamar a la lista varias veces sin que se guarde y cambien todo


#Función "list"
lista=list(["Spiderman 1", "Spiderman 2", 1, 2])
#list(Crea una lista)
print(lista)

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
print(lista)#Aqui se ve que el "Hola" paso al ultimo indice, sin importar que el anterior insert se supone que esta una posición después porque el "Hola" ya fue interpretado después del insert
print(f"Cantidad de elementos en la lista en este punto: {len(lista)}")

#Método Extend