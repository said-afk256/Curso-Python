# 05/05/2026

# Usamos un bucle para la primera pregunta también
while True:
    try:
        # Cambiamos el mensaje para que sea más claro
        entrada = input("¿Quieres trabajar con enteros (inserta 1) o decimales (inserta 2)?: ")
        pregunta = int(entrada)
        
        # Validamos que solo sea 1 o 2
        if pregunta in [1, 2]:
            break
        else:
            print("Por favor, elige solo la opción 1 o 2.")
    except ValueError:
        print("Error: Debes ingresar un número entero (1 o 2), no puntos ni letras.")

if pregunta == 1:
    while True:
        try:
            numero = int(input("Ingresa un número ENTERO: "))
            resultado = numero * 2
            print(f"Resultado entero: {resultado}")
            break
        except ValueError:
            print("Error: Eso no es un número entero. Intenta de nuevo.")
else:
    while True:
        try:
            # Aquí float() sí aceptará el 1.27 sin problemas
            numero = float(input("Ingresa un número DECIMAL: "))
            resultado = numero * 2
            print(f"Resultado con decimal(float): {resultado:.2f}")
            break
        except ValueError:
            print("Error: Eso no es un número válido. Intenta de nuevo.")