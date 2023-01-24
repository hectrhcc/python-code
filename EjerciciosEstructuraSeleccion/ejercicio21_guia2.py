letra=input("Introduce una letra: ")
if 0<len(letra)<2:
    if letra =="ñ":
        print("La letra es una consonante ")     
    elif  65<=ord(letra)<=90 or 97<=ord(letra)<=122:# LETRA
        if ord(letra) == 65 or ord(letra) == 69 or ord(letra) == 73 or ord(letra) == 79 or ord(letra) ==85 or ord(letra) == 97 or ord(letra) == 101 or ord(letra) == 105 or ord(letra) == 111 or ord(letra) == 117:
            print("La letra ingresada es una vocal ")
        else:
            print("La letra es una consonante ")    
    else: 
        print("Otro carácter distinto a letra")
else:
    print("Debes ingresar una letra")