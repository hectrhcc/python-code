lista = []
n=int(input("Ingrese la cantidad de elementos de la lista:"))
cont3=0
cont5=0
for i in range(0,n):
	x=int(input("Ingrese un numero:"))
	lista.append(x) # lista[i]=x

for i in lista:
	if i % 3==0:
            cont3+=1
	if i % 5==0:
            cont5+=1

print("N° total de multiplos de 3 en la lista:",cont3)
print("N° total de multiplos de 5 en la lista:",cont5)