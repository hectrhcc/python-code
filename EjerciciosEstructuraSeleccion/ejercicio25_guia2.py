print("\tMenu Opciones    ")
print("1) Suma     ")
print("2) Resta    ")
print("3) Multiplicacion    ")
print("4) Division    ")
print("5) Exponenciacion    ")
opcion = input("Ingrese una opcion:")

if opcion == "1":
    num1=int(input ("Ingrese numero 1: "))
    num2=int(input ("Ingrese numero 2: "))
    suma = num1 + num2
    print("El resultado suma = ", suma )
elif opcion == "2":
    num1=int(input ("Ingrese numero 1: "))
    num2=int(input ("Ingrese numero 2: "))
    resta = num1 - num2
    print("El resultado resta = ", resta )
elif opcion == "3":
    num1=int(input ("Ingrese numero 1: "))
    num2=int(input ("Ingrese numero 2: "))
    multiplicacion= num1*num2
    print("El resultado multiplicacion = ", multiplicacion )
elif opcion == "4":
    num1=int(input ("Ingrese numero 1: "))
    num2=int(input ("Ingrese numero 2: "))
    if num2 ==0:
        print("La division por cero es indeterminada")
    else:
        division = num1 /num2
        print("El resultado division = ", division )
elif  opcion == "5":
    num1=int(input ("Ingrese numero 1: "))
    num2=int(input ("Ingrese numero 2: "))
    exponenciacion = num1**num2
    print("El resultado exponenciacion = ", exponenciacion )
else:
    print("Ingrese una opcion válida ")