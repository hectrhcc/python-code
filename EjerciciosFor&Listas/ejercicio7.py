lista1= []
lista2= []
lista_sum = []
lista_res = []
lista_multi = []
n=int(input("Ingrese la cantidad de elementos de la lista 1:"))
for i in range(0,n):
	x=int(input("Ingrese un numero:"))
	lista1.append(x) # lista[i]=x
k=int(input("Ingrese la cantidad de elementos de la lista 2:"))
for i in range(0,k):
	x=int(input("Ingrese un numero:"))
	lista2.append(x) # lista[i]=x
print("========")
print(" M E N U")
print("========")
print("0) Ver listas")
print("1) Suma de listas")
print("2) Resta de listas")
print("3) Multiplicacion de listas")
print("4) Finalizar ")
opcion=int(input("Ingrese una opción:"))
while (opcion>=0 and opcion<5) or opcion!=4:
    if opcion==4:break
    elif opcion==0:
        print("Lista 1:", lista1)
        print("Lista 2:", lista2)
    elif opcion==1:
        #print("Suma de listas:",lista1+lista2 ) Concatena 2 listas
        lista_sum = [a+b for a,b in zip(lista1, lista2)]
        print("Suma de listas:",lista_sum )
    elif opcion==2:
        lista_res = [a-b for a,b in zip(lista1, lista2)]
        print("Resta de listas:",lista_res )	#list(map(int.__sub__, lista1, lista2))
    elif opcion==3:
        #Ciclo for junto a zip (compresión de listas):
        lista_multi = [a*b for a,b in zip(lista1, lista2)]
        print("Multiplicación de listas:", lista_multi)	
    else:
        print("opción inválida, intente de nuevo")
    opcion=int(input("Ingrese una opción:"))