a=float(input("Ingresar el valor de a"))
b=float(input("Ingresar el valor de b"))
c=float(input("Ingresar el valor de c"))

x1 =(-b + (b**2-4*a*c )**(1/2))/(2*a)

x2 = (-b - (b**2-4*a*c )**(1/2))/(2*a)
print("Las soluciones de la ecuacion de segundo grado son: %4.2f %4.2f" %x1 %x2)
