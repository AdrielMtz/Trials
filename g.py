#muestra secuencia fibonacci
import math

a = int(input("Comienzo: "))
b = int(input("Fin: "))

f= (1 + (math.sqrt(5)) ) / 2

for n in range (a, b):
    num = (f**n-((-f)**(-n)))/(math.sqrt(5))
    print(int(num))


# secuencia desde el cero
b = int(input("Cantidad de #´s: "))

f= (1 + (math.sqrt(5)) ) / 2

for n in range (0, b):
    num = (f**n-((-f)**(-n)))/(math.sqrt(5))
    print(int(num))
