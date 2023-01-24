letra=input("Introduce una letra ")
if 0<len(letra)<2:
    if 97<=ord(letra)<=122:
        print("El caracter ingresado es una letra minuscula")
    elif 65<=ord(letra)<=90:
        print("El caracter ingresado es una letra mayúscula")
else:
    print("Debes ingresar una letra")