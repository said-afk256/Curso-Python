# ==============================================================================
# MINIPROYECTO 4: SISTEMA DE MONITOREO INDUSTRIAL Y SEGURIDAD (Operadores Lógicos)
# ==============================================================================

# 1. CONTROL DE ALARMA DE TEMPERATURA Y PRESIÓN (Operador 'and' / 'or')
# Estás programando la lógica de seguridad para un compresor en tu sistema SCADA.
# La alarma de emergencia debe activarse (True) si la temperatura supera los 85°C 
# O si la presión supera los 120 PSI.
# Modifica las variables de prueba y escribe la condición lógica para 'activar_alarma'.
temperatura=90
psi=100

if temperatura>85 or psi>120:
    print("Activación de la alarma")
else:
    print("Alarma inactiva")

print()
# 2. VALIDACIÓN DE ACCESO DE DOBLE FACTOR (Operador 'and' y 'not')
# Para entrar al menú crítico del HMI, el usuario debe tener la tarjeta física insertada
# Y ADEMÁS el sistema NO debe estar en modo de mantenimiento.
# tarjeta_presente = True
# en_mantenimiento = False
# Escribe la expresión lógica que determine si 'acceso_concedido' es True o False.
tarjeta_presente= True
en_manternimiento= False

if tarjeta_presente==False or en_manternimiento==True:
    print("Entrada al menu HMI denegada")
else:
    print("Acceso al menu autorizado")
    
print()

# 3. VERIFICACIÓN DE RANGO SEGURO DE OPERACIÓN (Operadores compuestos)
# Un motor terapéutico debe operar únicamente en un rango seguro de frecuencia:
# Debe ser mayor o igual a 20 Hz Y menor o igual a 60 Hz.
# Pide al usuario la frecuencia con un 'input()', conviértela a flotante de forma segura 
# con 'try...except', y evalúa si está dentro del rango seguro usando 'and'.
try:
    frecuencia=input("Ingrese la frecuencia del motor (Hz):")

except:
    frecuencia=1


# ------------------------------------------------------------------------------
# EJERCICIO PARA TRABAJAR (Copia y completa):
# ------------------------------------------------------------------------------

# --- TAREA 1: Alarma del Compresor ---
# temperatura_actual = 90.5
# presion_actual = 115.0
# activar_alarma = 

# --- TAREA 2: Acceso al HMI ---
# tarjeta_presente = True
# en_mantenimiento = False
# acceso_concedido = 

# --- TAREA 3: Rango de Frecuencia del Motor ---
# while True:
#     try:
#         frecuencia = float(input("Ingrese la frecuencia de prueba del motor (Hz): "))
#         # Evalúa aquí si está en el rango [20.0, 60.0]
#         es_rango_seguro = 
#         break
#     except ValueError:
#         print("Error: Ingrese un valor numérico válido.")

# ------------------------------------------------------------------------------
# MOSTRAR RESULTADOS (Usa f-strings):
# ------------------------------------------------------------------------------
# print(f"¿Alarma de emergencia activada?: {activar_alarma}")
# print(f"¿Acceso concedido al menú crítico del HMI?: {acceso_concedido}")
# print(f"¿La frecuencia {frecuencia} Hz está dentro del rango seguro?: {es_rango_seguro}")
# ==============================================================================