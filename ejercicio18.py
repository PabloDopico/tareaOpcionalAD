total_preguntas=int(input("Ingrese el total de preguntas: "))
total_correctas=int(input("Ingrese la cantidad de preguntas correctas: "))
porcentaje=total_correctas * 100 / total_preguntas
if porcentaje>=90:
    print ("nivel máximo")
else:
    if porcentaje>=75:
        print ("Nivel medio")
    else:
        if porcentaje>=50:
            print ("Nivel regular")
        else:
            print ("Fuera de nivel")
