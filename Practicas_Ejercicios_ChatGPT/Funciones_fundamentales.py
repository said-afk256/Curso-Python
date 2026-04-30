# ==============================================================================
# RETOS DE PROGRAMACIÓN: ESCRIBE TU PROPIO CÓDIGO
# ==============================================================================
# INSTRUCCIONES:
# 1. Debajo de cada comentario, escribe el código que resuelva el problema.
# 2. No olvides definir las variables necesarias.
# 3. Usa print() para comprobar que tu solución funciona.
# ==============================================================================

# --- SECCIÓN 1: VARIABLES Y ARITMÉTICA ---

# Ejercicio 1:
# Crea una variable 'grados_celsius' con el valor 25. 
# Calcula la conversión a Fahrenheit usando la fórmula: (Celsius * 9/5) + 32.
# Guarda el resultado en 'grados_fahrenheit'.
grados_celsius=25
grados_fahrenheit=(grados_celsius*9/5)+32
print(f"Ejercicio 1: {grados_fahrenheit}")

# Ejercicio 2:
# Tienes una capacidad de 17 litros y envases de 3 litros. 
# Usa el operador de división entera (//) para ver cuántos envases llenas 
# y el operador residuo (%) para ver cuántos litros sobran.
envases_llenos=17//3
litros_sobrantes=17%3
print(f"Ejercicio 2: Con 17 litros llenamos {envases_llenos} envases de 3 litros, y nos sobra {litros_sobrantes} litros")


# Ejercicio 3:
# Calcula el sueldo semanal de un operario. 
# Trabaja 40 horas a una tasa de 15.5 dólares la hora.
sueldo_semanal=40*15.5
print(f"Ejercicio 3: El operario gana a la semana {sueldo_semanal} dolares")

# --- SECCIÓN 2: DATOS COMPUESTOS (LISTAS/DICT) ---

# Ejercicio 4:
# Crea una lista llamada 'colores' con: "rojo", "azul", "verde".
# Añade "amarillo" al final y luego cambia "azul" por "cian".
colores=["rojo", "azul", "verde"]
colores[2]="cian"#necesite de ayuda
colores.append("amarillo")#También necesite de ayuda
print(f"Ejercicio 4: {colores}") #Para toda la lista se pone nada mas el nombre de la variable
#Para un elemento especifico se usa el corchete "colores[Num.Indice]"
#Necesite ayuda por que puse "colores[]" y no era asi


# Ejercicio 5:
# Crea un diccionario llamado 'sensor' que tenga las llaves: 
# "tipo" (valor: "temperatura"), "valor" (valor: 22.5) y "unidad" (valor: "C").
sensor={"tipo": "Temperatura",
        "valor":22.5,
        "unidad":"C"}
print(f"Ejercicio 5: Diccionario: {sensor}")

#Extra de Gemini
# 2. Accedemos a un dato específico (opcional, para comprobar)
#print(f"El sensor detecta: {sensor['tipo']}")
#print(f"Lectura actual: {sensor['valor']} {sensor['unidad']}")

# Ejercicio 6:
# Tienes la lista [10, 20, 30, 40]. Suma el primer elemento con el último 
# usando sus índices y guarda el resultado en 'suma_extremos'.
Lista_numeros=[10, 20, 30, 40]
suma_extremos=Lista_numeros[0] + Lista_numeros[3]#50
print(f"Ejercicio 6: Suma del primer elemento de la lista con el ultimo: {suma_extremos}")#Esta correcto


# --- SECCIÓN 3: CONDICIONALES Y COMPARACIÓN ---

# Ejercicio 7:
# Define 'puntuacion = 85'. Si la puntuación es mayor a 80, 
# imprime "Nivel Avanzado", de lo contrario imprime "Nivel Estándar".
puntuacion= 85
if puntuacion>80:
    print("Ejercicio 7: ")
    print("Nivel Avanzado")
else:
    print("Ejercicio 7: ")
    print("Nivel Estándar")

