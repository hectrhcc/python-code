#Funciones
#Factorial
def factorial(n):
    f=1
    while n>0:
        f=f*n
        n=n-1
        #print(n)
        #print(f)
    return f
#Binominal
def Binominal(x,y):
    return (factorial(x)/(factorial(x-y)*factorial(y)))

#Programa principal
valorm =int(input("Ingrese un valor para positivo M:"))
while valorm<=0:
    print("Error ingrese un valor negativo")
    valorm =int(input("Ingrese un valor para positivo M:"))
valorn=int(input("Ingrese un valor para N menor que %d:"%valorm))
while valorn>=valorm:
    valorn=int(input("Ingrese un valor para N menor que %d:" %valorm))    
print("El resultado es:",Binominal(valorm,valorn) )
    










