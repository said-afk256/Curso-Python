#Estructura
#if condicion:
    #accion se ejecuta

edad=17
if edad >= 18:
    print("Puedes pasar")
    print("Forma parte del if")
    #para poder salir de la condicional, debemos de salir de la sangria del if
    #En esta linea seguimos dentro
#Aqui ya estoy fuera
else:
    print("No puedes pasar")
    print("Esto forma parte del else")
    
print("Esta linea de texto se ejecutara de igual manera por no tener ninguna condicional")

Contraseña_almacenada="1234"
Contraseña_escrita="1234"

if Contraseña_escrita == Contraseña_almacenada:
    print("Contraseña correcta, INICIANDO SESIÓN")
    
else:
    print("Contraseña incorrecta, Intente de nuevo")