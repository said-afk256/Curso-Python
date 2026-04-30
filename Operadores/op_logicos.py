#Operadores Logicos AND OR NOT
#Se pueden usar en condicionales para activar códigos si se cumplen con los True o False

#And
#Solo cuando las 2 condiciones o mas condiciones sean "True", El resultado se ejecutara o dara True
resultado1=True and True
resultado2=False and True
resultado3=True and False
resultado4=False and False

#OR
#Cuando una sola condición se cumpla de 2 o mas condiciones, El resultado se ejecutara o dara True
resultado5=True or True
resultado6=False or True
resultado7=True or False
resultado8=False or False

#not
#Invierte o niega el resultado original, True->False y False->True
resultado9= not True #False
resultado10=not False #True

print(f"Resultado 1: {resultado1}")
print(f"Resultado 2: {resultado2}")
print(f"Resultado 3: {resultado3}")
print(f"Resultado 4: {resultado4}")
print(f"Resultado 5: {resultado5}")
print(f"Resultado 6: {resultado6}")
print(f"Resultado 7: {resultado7}")
print(f"Resultado 8: {resultado8}")
print(f"Resultado 9: {resultado9}")
print(f"Resultado 10: {resultado10}")
#Operador Bit a Bit (bitwise)
resultado1= True | True 
print(resultado1)
#True=1
#1|1=1 True

resultado2= True or True
print(resultado2)
#True or True= True

print(5|3)#El "|" Compara números binarios, 1=True 0=False, si funciona con True y False es por que los transforma a bits de 1 y 0
#por lo que si, 5 en binario es 0101, 3 en binario es 0011, el resultado es la comparación de cada bit que da 0111 que es 7 en binario
"""F T T T
   0 1 0 1
   0 0 1 1
   Por lo que F=0 y T es 1,
   el resultado de la comparación es 0111 que es 7 en binario
   Por eso da ese resultado"""