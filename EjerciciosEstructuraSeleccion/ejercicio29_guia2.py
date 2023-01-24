num = int(input(" Ingrese un numero de 4 digitos: "))

if 9<num<100:
    decena= int((num % 100)/10)
    unidad= num % 10
    if decena == unidad:
        print("El numero ingresado es un palindromo")

if 99<num<1000:
    centena= int((num % 1000)/100)
    decena= int((num % 100)/10)
    unidad= num % 10
    if centena == unidad:
        print("El numero ingresado es un palindromo")
        
if 999<num<10000:
    unidadmil = int(num/1000) # PRIMER DIGITO
    centena= int((num % 1000)/100) # SEGUNDO DIGITO
    decena= int((num % 100)/10) # TERCER DIGITO
    unidad= num % 10 # CUARTO DIGITO
    #print("1000",unidadmil)
    #print("100", centena)
    #print("10", decena)
    #print("1", unidad)
    if unidadmil == unidad and centena == decena:
        print("El numero ingresado es un palindromo")
    else:
        print("El numero ingresado no es un palindromo")
else:
    print("Ingrese un numero de 4 digitos") 