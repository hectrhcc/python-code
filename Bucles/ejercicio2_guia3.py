#Solicitar 2 numeros
#Mientras los numeros sean distintos de cero
#Sumar
#Decrementar el valor  de los numeros


num1 = float(input("Ingresar un numero: "))
num2 = float(input("Ingresar otro numero: "))

while num1!=0 and num2!=0:
     
     sumar = num1 +num2
     print("La suma es: ", sumar)
     num1-=1
     num2-=1
