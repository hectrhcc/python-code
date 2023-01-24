lista1 = []#[44, 33, 22, 87, 12, 21, 3, 11]
lista2 = []#[44, 22, 33, 87, 12, 21, 3, 11]
def FuncionListas(listax,listay):
    if ((len(lista1) == len(lista2)) and (all(i in lista2 for i in lista1))):
       print('Son iguales en contenido')
        #return True
    else:
       print('Son distintas en contenido')
        #return False
    
def Agregar():
    global elem1
    global elem2
    elem1=int(input("Agregue elementos de la lista1:"))
    lista1.append(elem1)
    elem2=int(input("Agregue elementos de la lista2:"))
    lista2.append(elem2)
    while elem1!=0 or elem2!=0:
        elem1=int(input("Agregue elementos de la lista1:"))
        if elem1==0:
            print("Lista llena")
        else:
            lista1.append(elem1)
        elem2=int(input("Agregue elementos de la lista2:"))
        if elem2==0:
            print("Lista llena")
        else:
            lista2.append(elem2)
        print("Para terminar ingrese 0:")
print(Agregar())
print("Lista 1 :",lista1)
print("Lista 2:",lista2)
FuncionListas(lista1,lista2)
    