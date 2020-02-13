#import math
# from sympy import prime
# import sympy

#print("5x^2+5")h
formula = str(input("formula: "))
a = int(input("Comienzo: "))
b = int(input("Fin: "))
print("\n Evaluando en: ", formula)
for i in range (a, (b+1)):
    x= ( 5*(i**2)+5*i )
    print("Con",(i ), "=",(x))


# funciones trigonometricas
# con modulo "math"
import math
a=int(input("Cominenza: "))
b=int(input("Fin: "))
for x in range (a,(b+1)):
    y = math.cos(x)+1
    print (y)