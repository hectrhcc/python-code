num=int(input("Ingrese un valor:"))  #2 numeros naturales
num1=int(input("Ingrese otro valor:")) #4 numeros naturales

if num ==num1: #todo numero es multiplo de si mismo
   print("el numero %d"% num," es multiplo de %.d" % num1)
elif num1 ==0:
    print("La división por cero no está permitida/definida")
else:
    if num % num1 == 0:
        print("el numero %d"% num," es multiplo de %.d" % num1)                                            
    elif num1 % num ==0:
        print("el numero %d"% num1," es multiplo de %d" % num)
    else:
        print("los numeros ingresados no son multiplos")
# 2 es submultiplo de 4

