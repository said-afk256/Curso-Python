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