#Solicitar monto del sueldo mensual trabajador
#Solicitar monto del reajuste en porcentaje
#Dividir monto del reajuste en porcentaje en 100
#Obtenemos el reajuste multiplicando lo anterior por el monto del sueldo mensual
#Calcular el nuevo sueldo restando al sueldo el reajuste

#Datos de entrada
monto_sueldo_trabajador = float(input(" Ingrese sueldo mensual: "))
porcentaje_reajuste = float(input("Ingrese el porcentaje de reajuste: "))

#Calculo
retencion = monto_sueldo_trabajador * (porcentaje_reajuste/100)
nuevo_sueldo = monto_sueldo_trabajador - retencion

#Datos de salida
print(" El nuevo sueldo  mensual del trabajador es: %.2f " %nuevo_sueldo) 