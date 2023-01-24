#IMC =  masa /estatura  = kg*m2
estatura = float(input("Ingrese su estatura en metros:"))
masa = float(input("Ingrese su masa corporal en kg: "))
imc = masa / estatura**2
print("Su Indice de masa corporal (IMC) es: %.2f" % imc)
if imc < 16.00:
    print(" Categoria: Delgadez Severa")
elif 16<=imc<=16.99:
    print(" Categoria: Delgadez Moderada")
elif 17.0<=imc<=18.49:
    print(" Categoria: Delgadez Leve")
elif 18.5<=imc<=24.99:
    print(" Categoria: Normal")
elif 25.00<=imc<=29.99:
    print(" Categoria: Pre-obeso")
elif 30.00<=imc<=34.99:
    print(" Categoria: Obesidad Leve")
elif 35.00<=imc<=39.99:
    print(" Categoria: Obesidad Media")
elif imc>=40.00:
    print(" Categoria: Obesidad Mórbida")
else:
    print(" Sin Categoria ")