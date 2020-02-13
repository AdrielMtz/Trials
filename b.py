
#pide 10 numeros
#da su promedio
#ordena los numeros pedidos
l = []
for a in range (0, 10):
    num = int(input("numero: "))
    l.append(num)
    x=sorted(l)
print ("Promedio: ", sum(l)/len(l))
print (x)


#pide 10 palabras
#ordena alfabeticamente
#imprime dentro de lista
l = []
for a in range (0, 10):
    num = str(input("Palabra: "))
    l.append(num)
    x=sorted(l)
print (x)