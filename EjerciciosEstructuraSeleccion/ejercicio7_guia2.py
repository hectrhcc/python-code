num1 = int(input("Ingrese numero 1:"))
num2 = int(input("Ingrese numero 2:"))
num3 = int(input("Ingrese numero 3:"))
num4 = int(input("Ingrese numero 4:"))
num5 = int(input("Ingrese numero 5:"))

# SI COMPARO CON EL ANTECESOR SOLAMENTE NO VOY A ENCONTRAR REALMENTE AL MAYOR solo funciona de forma ascendente o descendente
# SI COMPARO CON EL NUMERO QUE QUEDO COMO MAYOR AHI SI ENCUENTRO AL MAYOR

mayor= num1
menor= num1
LUGAR_MAYOR = 1
LUGAR_MENOR = 1

if num2>mayor:
    mayor = num2
    LUGAR_MAYOR = 2
else:
    menor = num2
    LUGAR_MENOR = 2    
if num3> mayor:
     mayor = num3
     LUGAR_MAYOR = 3
elif num3<menor:
     menor = num3
     LUGAR_MENOR = 3
if num4> mayor:
     mayor = num4
     LUGAR_MAYOR = 4
elif num4 < menor:
     menor = num4
     LUGAR_MENOR = 4
if num5> mayor:
     mayor = num5
     LUGAR_MAYOR = 5
elif num5 < menor:
     menor = num5
     LUGAR_MENOR = 5
print("El numero mayor es:", mayor,"se ingreso en el lugar:", LUGAR_MAYOR)
print("El numero menor es:", menor,"se ingreso en el lugar:", LUGAR_MENOR)