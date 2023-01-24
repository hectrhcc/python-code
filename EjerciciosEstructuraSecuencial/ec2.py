
import math
print("Ecuación Cuadratica")
a=float(input("Dime el valor de a: " ))
b=float(input("Dime el valor de b: " ))
c=float(input("Dime el valor de c: " ))
d= b*b-4*a*c
if d != 0:
  x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
  x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
  print("Soluciones de la ecuacion: x1=%4.3f y x2=%4.3f " % (x1, x2))
else:
  if b != 0:
    x = -c / b
    print ("Solucion de la ecuacion: x=%4.3f " % x)

  else:
    if c != 0:
      print ("La ecuacion no tiene solucion. ")

    else:
      print ("La ecuacion tiene infinitas soluciones. ")
