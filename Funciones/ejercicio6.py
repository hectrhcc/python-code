#Escriba una función que nos indique si una lista 
#se encuentra ordenada

def orden(x):
    y=sorted(x)
    z=sorted(x, reverse=True)
    if x==y or x==z:
        print("La lista esta ordenada")
    else:
        print("La lista esta desordenada")
        
lista = []
def Agregar(n):
    global men
    while n!=0:
        val=int(input("Ingrese valores en la lista:"))
        print("Para terminar ingrese 0")
        if val ==0:
            n=val
            print("Lista creada")
        else:
            lista.append(val)
            men=val
            n=val

print("Agregar elementos a la lista")
#llamada a la funcion
Agregar(lista)
print(lista)
if len(lista)!=0:
    orden(lista)
else:
    print("Ingrese mas valores a la lista")
