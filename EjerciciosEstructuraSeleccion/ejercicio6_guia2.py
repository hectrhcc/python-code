num1 = int(input("Ingrese numero 1:"))
num2 = int(input("Ingrese numero 2:"))
num3 = int(input("Ingrese numero 3:"))
num4 = int(input("Ingrese numero 4:"))
num5 = int(input("Ingrese numero 5:"))

# SI COMPARO CON EL ANTECESOR SOLAMENTE NO VOY A ENCONTRAR REALMENTE AL MAYOR solo funciona de forma ascendente o descendente
# SI COMPARO CON EL NUMERO QUE QUEDO COMO MAYOR AHI SI ENCUENTRO AL MAYOR

mayor= num1
menor= num1

if num2>mayor:
    mayor = num2
else:
    menor = num2
    
if num3> mayor:
     mayor = num3
elif num3<menor:
     menor = num3
     
if num4> mayor:
     mayor = num4
elif num4 < menor:
     menor = num4
     
if num5> mayor:
     mayor = num5
elif num5 < menor:
     menor = num5

print("El numero mayor es:", mayor)
print("El numero menor es:", menor)