# Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

numeros = (5,4,3,2,1,6,45,3,6,6,6,6,6)
 
numero = int(input("Dame un numero: "))
 
contador= 0
for i in numeros:
    if numero == i:
        contador = contador + 1
 
print ("Hay ",contador," repeticion/es")
