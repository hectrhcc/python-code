#Leer una secuencia de 30 números y mostrar la suma de los primos.
n = 0
suma = 0
while n<30:
    n+= 1
    num = float(input("Ingresar un numero: "))
    suma +=  num

print("la suma es", suma)