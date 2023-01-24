numero_entrada = int ( input("Ingrese un numero de 3 digitos:" ))
if (numero_entrada >99):

    primer_digito = numero_entrada % 10
    segundo_digito = int (((numero_entrada % 100)/10))
    tercer_digito = int (numero_entrada / 100)
#print(primer_digito)
#print(segundo_digito)
#print(tercer_digito)
    numero_salida = primer_digito *100 + segundo_digito*10 + tercer_digito
    print("El numero invertido es: ", numero_salida)
else:
    print("El numero ingresado no es de 3 digitos")