opcion=""
codigo=[]
cantidad =[]
precio =[]
lista=[codigo,precio,cantidad] #lista de listas
while opcion!=5:
    print(" ")
    print("-----")
    print("Menu")
    print("-----")
    print("1) Ingresar nuevo producto:")
    print("2) Eliminar producto:")
    print("3) Modificar la cantidad de un producto determinado:")
    print("4) Modificar el precio de un producto determinado:")
    print("5) Finalizar")
    opcion=int(input("Ingrese una opción:"))
    if opcion==5:break
    elif opcion==1:
        cod=int(input("Ingrese el código del producto:"))
        codigo.append(cod)
        prec=int(input("Ingrese el precio del producto:"))
        precio.append(prec)
        cant=int(input("Ingrese una cantidad:"))
        cantidad.append(cant)
        for i in lista:
            print(i, end="-")
    
    elif opcion==2: # con pop
        cont=0
        cod=int(input("Ingrese el código del producto a eliminar:"))
        for i in codigo:
            if cod==codigo[cont]:
                codigo.pop(cont)
                precio.pop(cont)
                cantidad.pop(cont)
            cont+=1
    elif opcion==3:
        cont=0
        cod=int(input("Ingrese el código del producto:"))
        cant=int(input("Ingrese cantidad :"))
        for i in codigo:
            print("i",i)
            print("codigo",codigo)
            if cod==codigo[cont]: #i==codigo[cont]
                cantidad[cont]=cant
            cont+=1
    elif opcion==4:
        cont=0
        cod=int(input("Ingrese el código del producto:"))
        prec=int(input("Ingrese el precio:"))
        for i in codigo:
            if cod==codigo[cont]:
                precio[cont]=prec
            cont+=1        
    else:
        print("Ingrese una opción válida")