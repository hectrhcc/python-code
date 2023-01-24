#Leer una secuencia de números y sumar solo los pares mostrando
#el resultado del proceso.
n =float(input("Ingrese cantidad de numeros:"))
suma = 0
while n!=0:
    num =float(input("Ingresar numero:"))    
    suma += num
    n-=1

print("la suma es: ", suma)
