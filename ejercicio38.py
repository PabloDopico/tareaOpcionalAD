﻿pares=0
impares=0
x=1
n=int(input("Cuantos numeros ingresara:"))
while x<=n:
    valor=int(input("Ingrese el valor: "))
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
    x=x+1
print("Cantidad de pares")
print(pares)
print("Cantidad de impares")
print(impares)
