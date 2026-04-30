ingreso_mensual= 1110
gasto_mensual=1000

#if anidado y else if

#If anidado
if ingreso_mensual>10000:#Esta es la primera condición, que si se cumple, pasa al if anidado
    if ingreso_mensual-gasto_mensual < 0: #Si esta resta da negativo, se activa el código de este if y se acaba la secuencia
        print("Estas gastando de más de lo que tienes, estas en deficit")
    elif ingreso_mensual-gasto_mensual < 5000:#Si la condición es mayor de cero pero es menor que 5000, se activa este else if(elif)
        print("Estas gastando una banda")
    else:#En caso de no activarse ninguna condición anterior, se activa el código de este else
        print("Ganas y ahorras muy bien")
        
#elif normal(sin if anidado)
elif ingreso_mensual>5000:
    print("Ganas bien para vivir en latinoamerica :)/! ")

elif ingreso_mensual>1000:
    if ingreso_mensual-gasto_mensual < 0:
        print("Ganas para vivir en Argentina o Venezuela, PERO gastas mas de lo que tienes, ya le debes al banco chaval")
    elif ingreso_mensual-gasto_mensual > 300:
        print("Vivis muy bien para Argentina y Venezuela loco")
    else:
        print("Puedes vivir en Argentina o Venezuela, Pero gastas mucho, cuidao")
else:
    print("Vivis en la calle")

print("Nuevo mensajeee")