# Ejercicio 8:
# Verifica si un número es par Y positivo al mismo tiempo usando un solo IF.
numero=10
print("Ejercicio 8:")
if numero%2==0 and numero>0 : #Solo necesite ayuda para el numero par, original: if numero/2= int
#En este caso se utiliza "numero%2==0" por que el % saca el residual de un número, por lo que usando la logica,
#Si un numero no tiene residuo cuando se divide entre 2, significa que es un número par
#El "numero>0" que yo puse, es por que si un número es mayor a 0, este sera positivo
#El "and" es para que se cumpliera ambas condiciones si o si
    print(f"El número: {numero} es par y positivo")
else:
    print(f"El número: {numero} es impar y/o negativo")

# Ejercicio 9:
# Crea un sistema de acceso. Si 'usuario' es "admin" y 'password' es "1234",
# guarda "Acceso concedido" en una variable, si no, guarda "Acceso denegado".
usuario="admin"
password="1234"
print("Ejercicio 9: ")
#El ejercicio se refiere a que se resuelva de esta manera usando if y comparadadores logicos
if usuario=="admin" and password=="1234":
    acceso="Acceso concedido"
    print(acceso)
else:
    acceso="Acceso denegado"
    print(acceso)


# --- SECCIÓN 4: COMBINADOS (EL DESAFÍO) ---

# Ejercicio 10:
# Tienes una lista de compras: ["pan", "leche", "huevos"].
# Si "leche" está en la lista Y el tamaño de la lista es igual a 3, 
# imprime "Lista lista", si no, imprime "Faltan cosas".
compras=["pan", "leche", "huevos"]
print("Ejercicio 10: ")
if "leche" in compras and len(compras)==3: #Nueva funcion: "len(Lista que queremos comparar)" nos sirve para contar la cantidad total de elementos en la lista
    print("La lista esta lista")#Nota: Recuerda siempre que si queremos consultar la lista completa, solo se pone el nombre de la variable sin los corchetes, que me volvio a pasar al intentar usar in con compras y me daba un error de sitaxis
else:
    print("Le falta cosas a la lista")

# Ejercicio 11:
# Un auto recorre 300km con 20 litros. Calcula el consumo (km/l).
# Si el consumo es mayor a 12 km/l, guarda "Económico", si no "Gastalon". #Entre mas kilometros, mejor, ya que eso significa que avanza mas kilomentros con un solo litro de gasolina
km_carro= 300
litros_carro= 20
consumo=km_carro/litros_carro
print("Ejercicio 11: ")
if consumo>12:
    print(f"Es un carro economico, su consumo es de {consumo}km/L")
else:
    print(f"Es un carro gastador, su consumo es de {consumo}km/L")


# Ejercicio 12
# Tienes un diccionario: producto = {"nombre": "PLC", "stock": 5}.
# Si el stock es mayor a 0, resta 1 al stock e imprime "Venta realizada".
# Si el stock es 0, imprime "Sin inventario".
producto = {"nombre": "PLC", "stock": 5}
print("Ejercicio final 12: ")

if producto["stock"]>0:
    producto["stock"]-=1 #El -1 como indice sirve para tomar el ultimo número de la lista y asi no contar todo por si acaso
    print(f"Venta realizada, Stock Restante: {producto['stock']}")
else:
    print(f"Sin inventario, Stock: {producto['stock']}")
#Correciones: <0 pequeño fallo, solución: >0
#Correciones: productos[-1], olvide que es un diccionario, osea, sus "keys" pueden ser strings, 
#como lo fue en este caso, además, en vez de usar -1, es mejor -=1, ya que usaremos un valor ya existente para hacer uno de estos tipos de operación
#Solución: producto[stock]-=1
#Fallo -1 punto
print()
print("Puntacion:9/10")

# ==============================================================================
# RESPUESTAS PARA CORROBORAR (¡No las mires hasta terminar!)
# ==============================================================================
# 1. fahrenheit = 77.0
# 2. envases = 5, sobra = 2
# 3. sueldo = 620.0
# 4. colores = ['rojo', 'cian', 'verde', 'amarillo']
# 5. sensor['valor'] -> 22.5
# 6. suma_extremos = 50 (10 + 40)
# 7. Imprime "Nivel Avanzado"
# 8. (num % 2 == 0) and (num > 0)
# 9. Depende de los valores que elijas.
# 10. Imprime "Lista lista"
# 11. consumo = 15.0 -> "Económico"
# 12. stock final = 4 -> "Venta realizada"