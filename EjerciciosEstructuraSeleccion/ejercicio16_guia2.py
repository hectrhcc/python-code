lado1=float(input("Ingrese primer lado del triángulo:")) 
lado2=float(input("Ingrese segundo lado del triángulo:")) 
lado3=float(input("Ingrese tercer lado del triángulo:")) 

mayor=lado1                                  
menor=lado1                                  
menor2 =lado1  
if lado2>mayor:
    mayor=lado2     
else:               
    menor=lado2
if lado3>mayor:
    mayor=lado3
elif lado3<menor:
    menor=lado3
#valor de menor... en este contexto no hay intermedio
# cuando los mayores se repitan entonces menor2 = mayor
if  mayor == lado1 and mayor == lado2:   
   menor2 = mayor
elif mayor == lado2 and mayor == lado3:   
   menor2 = mayor
elif mayor == lado1 and mayor == lado3:   
    menor2 = mayor
# cuando los menores se repitan entonces menor2 = menor
if  menor == lado1 and menor == lado2:   
   menor2 = menor
elif menor == lado2 and menor == lado3:   
   menor2 = menor
elif menor == lado1 and menor == lado3:   
    menor2 = menor

if (lado1>menor) and (lado1<mayor):
    menor2 = lado1
if (lado2>menor) and (lado2<mayor):
    menor2 = lado2
if (lado3>menor) and (lado3<mayor):
    menor2 = lado3
if menor + menor2 > mayor :

    print("los lados ingresados forman un triangulo")
#si es un triangulo entonces de que tipo es
    if lado1 != lado2 and lado1!=lado3 and lado2!=lado3:
        print("el tipo de triangulo es escaleno")
    elif lado1 == lado2 and lado1==lado3: 
        print("el tipo de triangulo es equilatero")
    else:
        print("el tipo de triangulo es isósceles")
else:
    print("los lados ingresados no forman un triangulo")