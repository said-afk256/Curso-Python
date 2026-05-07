# ==============================================================================
# MINIPROYECTO: ANALIZADOR DE EFICIENCIA EN CASCADA
# ==============================================================================

# DATOS INICIALES (Tiempos de llenado en minutos)
tiempo_sistema_viejo = 12.5
tiempo_sistema_estandar = 8.0
tiempo_tu_sistema_optimizado = 4.5

# DATOS DE VOLUMEN (Litros)
volumen_inicial_cisterna = 1000
volumen_final_tinaco_promedio = 850   #(lo que llega después de pérdidas)
volumen_final_tinaco_tu_sistema = 960 #(tu sistema es más eficiente)

# ------------------------------------------------------------------------------
# TAREAS A REALIZAR:
# ------------------------------------------------------------------------------

# 1. Calcular la diferencia porcentual de TIEMPO entre:
#    a) Tu sistema y el viejo.
diferencia_con_viejo = 100 - (tiempo_tu_sistema_optimizado / tiempo_sistema_viejo * 100)
print(f"La diferencia porcentual de tiempo de mi sistema con el viejo es del {diferencia_con_viejo:.1f}%")
#    b) Tu sistema y el estandar.
diferencia_con_estandar= 100-(tiempo_tu_sistema_optimizado/tiempo_sistema_estandar*100)
print(f"La diferencia porcentual de tiempo de mi sistema con el estandar es del {diferencia_con_estandar:.1f}%")
#    (Fórmula sugerida: 100 - (tiempo_tu_sistema / tiempo_otro * 100))
print()

# 2. Calcular el porcentaje de "Pérdida de Agua" en:
#    a) El sistema promedio.
perdida_promedio= 100-(volumen_final_tinaco_promedio/volumen_inicial_cisterna*100)
print(f"La perdida de agua en el sistema promedio es del {perdida_promedio:.1f}%")
#    b) Tu sistema optimizado.
perdida_sistema_optimizado=100-(volumen_final_tinaco_tu_sistema/volumen_inicial_cisterna*100)
print(f"La perdida de agua en el sistema optimizado es del {perdida_sistema_optimizado:.1f}%")
#    (Fórmula sugerida: 100 - (volumen_final / volumen_inicial * 100))
print()

# 3. Equivalencia de Eficiencia:
#    Si dejas funcionando tu sistema por 60 minutos... 
#    ¿A cuántos minutos de funcionamiento del "sistema viejo" equivaldría en 
#    términos de agua movida?
equivalencia_viejo=(tiempo_sistema_viejo/perdida_sistema_optimizado*60)
equivalencia_viejo_hora=(tiempo_sistema_viejo/perdida_sistema_optimizado)
print(f"""Si dejamos los sistemas funcionando 1 hora completa, los minutos del sistema viejo
en el nuevo serian equivalentes a {equivalencia_viejo:.1f} minutos o a {equivalencia_viejo_hora:.1f} horas""")
# ------------------------------------------------------------------------------
# RESULTADOS ESPERADOS (Ejemplo de salida):
# ------------------------------------------------------------------------------
# Tu sistema es un 64.0% más rápido que el sistema viejo.
# Tu sistema es un 43.8% más rápido que el sistema estándar.
#
# Pérdida de agua:
# Sistema promedio: 15.0%
# Tu sistema: 4.0%
#
# 60 min de tu sistema equivalen a X.X min del sistema viejo.
# ==============================================================================