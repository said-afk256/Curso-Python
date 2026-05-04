cadena1="Hola, soy Said"
cadena2="Bienvenido CRACK"

#Estructura de Funciones:  Funcion(Parametro o variable)    funcion()
#Estructura de Métodos: Varible_o_Dato.Metodo(Parametros solo si es necesario)     variable.metodo()

"Función"
#Función dir
resultadoDir= dir(cadena1) #Con esta función podemos ver todos los metodos del objeto que contenga
print(resultadoDir)

#Los métodos son las funciones aplicadas a objetos. Existen diferentes métodos para cada tipo de variable
#Los parentesis de los métodos se pueden poner parametros
"Métodos para convertir valores"
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

"Métodos para buscar valores"
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

"Métodos de consulta"
#Método isnumeric
#Este método busca que la cadena solo contenga strings númericos y no un string normal, dando como resultado "True" y "False"
cadena_numeros="12345678910"
metodo_isnumeric=cadena_numeros.isnumeric()
print(f"método numerico verdadero: {metodo_isnumeric}")
isnumeric_sin_numeros=cadena1.isnumeric()
print(f"Método numerico falso: {isnumeric_sin_numeros}")#Resultado= False
#Contiene Strings normales, además de no contener números

#Método isalpha
#Este método busca que la cadena sea exclusicamente las letras del abecedario(A-Z), osea, puede dar error si se usan caracteres como el espacio o comas.Siempre dando como resultado "True" y "False"
texto_alphanumerico="AlphaNumericoTrueCienPorciento"
metodo_isalpha=texto_alphanumerico.isalpha()
print(metodo_isalpha)

isalpha_false=cadena1.isalpha()
print(isalpha_false)#Sera false por contener espacios y comas en la cadena

"Método para contar"
#Método Count
#Este método cuenta la cantidad de veces que una cadena esta en una cadena. El Resultado sera el número de veces que aparecio, si no hay coincidencias, sera 0
metodo_count=cadena1.count("a")#Veces que el caracter "a" aparecio en la cadena
print("Metodo Count:")
print(metodo_count)
metodo_count1=cadena1.count("Hola")#Veces que la cadena "Hola" aparecio
print(metodo_count1)
metodo_count3=cadena1.count("la, so")#En la cadena "Hola, soy Said" encontrara "la, soy" que es la parte donde esta "Hola," y "Soy"
print(metodo_count3)
metodo_count4=cadena2.count("1")#Sera 0 por que la cadena no contiene "1"
print(metodo_count4)

#Función Len
#Función para contar todos los caracteres que contiene la cadena
funcion_len=len(cadena2)
print(f"Función Len con cadena2: {funcion_len}")

"Métodos de verificación"
#Método starswith
#Verifica si la cadena empieza con el caracter especificado
metodo_startwith=cadena1.startswith("Ho")
print(metodo_startwith)
#Tener cuidado con el Key Sensitive, ya que si el texto es "Hola" pero ponemos "h" nos dara false por ser minuscula y no mayuscula como en el texto original

#Método endswith
#Verifica si la cadena termina con el caracter especificado
metodo_endswith=cadena1.endswith("h")
print(metodo_endswith)#Sera false ya que no termina con h

"Método de remplazo"
#Método replace
#Este método remplaza un valor por otro
#Dentro del parentesis tenemos dos valores, el primero es para buscar todo lo que coincida con este valor
#El segundo, remplazara todas las coincidencias por el valor nuevo que uno ponga
metodo_replace=cadena1.replace("la","lis")
print(metodo_replace)

"Método de separación"
#Método split
#Este metodo separa las cadenas por el caracter que queramos para formar una lista
#Sabemos que en una lista tenemos valores, entonces para obtener valores de una cadena, obtendremos un valor
#segun el caracter que especifiquemos, como los espacios o comas
metodo_split=cadena1.split(" ")#Creara valores por cada espacio
print(metodo_split)
cadena3="Ejemplo,con,comas,para,método,split y aqui no pongo comas para que veas que este pedazo de texto sera un solo valor"
metodo_split=cadena3.split(",")#Redifini la misma variable de metodo_split
print(metodo_split)#Hara una lista donde cada valor saldra de la separación de la cadena mediante comas
print(f"El tipo de resultado que nos da el split es el siguiente (debe ser una lista):{type(metodo_split)}")
#Como sabemos que el valor resultante de split es una lista, podemos usarla como tal
print(metodo_split[0])