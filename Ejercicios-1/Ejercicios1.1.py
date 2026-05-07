#Duraciones de los cursos

tiempo_minimo=2.5
tiempo_maximo=7
tiempo_este_curso=1.5
tiempo_promedio=4

crudo_este_curso=3.5
crudo_otro=5

#Diferencia en porcentaje entre el curso actual y el mas rapido
Porcentaje_rapido=tiempo_este_curso/tiempo_minimo*100

#Diferencia en porcentaje entre el curso actual y el mas lento

Porcentaje_lento=tiempo_este_curso/tiempo_maximo*100

#Diferencia en porcentaje entre el curso actual y el promedio
Porcentaje_promedio=tiempo_este_curso/tiempo_maximo*100

print(Porcentaje_rapido)
print(Porcentaje_lento)
print(Porcentaje_promedio)

#Porcentaje de material inservible que se reduce en:
#El promedio de los cursos
#El curso actual

#Duraciones de los cursos
#Ver 10 horas de este curso a cuantas de otros cursos equivale? 2.-¿y al revés?

#Duraciones de los cursos

#1

diez_horas=10
equivalencia=(crudo_otro/crudo_este_curso)
equivalencia_final=equivalencia*10
print(f"10 horas del curso de Dalto equivalen en otro curso a {equivalencia_final} horas")
print()

#2
diez_horas=10
equivalencia=(crudo_este_curso/crudo_otro)
equivalencia_final=equivalencia*10
print(f"10 horas de otros cursos equivalen a {equivalencia_final} horas del curso de Dalto")
print()
