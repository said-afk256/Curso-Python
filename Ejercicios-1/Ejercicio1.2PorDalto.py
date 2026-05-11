#Por Dalto 11/05/2026 4:30pm - 
#Le pedimos al usuario que nos diga una frase (o varias)
frase=input("Decime una frase y te calculo cuanto te tardarias si tuvieras que decirla: ")

#Creamos una lista con todas las palabras de la frase (se separan)
palabras_separadas= frase.split(" ")

#Usamos Len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras=len(palabras_separadas)

#En caso de que tarde más de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras>120:
    print("Para loco tampoco te pedi un testamento")
else:
    print()
    
#Calculamos cuanto tardaría en decir las palabras y se lo decimos
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras*100//2*1.3/100} segundos")
#El calculo de la velociada en que lo diria Dalto esta mal, se supone que es un 30% rapido pero en el resultado 
#resulta que es mas lento, se deberia cambiar la operación para resolver eso
#En general este código esta más optimizado que el mio, ya que ni era necesario hacerlo una lista para usar un split,
#si split fuera un método de lista y no una función, seria una resolución parecida a la mia, pero no es el caso
#igual todo bien