#Con ayuda de ia para resolverlo
# 07/05/2026
# Datos
tiempo_minimo = 2.5
tiempo_maximo = 7
tiempo_promedio = 4
tiempo_este_curso = 1.5

crudo_otro = 5
crudo_este_curso = 3.5

# Diferencias (Cuánto % MENOS tiempo duran)
# Fórmula: 100 - (este / otro * 100)
dif_con_min = 100 - (tiempo_este_curso / tiempo_minimo * 100)
dif_con_max = 100 - (tiempo_este_curso / tiempo_maximo * 100)
dif_con_promedio = 100 - (tiempo_este_curso / tiempo_promedio * 100)

print(f"El curso es un {dif_con_min:.1f}% más rápido que el más rápido.")
print(f"El curso es un {dif_con_max:.1f}% más rápido que el más lento.")
print(f"El curso es un {dif_con_promedio:.1f}% más rápido que el promedio.")

# Reducción de material inservible (Tiempo vacío o crudo)
# Calculamos cuánto tiempo se quitó en la edición
reduccion_promedio = 100 - (tiempo_promedio / crudo_otro * 100)
reduccion_este_curso = 100 - (tiempo_este_curso / crudo_este_curso * 100)

print(f"\nMaterial inservible eliminado:")
print(f"En promedio: {reduccion_promedio:.1f}%")
print(f"En este curso: {reduccion_este_curso:.1f}% (¡Mucho más editado!)")

# Equivalencias
equivalencia_otros = (crudo_otro / crudo_este_curso) * 10
equivalencia_este = (crudo_este_curso / crudo_otro) * 10

print(f"\nEquivalencias de 10 horas:")
print(f"10h de este curso equivalen a {equivalencia_otros:.1f}h de otros.")
print(f"10h de otros cursos equivalen a {equivalencia_este:.1f}h de este.")     