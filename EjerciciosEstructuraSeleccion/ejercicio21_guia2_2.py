
letra=input("Introduce una letra ")

#a = 97       A = 65
#e = 101      E = 69
#i = 105      I = 73
#o = 111      O = 79
#u = 117      U = 85 
if 0<len(letra)<2:
    if 97<=ord(letra)<=122:
        print("El caracter ingresado es una letra minuscula")
        if ord(letra) == 97 or ord(letra) == 101 or ord(letra) == 105 or ord(letra) == 111 or ord(letra) == 117:
            print("La letra ingresada es una vocal ")
        else:
            print("La letra ingresada es una consonante ")
    elif 65<=ord(letra)<=90:
        print("El caracter ingresado es una letra mayúscula")
        if ord(letra) == 65 or ord(letra) == 69 or ord(letra) == 73 or ord(letra) == 79 or ord(letra) ==85:
            print("La letra ingresada es una vocal ")
        else:
            print("La letra es una consonante ")
    else: 
        print("Otro carácter distinto a letra")
else:
    print("Debes ingresar una letra")