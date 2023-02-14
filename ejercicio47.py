n=int(input("Cuantos triangulos procesara:"))
cantidad=0
for f in range(n):
    base=int(input("Ingrese el valor de la base:"))
    altura=int(input("Ingrese el valor de la altura:"))
    superficie=base * altura / 2;
    print("superficie")
    print(superficie)
    if superficie>12:
        cantidad=cantidad+1
print("Cantidad de triangulos con superficie mayor a 12")
print(cantidad)
