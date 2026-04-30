#Matriz: Conjunto de datos
#Lista:Tipo de matriz

#1.- Lista
#Ejemplo de lista con el orden Nombre, que soy, estoy exelente, altura aprox
lista = ["Said Burciaga", "Soy programador", True, 1.72]

print(lista[0])
#Lo anterior es un array simple
#En el mundo de la programación, los arrays se cuentas desde el 0 hasta el número tope
#El elemento 1 recibe el indice 0, el elemento 2 el indice 1, y asi continuamente



#2.-Tupla
#La tupla es casi lo mismo que la lista, pero usa parentesis en vez de corchetes
Tupla=("Aemeath","Exostrider", False, 1.70)

print(Tupla[0])#Aunque la tupla use parentesis, en los prints se usa corchete
#Nota: Puedes llamar como quieras a la List y la Tupla o Tuple

#Diferencia principal: Los datos de la List son modificables
#y los Tupla no se puede modificar los datos que tiene dentro

#Modificación valida (List)
lista[0]="Leo Burciaga"
#La modificación sera valida si el print se realiza a partir de este punto
#Python=Interpretación linea a linea

#Modificación invalida(Tupla)
#list(0)= Luquitas Bobic

#3.- Set(Conjunto)
#No se puede acceder a los elementos por el indice
#No almacena datos duplicados

conjunto= {"Carthetya", "sacra docenlla", 40}

#print(conjunto[3]) -> no se puede acceder al elemento
print(conjunto)

#4.- Dict(Diccionario)
#La es estructura es key : value    y separamos por comas
diccionario={
    'nombre':'Phrolova',
    'alias':'Hecate',
    "arma":"catalizador", #Las comas son importantes
    'dato duplicado':'Hecate'
}

print(diccionario['nombre'])