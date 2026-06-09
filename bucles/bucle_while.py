#09/06/2026

#Un bucle while es un bucle que se activa al cumplir cierta condición, no es como el for, que completa todo
#el bucle, sino, que realiza el bucle hasta que deje de cumplirse el bucle


#Creando un contador que va a ir sumandose
contador=0

#Mientras que la condición se cumpla, el bucle va a seguir ejecutando.
#Vuelta, tras vuelta se verifica la condición
while contador<10:#Mientras contador sea menor a 10, se ejecutara el siguiente código
    print(contador)
    contador+=1 #Se pone esta expresión para evitar que el bucle sea infinito, ya que el bucle se
#repetira de manera indefinida hasta que contador sea 10, entonces sumamos +1 al valor de contador
#para que en cada vuelta valga 1 mas y llegue asi al 10 y terminar el bucle.
print("Se acabo el bucle while")
print(f"Valor que conservo el contador: {contador}")
print()




#si queremos que tenga limite el while pero no queremos que aumente el valor, podemos hacer lo siguiente
numero=0
contador=0 #Reiniciamos el contador por que lo usamos en el anterior bucle, saliendo con un valor de 10
while contador<5:
    print(numero)
    contador+=1
print("Se termina el segundo bloque")