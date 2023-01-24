palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")
if len(palabra1)==0 or len(palabra2) ==0:
    print("Ingrese una palabra")
 
else:
    if len(palabra1) > len(palabra2):
        print("La primera palabra es mas larga que la segunda")
    elif len(palabra1) == len(palabra2):
        print("La primera palabra es igual de larga que la segunda")
    else:
        print("La segunda palabra es mas larga que la primera")
    