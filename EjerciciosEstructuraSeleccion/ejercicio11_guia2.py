num = int(input("Ingrese un numero de 4 digitos: "))

if num <1000: # Si ingresa un n° menor que 4 digitos o es negativo entonces
    print("Le dije que ingrese un numero de 4 digitos")
elif num >9999: # Si ingresa un n° mayor que 4 digitos
    print("Le dije que ingrese un numero de 4 digitos")
else:
    unidadmil = int (num/1000)
    centena = int((num % 1000)/100)
    decena = int((num % 100)/10)
    unidad = (num % 10)
    #print(unidadmil)
    #print(centena)
    #print(decena)
    #print(unidad)
    suma = unidadmil+ centena + decena + unidad
    if suma % 2 ==0:
        print("La suma de sus digitos es par")
    else:
        print("La suma de sus digitos es impar")
