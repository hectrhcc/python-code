#Escriba una función que encuentre el menor valor de una lista.

def menor(x):
    global men
    for i in x:
        if i<men:
            men=i
    return men

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
    print("El menor valor de la lista es", menor(lista))
else:
    print("Ingrese mas valores a la lista")


