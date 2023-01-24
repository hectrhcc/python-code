import math

valor = float(input("Ingrese un valor: "))
valor2 = math.trunc(valor)
#print(" valor2", valor2)
if valor2 % 8 == 0 and valor2 % 3 == 0:
    print("el valor ingresado es múltiplo de 8 y 3 a la vez")
#else:
    #print("el valor ingresado no es múltiplo de 8 y 3 a la vez")