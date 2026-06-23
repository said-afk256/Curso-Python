#11/06/2026

#forma no optima de sumar valores

#def suma(lista):
#   numeros_listados=0
#   for numero in lista:
#       numeros_listados=numeros_listados+numero
#   return numeros_listados
#resultado=sum(2+2+5+1)
#print(resultado) #10

#Utilizando el operador " * " como argumento (*args)
#Este operador junta varios parametros para que sean uno solo
#Ejemplo= (12,2,1) pasa a (12 2 1)
def suma(nombre,*numeros):#el operador * tiene que ir al ultimo ya que no deja agregar mas parametros después de este
    return f"Nombre del usuario: {nombre}, su suma es de: {sum(numeros)}"
resultado=suma("Said", 12+24+64)
print(resultado)

#Forma optima de sumar valores
def suma_total(numeros):
   print(*numeros)
   return suma([*numeros])
 
resultado2=suma_total([2+2+5+1])
print(resultado)