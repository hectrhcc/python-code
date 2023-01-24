#Leer una secuencia de números y mostrar la suma de los pares
#y el producto de los que son múltiplo de 5.
suma = 0
producto = 1
while True:
    num =float(input("Ingrese un numero:"))
    
    if num % 2 == 0 :
        suma += num
    if num % 5 == 0:
        producto*= num 
    print("la suma es: ", suma)
    print("el producto: ", producto)
