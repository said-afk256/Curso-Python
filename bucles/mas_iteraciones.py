frutas = ["banana", "manzana", "ciruela", "pera", "naranja","granada", "durazno"]

#Usando "continue" en un bucle for
for fruta in frutas:
    if fruta=="granada":
        continue
        #lo que hace "continue" es que se salta una vuelta, entonces al poner como condición "granada"
        #lo que hara es que se salte granada del bucle
    #recordad que los for son bucles, en lo bucles se repite el código dando vueltas
    #por que en una vuelta llega al elemento 1, en la siguiente vuelta llega al 2 y asi
    print(f"Me voy a comer una {fruta}")
print()

#Usando "break" en un bucle for
for fruta in frutas:
    print(f" Se come la {fruta}") #Volviendo con el tema del ejercicio 4 del 1.py en iteracion
#Si el contexto es que después de la ciruela, a la persona le duele la panza y tiene que dejar de comer
#la fruta, PERO ya se comio la ciruela, para que el programa imprima que si la comio, entonces ahora
#ponemos print() primero que el if
    if fruta=="ciruela":
        break #El break rompera la secuencia del bucle (incluyendo el "else" del for)
else:
    print("se ejecuto el else del for")
print("Se acabo el bucle por el break")

#Iterar: recorrer un conjunto/recorrer los elementos de un conjunto

#Iteración con cadenas de texto
cadena="Hola Dalto"

for letra in cadena:
    print(letra)
#Al recorrer una cadena de texto, se recorre por cada caracter que contenga (incluyendo espacio y cualquier otro especial)
#Y cada caracter tiene un indice también

#for en una sola linea de código
numeros=[2,5,8,10]

#Queremos sacar el doble de la lista numeros, por que se hace lo siguiente:
numeros_duplicados=[x*2 for x in numeros] #Sirve para expresiones matematicas sencillas
#Se guarda en una variable, luego se abren corchetes como si fuera una lista y se pone la expresión
print(f"Lista numeros duplicado por 2: {numeros_duplicados}")#Si ponemos type() a la variable, saldra que es una lista

