#11/06/2026

#Creando nuestras propias funciones
#usamos el código "def"

def saludar():
    print("Hola Lucas, ¿como esta maestro?")

#Ejecutando una función simple

saludar()
#EN este caso no se necesita poner un print para la función, ya que en la función utilizamos un
#print(), si la función fuera diferente o no usara print(), en ese caso si se podria poner uno guardando
#en una variable el resultado ya que no puedes imprimir una función como tal
#Depende del contexto o el código de la función

#Creando una función con parametro
#Un PARAMETRO es una VARIABLE que se usa unicamente dentro de la función y nada mas
def saludo(nombre,sexo): #nuestra función saludo tendra 2 parametros
    sexo=sexo.lower()#convertimos todo a minusculas para que lo que escriba el usuario para que coincida con el siguiente if, recordad que python es Case Sensitive
    if(sexo=="mujer"):
        adjetivo="reina"
    elif(sexo=="hombre"):
        adjetivo="bro"
    else:
        adjetivo="amor"
    print(f"Hola {nombre}, mi {adjetivo}, ¿Cómo llevas la vida? ")
    #Las variables naranjas son los parametros, variables que solo funcionan dentro de la función y no afuera

saludo("Said", "Hombre")
saludo("Valeria", "mujeR")
saludo("Yael", "No-binario")
print()
#Escribiendo el nombre de la función, nos evitamos escribir el código entero 3 veces

#También pueden ir en los parametros números ya que las variables de la fución se definen con 
#los parametros que pongamos, al menos que, en el código haya una función que sea exclusivo de
#un tipo de variable, como ".lower()"(str) o ".get()"(list), etc

#Crear una función que nos retorne valores
def crear_contraseña_random(num):
    chars="abcdefghij"
    num_entero=str(num)
    num=int(num_entero[0])
    c1=num-2
    c2=num
    c3=num-5
    contraseña=f"{chars[c1]+chars[c2]+chars[c3]}{num*2}"
    return(contraseña)#El return saca el valor de la variable local(variable de la función), mas NO la variable en si
#La función termina automaticamente cuando encuentra un return

password= crear_contraseña_random(8)#si no hubiera return, password seria "None"
frase= f"Tu contraseña nueva es: {password}"#El valor se quedo guardado en password,
#password≠crear_contraseña_random, password=gid16
print(password)

print()

#return permite que una función entregue al exterior un valor calculado
#dentro de ella para que pueda ser utilizado en otras partes del programa.

#Crear una función que nos retorne MULTIPLES valores
def crear_contraseña_random(num):
    chars="abcdefghij"
    num_entero=str(num)
    num=int(num_entero[0])
    c1=num-2
    c2=num
    c3=num-5
    contraseña=f"{chars[c1]+chars[c2]+chars[c3]}{num*2}"
    return contraseña,num#tupla

#desempaquetando la función
password, primer_num=crear_contraseña_random(124908) #password=contraseña, primer_num=num [tupla(contraseña, num)]

#Mostrando los resultados obtenidos y los datos utilizados para obtenerlos
print(f"Tu contraseña es {password}")
print(f"El primer número utilizado para tu contraseña es {primer_num}")







#Crear una función que nos retorne MULTIPLES valores (versión tupla, es mas recomendable lo anterior)
def crear_contraseña_random(num):
    chars="abcdefghij"
    num_entero=str(num)
    num=int(num_entero[0])
    c1=num-2
    c2=num
    c3=num-5
    contraseña=f"{chars[c1]+chars[c2]+chars[c3]}{num*2}"
    return(contraseña, c1, c2, c3)#Este return nos dara una tupla por ser varios valores

password= crear_contraseña_random(8)
frase= f"Tu contraseña nueva es: {password}"
print(f"Password es: {type(password)}")

print(f"imprimiendo el password: {password}")
resultado2=crear_contraseña_random(8)[0]
resultado3=crear_contraseña_random(8)[1]#Cómo el resultado es una tupla, se puede buscar también con los parentesis []
print(f"Busqueda tupla con función 8, [0]: {resultado2}, [1]: {resultado3}")
print()





def porcentaje(total, cantidad):
    porcentaje=(cantidad/total)*(100)
    print(f"{cantidad} de {total} equivale a {porcentaje:.2f}%")
porcentaje(1700,200)
porcentaje(800,400)
porcentaje(1600,200)
porcentaje(5,2)
porcentaje(150, 60)#Si son 150 alumnos y 60 entran, que porcentaje es el que esta entrando?
porcentaje(150,80)
porcentaje(150,100)







"Explicación función crear_contraseña_random()"
# Llamamos a la función enviando el número 8
#crear_contraseña_random(8)

# ============================
# Dentro de la función
# ============================

# Se crea una cadena de caracteres que servirá como base
#chars = "abcdefghij"

# Índices:
# 0=a, 1=b, 2=c, 3=d, 4=e,
# 5=f, 6=g, 7=h, 8=i, 9=j

# Convertimos el número recibido a texto
#num_entero = str(num)

# Tomamos únicamente el primer dígito del número
# Ejemplo:
# "8"[0] = "8"
# "87"[0] = "8"
#num = int(num_entero[0])

# Calculamos tres posiciones para buscar letras
#c1 = num - 2
#c2 = num
#c3 = num - 5

# Si num = 8:
# c1 = 6
# c2 = 8
# c3 = 3

# Obtenemos las letras usando los índices calculados
# chars[6] = "g"
# chars[8] = "i"
# chars[3] = "d"

# Construimos la contraseña:
# letra de c1 + letra de c2 + letra de c3 + (num * 2)
#contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"

# Si num = 8:
# contraseña = "g" + "i" + "d" + "16"
# Resultado: "gid16"

# Mostramos la contraseña en pantalla
#print(contraseña)

# 1. Recibe un número.
# 2. Convierte el número a texto.
# 3. Toma solo el primer dígito.
# 4. Usa ese dígito para calcular posiciones.
# 5. Obtiene letras de la cadena "abcdefghij".
# 6. Une las letras y el doble del número.
# 7. Imprime la contraseña generada.