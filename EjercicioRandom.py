#03/06/2026


# ==============================================================================
# MINIPROYECTO 3: CONTROL DE ACCESO Y CONFIGURACIÓN DE DISPOSITIVOS (PLCs)
# ==============================================================================

# 1. VERIFICACIÓN DE IP ÚNICA EN LA RED (Sets)
# Estás configurando las direcciones IP de tres PLCs en la red de tu planta.
# Tienes un conjunto con las IPs que ya están ocupadas: ips_ocupadas = {"192.168.1.10", "192.168.1.11"}
# El sistema intenta asignar un nuevo conjunto de IPs para los sensores: ips_nuevas = {"192.168.1.12", "192.168.1.13"}
# Usa la función '.isdisjoint()' para verificar si las 'ips_nuevas' están completamente libres 
# (es decir, que no tengan ningún elemento en común con 'ips_ocupadas').
ips_ocupadas={"192.168.1.10", "192.168.1.11"}
ips_nuevas={"192.168.1.12", "192.168.1.13"}

print(f"Ejercicio 1: Las ips nuevas estan completamente libres: {ips_nuevas.isdisjoint(ips_ocupadas)}")
print()

# 2. SISTEMA DE SEGURIDAD Y DESEMPAQUETADO DE CREDENCIALES
# Para registrar un operador en el HMI, recibes sus datos en una lista fija:
# operario = ["Said", "Ingeniero", "Nivel_3"]
# Desempaqueta esta lista en tres variables: nombre, puesto y nivel_acceso.
# Luego, usando un condicional 'if', verifica si el 'nivel_acceso' es igual a "Nivel_3".
# Si lo es, asigna a la variable 'permiso' el valor "Acceso Total a Calibración", de lo contrario, "Acceso Restringido".
operario = ["Said", "Ingeniero", "Nivel_3"]

nombre, puesto, nivel_acceso=operario
print("Ejercicio 2:")
if nivel_acceso == "Nivel_3":
    permiso="Acceso total a calibración"
    print(f"Permiso: {permiso}")
else:
    permiso="Acceso restringido"
    print(permiso)

print()
    
# 3. CONVERSIÓN SEGURA DE PARÁMETROS CRÍTICOS (Try...Except)
# El HMI envía la frecuencia para un variador de velocidad como un texto. Si el operador
# escribe una coma en lugar de un punto (ej. "50,5"), float() fallará.
# Crea un bucle 'while True' que pida la frecuencia
