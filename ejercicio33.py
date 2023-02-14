suma=0
x=1
n=int(input("Cuantas personas va a procesar:"))
while x<=n:
    altura=float(input("Ingrese la altura:"))
    suma=suma+altura
    x=x+1
promedio=suma/n
print ("Altura promedio")
print(promedio)
