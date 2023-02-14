num=int(input("Ingrese un numero positivo entre 1 y 999:"))
if num<10:
    print ("Tiene un digito")
else:
    if num<100:
        print ("Tiene 2 digitos")
    else:
        if num<1000:
            print ("Tiene 3 digitos")
        else:
            print("Error en la entrada de datos")
print ("Fin del programa")
