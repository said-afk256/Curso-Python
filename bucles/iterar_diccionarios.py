diccionario = {
    "nombre": "Lucas",
    "apellido": "Dalto",
    "subs": 1000000 
}

print(diccionario)
print()

#Recorriendo el diccionario para obtener las claves
for key in diccionario:#No importa si cambias la varible "key" por otra, de igual manera te regresa las claves del diccionario
    print(key)
print()

#Recorriendo un diccionario con items() para obtener la clave y el valor
#Para hacerlo se necesita usar el método ".items()", ya que este nos permite iterar los elementos(valores) del diccionario
for key in diccionario.items():
    print(key)#Nos devuelve una tupla (clave, valor)
print()
#
for datos in diccionario.items():
    clave=datos[0]
    valor=datos[1]
    print(f"La clave es {clave}, su valor: {valor}")
print()
