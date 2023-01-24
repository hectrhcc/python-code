num1 = int(input("Ingrese numero 1:"))
num2 = int(input("Ingrese numero 2:"))
num3 = int(input("Ingrese numero 3:"))
num4 = int(input("Ingrese numero 4:"))
num5 = int(input("Ingrese numero 5:"))


mayor= num1
menor= num1
#solo funciona de forma ascendente o descendente
if num2>mayor: # si este no se cumple ya no funciona el resto del codigo
    mayor = num2
    menor = num1  #hay que hacer que se ejecute independiente si es verdad o no
    print("entre al primer if") 
elif num3> mayor: #and num3>num1:
    mayor = num3
    print("entre al segundo if") 
elif num4> mayor: #and num4>num2 and num4>num1:
    mayor = num4
    print("entre al tercer if") 
elif num5> mayor:#and num5>num3 and num5> and num2 and num5> num1:  
    mayor = num5
    print("entre al cuarto if ") 
print("El numero mayor es:", mayor) 
