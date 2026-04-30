#Variables#
#Las variables almacenan la información que se les asigna
a=1
b=3
c=a+b

print(c)

#Cuando se redifine una variable, toma la ultima redifinición para el resultado
nombre="Dalto" #Definición
nombre="Pendrito "#Redifinición
nombre="Anon"#Redifinición

print(nombre)

#El "+=" es para sumar (también se puede cualquier otro signo)
#el valor anterior de la variable con el número nuevo que pusiste
numero=10
numero+=1

print(numero)

numero+= 5
concatenacion= f"ahora con +=5 es: {numero}"
print(concatenacion)

#ejemplo con resta
numero2=10
numero2-=5
print(numero2)
numero2-=2

print(numero2)

#El "f" + "{}" sirve para concatenar texto con datos de otro tipo
#El dato no String pasa a ser String con este formato
#Esta función se llama "f strings"
nombre=True
bienvenida= f"Hola {nombre} ¿cómo estas chaval?"
print(bienvenida)

#una forma de concatenar texto(se recomienda mas el formato anterior)
nombre="Mario"
welcome= "hola " + nombre
#Se pone espacio en el hola ya que en la concatenación toma cualquier caracter, como el espacio
print(welcome)

#Uso de "del"

nombre1=False
bienvenida1= f"Hola {nombre1} ¿cómo estas chavalon?"
del nombre1
#en este punto, la variable ya no esta definida
#aun asi se guardo el valor de "False" en "bienvenida1"
#Esto pasa ya que se utilizo "nombre1" antes de borrar su valor
print(bienvenida1)
del bienvenida1

#operadores de pertenencia (in/not in)#

#Con IN buscamos que un valor si este en la variable
#El resultado de la impresión es con True y False
nombre1="Mario"
bienvenida1= f"Que onda {nombre1} ¿como va todo?"
print()
print("Mario" in bienvenida1)
print( )

#Con NOT IN buscamos que el valor no este en la variable
#True si no esta, False si esta

print("Mario" not in bienvenida1)
print( )

#concatenar con +
bienvenida= "Hola" + "¿como andamos?";

print(bienvenida)

#Definiendo una variable con camelCase#
#Separar palabras con mayusculas(sin espacios) para convertirla variable
camelCaseVariableEnEfecto= 1
#Definiendo una varible con Snake_case
#Para separar palabras, se una guion bajo "_"
snake_is_the_official_mode=2;

print(camelCaseVariableEnEfecto)
print(snake_is_the_official_mode)
