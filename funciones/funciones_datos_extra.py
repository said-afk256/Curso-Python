#23/06/2026

#Función frase con 3 parametros
#def frase(nombre, apellido, adjetivo):#Parametros posicionales
#    return f" Hola {nombre} {apellido}, hoy estas muy {adjetivo}"

#Parametros mediante asignación (Parametros KEYWORD[palabra clave])
#frase_res=frase(adjetivo="Piano embrujado", nombre="Lucas", apellido="Dalto")#Se tiene que asignar a todos por variables cuando se hace por asignación
#print(frase_res)

#En orden
#frase_res=frase("Lucas", "Dalto", "helicoptero")
#print(frase_res)

#Creando función con parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo="Tonto"):
    return f" Hola {nombre} {apellido}, hoy estas muy {adjetivo}"

frase_res=frase("Lucas","Dalto", "Inteligente")#o adjetivo="Inteligente"
print(frase_res)