numeros=[1,2,3,4,5,6,7,8,9,2345,34,65,32]

#Creando una función para multiplicar por 2
multiplicar_por_dos= lambda x: x*2
#Las funciones Lambda son funciones anonimas, es decir, que no estan asignadas o no estan guardadas
#ya no los puedes volver a llamar mas adelante, aunque si puedes guardala en un variable
#Sirve mucho para funciones simples, de un sola condición



#Creando una función comun que diga si es par o no
#def es_par(num):
#    if(num%2==0):
#        return True
    
#Usando Filter con una función común
#numeros_par=filter(es_par(numeros))


#Creando lo mismo de antes pero con lambda
numeros_pares=filter(lambda numero: numero%2==0, numeros)
print(list(numeros_pares))#Tiene que ser una lista por que eso es lo que devuelve filter
#Ya que funciona como un bucle que repasa cada número de la lista y crea uno poniendo solamente los TRUE