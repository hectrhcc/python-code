# recibo de la  liquidacion de sueldo
# <=180hrs = valor hora
# 180<x =<195  = 50% mas
#  196> = 100%
# Bono = 100000 > 5 años  y 300000 > 10 años
# salud y prevision = 20% del sueldo

nombre = input("Ingrese nombre trabajador: ")
valorhora = float(input("Valor hora: "))
cant_años = float(input("Cantidad de años trabajando: "))
cant_hora_mes = float(input("Cantidad de horas que trabajo en el mes: "))

if cant_hora_mes <=180:
    sueldo_bruto = valorhora*cant_hora_mes

if cant_hora_mes >180 and cant_hora_mes <=195:
    #cant_hora_mes -=180
    sueldo_bruto = valorhora*cant_hora_mes+ valorhora*cant_hora_mes*0.50

if cant_hora_mes >195:
    sueldo_bruto = valorhora*cant_hora_mes + valorhora*cant_hora_mes

if cant_años >5 and cant_años<=10:
    bono_antiguedad = 100000
elif cant_años >10:
    bono_antiguedad = 300000
else:
    bono_antiguedad = 0
#bono_antiguedad
#monto_sueldo_bruto
#monto_descuentos
#monto_sueldo_liquido
#sueldo_bruto+= bono_antiguedad 

monto_sueldo_bruto = sueldo_bruto + bono_antiguedad
monto_descuentos = monto_sueldo_bruto *0.20
monto_sueldo_liquido = monto_sueldo_bruto - monto_descuentos


#
print("---------------------------------")
print("Recibo de liquidación de sueldo: ")
print("Nombre empleado: ", nombre)
print("Bono: ", bono_antiguedad)
print("Monto Sueldo Bruto: $",monto_sueldo_bruto)
print("Monto Sueldo Líquido: $",monto_sueldo_liquido)
print("Monto descuentos: $",monto_descuentos )