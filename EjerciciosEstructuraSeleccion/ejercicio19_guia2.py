caracter=input("Introduce un carácter ")
if 0<len(caracter)<2:
    if 97<=ord(caracter)<=122:
        print("El caracter ingresado es una letra minuscula")
    elif 65<=ord(caracter)<=90:
        print("El caracter ingresado es una letra mayúscula")
    elif 48<=ord(caracter)<=57:
        print("El caracter ingresado es un digito")
    else:
        print("otro carácter distinto de dígito y letra")
else:
    print("Debes ingresar una letra")