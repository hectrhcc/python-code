
#Determinante >0  entonces hay 2 solucines
#Determinante = 0 hay soluciones iguales
#Determinante < 0 no hay soluciones reales

a=float(input("Ingrese el valor de A: "))
b=float(input("Ingrese el valor de B: "))
c=float(input("Ingrese el valor de C: "))

determinante =  b**2 -4*a*c

#a*x**2 + b*x +c = 0

#if a!=0:
if determinante>=0:
    x1 = (-b - ( b**2 -4*a*c)**(1/2)) / 2*a  # porque esta linea #el parentesis aqui es obligatorio
    x2 = (-b + ( b**2 -4*a*c)**(1/2)) / (2*a) #es distinta a esta linea??? esta es correcta
    print(" El resultado de x1 = %0.2f   x2 = %0.2f" %(x1, x2)) #%0.2f
else: #respuesta por la prioridad en la evaluacion mult y div misma prioridad porque son la misma operacion luego si hay empate de izquierda a derecha por eso que da resultados distintos en este ejemplo
    print(" No hay soluciones reales")
