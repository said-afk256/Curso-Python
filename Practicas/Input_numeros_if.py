#05/05/2026

pregunta=int(input("Si tu número es entero, inserta 1, sino, cualquier otro numero entero para decimales: "))#investigar después como limitar el resultado
if pregunta==1:
    numero=input("El siguiente número se multiplicara X2: ")
    #Cambiando el número a un Entero y multiplicandolo por 2
    resultado_entero=int(numero)*2#Si el número ingresado es decimal, saltara un error
    print(f"Resultado en entero: {resultado_entero}")
else:
    numero=input("El siguiente número se multiplicara X2: ")
    #Cambiando el número a un Float y multiplicandolo por 2
    resultado_float=float(numero)*2
    print(f"Resultado en Float o decimal: {resultado_float}")




#Comentario de Youtube: " 2:43:15 No seria mas facil hacer:"
#numero = int(input("dame un numero, capitan: "))
#numero = numero * 2
#print(numero)