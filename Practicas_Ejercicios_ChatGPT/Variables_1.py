# 1. Crea dos variables a=5 y b=10, luego guarda la suma en una variable c e imprime el resultado.
a=5
b=10
c=a+b
print(c)
# 2. Define una variable llamada nombre con tu nombre, luego redefínela con otro nombre e imprime el resultado final.
nombre='Said'
nombre='Dalto'
print(nombre)
# 3. Crea una variable numero=20 y usa += para sumarle 5. Imprime el resultado.
numero=20
numero+=5
print(numero)
# 4. Crea una variable numero2=50 y usa -= para restarle 15. Imprime el resultado.
numero2=50
numero2-=15
print(numero2)
# 5. Usa f-string para crear un mensaje que diga: "Hola (nombre), tienes (edad) años", usando variables.
edad=25
Mensaje_bienvenida= f"Hola {nombre}, tienes {edad} años"
print(Mensaje_bienvenida)
# 6. Concatena dos strings usando el operador + para formar la frase: "Python es genial".
print("Python es " + "genial")
# 7. Define una variable texto="Hola mundo" y verifica si la palabra "mundo" está dentro usando "in".
texto="Hola mundo"
print(texto)
print("mundo" in texto)
# 8. Usa "not in" para verificar que la palabra "adios" NO está en la variable texto="Hola mundo".
print("No esta palabra adios:")
print("adios" not in texto)
# 9. Crea una variable saludo, asígnale un valor, luego elimínala con "del" y trata de imprimirla (observa qué pasa).
saludo="¡Hola!"
del saludo
#print(saludo) 
#Dara error si se intenta imprimir

# 10. Crea dos variables: una usando camelCase y otra usando snake_case, asígnales valores e imprímelas.
VariablesPerronas="CamelCase"
Snake_is_serpiente="Snake"

print(VariablesPerronas)
print(Snake_is_serpiente)

#Extra de concatenación

print(VariablesPerronas + Snake_is_serpiente + " concatenación de variables")
print(VariablesPerronas + " " + Snake_is_serpiente + " " +"concatenación de variables 2")