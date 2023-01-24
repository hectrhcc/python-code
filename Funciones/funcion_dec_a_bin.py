import math
#definicion de la funcion
def funcion_dec_a_bin(x):
    bin=""
    while x:
        bin+=str(x%2) # al revés
        x/=2
        x=math.trunc(x)
        #print(x)    
    return bin[::-1] #invierto el string de la forma mas optima

#programa principal
print("Conversion de decimal a binario")
n=int(input("Ingrese un numero:"))
print("En binario =",funcion_dec_a_bin(n))