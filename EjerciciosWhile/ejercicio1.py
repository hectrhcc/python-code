num ="nada"
while num !=0:
    num =int(input("Ingresar un valor: "))

    if num==0:
        print("lo siento aún no se ponen de acuerdo")
    elif num % 2 == 0:
        print("es par")
    else:
        print("es impar")
