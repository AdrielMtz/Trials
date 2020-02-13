
#pide "x" palabras
#ordena alfabeticamente
#hacia abajo como str
l = []
A = int(input("Veces: "))
for a in range (0, (A)):
    num = str(input("Palabra: "))
    y = "\n"
    l.append(num)
    l.sort()
    x=y.join(l)
print (x)