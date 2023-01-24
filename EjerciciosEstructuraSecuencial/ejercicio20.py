
monto_sueldo=float(input("Ingresar el sueldo trabajador: "))
monto_reajuste=float(input("Ingresar el monto reajuste en porcentaje: "))
nuevo_sueldo=monto_sueldo - (monto_sueldo *(monto_reajuste/100) )
print("El nuevo monto de sueldo: %.2f" %nuevo_sueldo)