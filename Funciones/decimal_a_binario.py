#Funcion decimal a binario
def Decimal_a_binario(n):
    bin=""
    while n>0:
        bin+=str(n%2)
        #print("bin",bin)
        n//=int(2)
        #print("n",n)
    return bin[::-1]

#Programa principal
decimal=int(input("Ingrese un número decimal: "))
print("El equivalente en binario es: ",Decimal_a_binario(decimal))


