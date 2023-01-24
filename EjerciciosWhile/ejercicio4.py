num="nada"
while num!=-1:
    num = int(input("Ingrese un numero: "))
    if num % 8 == 0 and num % 3 == 0:
        print("el número es múltiplo de 8 y 3")
    else:
        print("el número no es múltiplo de 8 y 3")
