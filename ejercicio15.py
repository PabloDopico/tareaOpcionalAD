num1=int(input ("Ingrese primer valor: "))
num2=int(input ("Ingrese segundo valor: "))
num3=int(input ("Ingrese tercer valor: "))
print ("El valor mayor de los tres valores ingresados es")
if num1>num2:
    if num1>num3:
        print (num1)
    else:
        print (num3)
else:
    if num2>num3:
        print (num2)

    else:
        print (num3)
