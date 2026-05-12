#12/05/2026

#Creando un conjunto con set
conjunto=set(["Dato1"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1=frozenset(["Dato1","Dato2"])

conjunto2={conjunto1,"Dato3"}

print(conjunto2)
print()

#Teoria de los subconjuntos
conjunto1={1,3,5,7}
conjunto2={1,3,5}
#Función issubset()
#Sirve para comprobar si un conjunto es un subcojunto de un conjuto
resultado=conjunto2.issubset(conjunto1)#El resultado es booleano
resultado=conjunto2 <= conjunto1#Sirve igual que la función
#Ejemplo que dice esta función: ¿El conjunto 2 es un subconjunto del conjunto 1?
#obviamente también se puede preguntar viceversa

print(resultado)

#Función issuperset()
#Sirve para comprobar si un conjunto es un supercojunto de un conjuto
resultado=conjunto1.issuperset(conjunto2)
#Con signos
resultado=conjunto1 > conjunto2

print(resultado)
print()

#Función isdisjoint()
#Verificar si hay algun número en común
#True si son completamente diferentes y False si tienen al menos un elemento en común
resultado=conjunto2.isdisjoint(conjunto1)