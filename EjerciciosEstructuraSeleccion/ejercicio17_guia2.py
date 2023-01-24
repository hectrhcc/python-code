
valor1=float(input("Ingrese el primer valor:")) 
valor2=float(input("Ingrese el segundo valor:")) 
valor3=float(input("Ingrese el tercer valor:")) 

limite_menor=valor1
limite_mayor=valor2

if limite_menor<valor3<limite_mayor:
    print("El tercer valor esta dentro del intervalo ")
else:
    print("El tercer valor no esta dentro del intervalo ")