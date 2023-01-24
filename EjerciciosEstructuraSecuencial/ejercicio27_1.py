num_horas_mes = int(input("Ingrese numero de horas trabajadas en el mes: "))
valor_hora = float(input("Ingrese valor de hora: "))
percent_retencion = float(input("Ingrese porcentaje de retencion: "))
sueldo_bruto_mensual = num_horas_mes*valor_hora
retencion = sueldo_bruto_mensual * (percent_retencion/100)
sueldo_liquido = sueldo_bruto_mensual - retencion
print("El sueldo bruto mensual es: %.2f" %sueldo_bruto_mensual)
print("El sueldo liquido mensual es: %.2f" %sueldo_liquido)