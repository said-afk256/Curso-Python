#Los operadores de comparación dan como resultado solamente "True" y "False" 
#El resultado es MUY utilizado en condicionales, sirve mucho para eso

#El signo "=" es para Asignar
#El signo "==" es para comparar y decir si son iguales o no

igual_que= 5==6 #Resultado: False

distinto_que= 5!=6 #Resultado: True

mayor_que= 5>6 #False

menor_que= 5<6 #True

mayor_igual_que= 5>=6 #False

menor_igual_que= 5<=6 #True

#Nota: para escribir multilinea dejas presionado "Alt" y haces Click en las lineas que escribiras
print(igual_que)
print(distinto_que)
print(mayor_que)
print(menor_que)
print(mayor_igual_que)
print(menor_igual_que)
print()
print()
print()

#operación combinada
a=5
b=10
c=20

comparación_numerica= a+b < c
print(comparación_numerica)

contraseña_almacenada= "Burrito17"
contraseña_escrita= "burrito19"

comparación_contraseña= contraseña_almacenada== contraseña_escrita
print(comparación_contraseña)#El resultado debe de ser falso ya que las contraseñas no coinciden, la escrita empieza con minusculas y termina con 19 en vez de 17
