#Solicitar numeros de horas mensuales y valor de la hora
#Multiplicar numeros de horas mensuales por el valor de la hora
#Mostrar el suedo bruto mensual de un trabajador

#Datos de entrada
num_horas_mes =float(input("Ingrese numero de horas trabajadas en el mes: "))
valor_hora = float(input("Ingrese valor de la hora: "))

#Calculo

sueldo_bruto_mensual = valor_hora* num_horas_mes

#Datos de salida
print("El suedo bruto mensual es: %.2f" %sueldo_bruto_mensual)