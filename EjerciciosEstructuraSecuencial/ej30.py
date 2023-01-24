numero3 = int(input("Ingresar un numero de 3 digitos"))
#347  -> 743
if (numero3>99):
    centena = int (numero3 /100)
    
    decena = int ( (numero3 % 100)/10  )
    
    unidad = int (numero3 % 10)

    #print("centena ", centena )
    #print("decena ", decena)
    #print("unidad ", unidad)
    numero_invertido =  unidad*100 + decena *10 + centena
    print("El numero invertido es: ", numero_invertido ) 

else:
    print("Ingrese un numero de 3 digitos")





        