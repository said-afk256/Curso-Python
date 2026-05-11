#Como lo resolvio Dalto

#Promedio de duración

otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
dalto_curso=1.5

#Duración de crudos
crudo_promedio=5
crudo_dalto=3.5

#Diferencias de duración

diferencia_con_min=100-(dalto_curso/otros_cursos_min*100)
diferencia_con_max=100-dalto_curso*1000//otros_cursos_max/10
diferencia_con_promedio=100-dalto_curso/otros_cursos_promedio*100

#Mostrando las diferencias de duración (ejercicio A)
print("El curso de Dalto dura:")
print(f" - un {diferencia_con_min}% menos que el curso mas rapido")
print(f" - un {diferencia_con_max}% menos que el curso mas lento")
print(f" - un {diferencia_con_promedio}% menos que el curso promedio")
print("---")

#Calculando el tiempo vacio removido

tiempo_vacio_promedio=100-otros_cursos_promedio/crudo_promedio*100
tiempo_vacio_dalto=100-dalto_curso/crudo_dalto*100

#Mostrando el tiempo crudo removido (ejercicio B)
print(f"Un curso promedio remueve un {tiempo_vacio_promedio:.2f}% de tiempo crudo en sus videos")
print(f"El curso de Dalto se remueve un {tiempo_vacio_dalto:.2f}% de tiempo crudo en sus videos")
print("---")

#Mostrando las diferncias si los cursos duraran 10 horas (ejercicio C)
print(f"Ver 10 horas de este curso equivale a {otros_cursos_promedio/dalto_curso*10:.2f} hora en otro curso")
print(f"Ver 10 horas de otro curso equivale a {dalto_curso/otros_cursos_promedio*10:.2f} horas en el de Dalto")
