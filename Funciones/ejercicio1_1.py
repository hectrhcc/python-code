#Escriba una función que reciba una lista de rut y un rut y determine 
#si el rut pertenece a la lista si está en la lista retorne la posición
#en la lista en caso contrario un -1.
pos = 0
cont=0
def lafuncion(listarut,rut):
    global pos
    global cont
    for i in listarut:
        if i==rut:
            cont=1
            index=pos
        pos+=1
    if cont==1:
        return index
    else:
        return -1

lista = []
def Llenarlista():
    print("Ingese valor 0 para terminar")
    elem=input("Ingrese rut en la lista:")
    lista.append(elem)
    while elem!='0':
        print("Ingese valor 0 para terminar")
        elem=input("Ingrese rut en la lista:")
        if elem=='0':
            print("lista creada")
        else:
            lista.append(elem)
    rut=input("Ingrese un rut:")
    return rut

rut=Llenarlista()
print("La lista:",lista)
print("Rut ingresado:",rut)
print("Resultado:", lafuncion(lista,rut))