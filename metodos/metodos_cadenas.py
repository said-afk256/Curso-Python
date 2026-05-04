cadena1="Hola, soy Said"
cadena2="Bienvenido CRACK"

#Función dir
resultadoDir= dir(cadena1) #Con esta función podemos ver todos los metodos del objeto que contenga
print(resultadoDir)

#Los métodos son las funciones aplicadas a objetos. Existen diferentes métodos para cada tipo de variable
#Los parentesis de los métodos se pueden poner parametros

#Método upper
resultado_upper= cadena1.upper() #Convirte toda la cadena a MAYUSCULAS
print(resultado_upper)
resultado_upper2= 'todo este texto se transformara en mayusculas por el "upper"'.upper()#También se puede usar con puro texto ya que es un método para todos los strings
print(resultado_upper2)

#Método lower
resultado_lower= cadena2.lower() #Convierte toda la cadena a minusculas
print(resultado_lower)

#Método capitalize
resultado_capitalize= cadena1.capitalize() #Convierte la primera letra a Mayuscula y todo lo demás a minusculas
#Nota: Podria decirse que primero transforma todo el texto a minusculas, ya después pone la primera letra a mayuscula
print(resultado_capitalize)

#Método find
#Con este método, el resultado sera la posición de la letra o palabra
#Para la posición, la cadena sera contada igual que una lista, la primera letra empezara con la posicion 0
"""0 2 4 6 8 
   Hola, soy Said
    1 3 5 7 9 """#En este ejemplo, la "H" seria 0 y la "d" final el 13

busqueda_find_palabra= cadena1.find("soy") #Buscara "soy" en la cadena de texto
print(busqueda_find_palabra)#El resultado sera el número de la posicion de "s" en donde esta "soy"

busqueda_find_letra= cadena1.find("a")#Buscara la primera "a" del todo el texto
print(busqueda_find_letra)

busqueda_find1= cadena1.find("ola")#Buscara cualquier cadena que contenga "ola" como lo seria "Hola"
print(busqueda_find1)#El resultado sera el número de la posición de la "o" aunque este dentro de "Hola"

busqueda_find_No_existente= cadena1.find("O")
print(busqueda_find_No_existente)
#NOTA: Si lo que buscamos no esta en el texto, el resultado sera -1
#Nota: Recordar que Python es Key Sensitive, por lo que si "find" no encuentra resultados de una letra que si esta en la cadena, puede ser porque una es mayuscula y otra es minuscula

#Metodo Index

#Es casi lo mismo que el metodo find
metodo_index=cadena2.find("i")
print(metodo_index)
#La diferencia con find es que si la letra no se encuentra,no hay coincidencias, index nos saltara una excepción y nos dara error en programa, lo parara ahi
#metodo_index=cadena2.find("b") #Resultado=Error