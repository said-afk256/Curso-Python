#05/05/2026
diccionario={
    "nombre":"Juan",
    "Apellido":"Carrera",
    "Subs":"1000000"
}

#Método keys
#Con este método nos devuelve todas las claves
keys=diccionario.keys()
print(f"Método Keys: {keys}")
print()

#Método get()
#Obtiene el valor de la key
get=diccionario.get("Apellido")
get1=diccionario.get("KeyNoExistente")#También se podria usar diccionario["clave"] pero si no encuentra la clave
#El programa lanza una excepción y no continua a diferencia de usar get() que esto no pasa
print(f"Apellido: {get}")
print(f"Resultado de get con un dato no existente: {get1}")
print()
#También el get() tiene la propiedad de dejar mensajes como el pop()
#get("KeyInexistente","Mensaje")

#Método clear()
#Borra todos los elementos del diccionario
#diccionario.clear()

#Método pop()
#Eliminar un elemento(key) del diccionario
diccionario.pop("Apellido", "None")#Borra un solo elemento a la vez
#Estructura: diccionario.pop("Key", "MensajeEnCasoDeNoEncontrarLaKey")
#Para poder ver el mensaje, se necesita guardar en una variable y luego imprimirla
#Ejemplo: mensaje=diccionario.pop("KeyInexistente","Mensaje")   print(mensaje)
print(f"Se borro las keys Apellido y Subs del siguiente diccionario y solo queda: {diccionario}")
print()

#Método items
#Lo que hace este método es iterar el diccionario
#Iterar:Recorrer los elementos para poder acceder a cada uno de ellos
iterar=diccionario.items()
print(iterar)
print()