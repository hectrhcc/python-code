#Solicitar numero de horas normales
#Solicitar valor de hora
#Solicitar horas extras
#Calcular valor horas extras  multiplicando valor hora normal por  1,5
#Obtener sueldo extra multiplicando horas extras por valor horas extras
#Obtener sueldo normal multiplicando horas normales por valor hora
#Obtener sueldo total bruto sumando sueldo normal con sueldo extra


#Datos de entrada
num_horas_mes =float(input("Ingrese numero de horas normales en el mes: "))
valor_hora_normal = float(input("Ingrese valor de la hora: "))
hora_extra = float(input("Ingrese las horas extra: "))

#Calculo

sueldo_bruto_normal = valor_hora_normal* num_horas_mes
valor_hora_extra = 1.5 *valor_hora_normal
sueldo_extra = hora_extra* valor_hora_extra 
sueldo_bruto_total = sueldo_bruto_normal + sueldo_extra
#Datos de salida
print("El suedo bruto mensual es: %.2f" %sueldo_bruto_total)
