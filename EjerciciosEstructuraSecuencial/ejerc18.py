# Ecuacion a*x**2 + b*x +c
# Determinante = b**2 – 4*a*c
#x1=  (-b + ( b**2 – 4*a*c)**(1/2)) / (2*a)
#x2 = (-b - ( b**2 - 4*a*c)**(1/2) )/ (2*a)
#Datos de entrada coeficientes de la ecuacion
a = float(input("Ingrese coeficiente a :" ))
b = float(input("Ingrese coeficiente b :" ))
c = float(input("Ingrese coeficiente c :" ))

#Calculo

determinante = b**2 - 4*a*c

if determinante>=0:

    x1= (-b + ( b**2 - 4*a*c)**(1/2)) / (2*a)
    x2= (-b - ( b**2 - 4*a*c)**(1/2) )/ (2*a)
    print(" La soluciones de la ecuacion de segundo grado son:")
    print(" x1 = %.2f" %x1)
    print(" x2 = %.2f" %x2)

else:
    print("No existen soluciones reales ")