opcion=""
while opcion!=7:
    print("-------------")
    print("Menu Opciones")
    print("-------------")
    print("1) Pesos a Dolares ")
    print("2) Dolares a Pesos ")
    print("3) Pesos a Euros ")
    print("4) Euros a Pesos ")
    print("5) Pesos a Soles ")
    print("6) Soles a Pesos ")
    print("7) Finalizar")
    opcion = int(input("Ingrese una opcion:"))
    if opcion == 1:
        clp=float(input ("Ingrese cantidad en pesos:"))
        dolares= clp/821.23 # 821,23 TypeError: unsupported format string passed to tuple.__format__ 
        print("${0:,.2f} dolares".format(dolares))
    elif opcion == 2:
        usd=float(input ("Ingrese cantidad en dolares: "))
        clp= usd*821.23
        print("${0:,.2f} pesos" .format(clp))
    elif opcion == 3:
        clp=float(input ("Ingrese cantidad en pesos:"))
        euros= clp/915.79 
        print("${0:,.2f} euros".format(euros))
    elif opcion == 4:
        euros=float(input ("Ingrese cantidad en euros:"))
        clp= euros*915.79 
        print("${0:,.2f} pesos".format(clp))
    elif  opcion == 5:
        cpl=float(input ("Ingrese cantidad en pesos:"))
        soles= cpl/231
        print("${0:,.2f} soles".format(soles))

    elif  opcion == 6:
        soles=float(input ("Ingrese cantidad en soles:"))
        clp= soles*231
        print("${0:,.2f} pesos".format(clp))        
    elif  opcion == 7:
        break;
        print("Finalizar")
    else:
        print("\n Ingrese una opcion válida\n")
