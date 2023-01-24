nombre_completo = input("Ingrese nombre completo:")
contador = len(nombre_completo)
agregar=""
#los strings no son mutables
#las listas son mutables
lista_nombre=[]
print(nombre_completo.lower())
print(nombre_completo.upper())
for i in range(contador): #range para que contador sea iterable porque sino me sale: TypeError: 'int' object is not iterable
    if (i==0):
       agregar2= nombre_completo[i].upper() 
       lista_nombre.append(agregar2)
    #if (nombre_completo[i]==" "):
    #    agregar3= nombre_completo[i+1].lower()
    #    lista_nombre.append(agregar3)
    
    if (nombre_completo[i]==" "):
        agregar= nombre_completo[i+1].upper() #PARA CORVACHO NO SIRVE PORQUE QUEDA Corvaho
        lista_nombre.append(" ")
        lista_nombre.append(agregar)
        #lista_nombre.remove()
    elif (nombre_completo[i]!=" " and nombre_completo[i-1]!=" " and i!=0): #increible lo hice
        agregar3= nombre_completo[i].lower()
        lista_nombre.append(agregar3)
    #print(i)
    #else:
     #   lista_nombre.append(" ")
    #print(nombre_completo[i])
#print(nombre_completo[0].upper())
#transformar la lista en string
        

Strnombre = "".join(lista_nombre)
print(Strnombre)