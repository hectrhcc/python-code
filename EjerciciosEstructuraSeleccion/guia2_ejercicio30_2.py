rut_trabajador = str(input('Ingrese el rut del trabajador: '))
sueldo_base = int(input('Ingrese el valor del sueldo base: '))
cant_anios = int(input('Ingrese la cantidad de años que lleva trabajando en la empresa: '))
cant_hrsXtras = int(input('Ingrese la cantidad de horas extras que trabajó en el mes: '))

aux1_hrs = aux2_hrs = aux3_hrs =  0

if cant_hrsXtras > 10:
    aux1_hrs = 10
    auxiliar = cant_hrsXtras - aux1_hrs
    pago_hrsXtras1 = aux1_hrs * 20000
    pagoTotal_hrsXtras = pago_hrsXtras1
    if auxiliar > 20:
        aux2_hrs = 20
        aux3_hrs = auxiliar - aux2_hrs
        if cant_anios < 10:
            porcentaje = 50
            pago_hrsXtras2 = aux2_hrs * 20000 * 1.5
            pago_hrsXtras3 = aux3_hrs * 20000
            pagoTotal_hrsXtras = pagoTotal_hrsXtras + pago_hrsXtras2 + pago_hrsXtras3
        elif cant_anios < 20:
            porcentaje = 75
            pago_hrsXtras2 = aux2_hrs * 20000 * 1.75
            pago_hrsXtras3 = aux3_hrs * 20000
            pagoTotal_hrsXtras = pagoTotal_hrsXtras + pago_hrsXtras2 + pago_hrsXtras3
        else:
            porcentaje = 100
            pago_hrsXtras2 = aux2_hrs * 20000 * 2
            pago_hrsXtras3 = aux3_hrs * 20000
            pagoTotal_hrsXtras = pagoTotal_hrsXtras + pago_hrsXtras2 + pago_hrsXtras3
    else:
        aux2_hrs = auxiliar
        if cant_anios < 10:
            porcentaje = 50
            pago_hrsXtras2 = aux2_hrs * 20000 * 1.5
            pagoTotal_hrsXtras = pagoTotal_hrsXtras + pago_hrsXtras2
        elif cant_anios < 20:
            porcentaje = 75
            pago_hrsXtras2 = aux2_hrs * 20000 * 1.75
            pagoTotal_hrsXtras = pagoTotal_hrsXtras + pago_hrsXtras2
        else:
            porcentaje = 100
            pago_hrsXtras2 = aux2_hrs * 20000 * 2
            pagoTotal_hrsXtras = pagoTotal_hrsXtras + pago_hrsXtras2
else:
    aux1_hrs = cant_hrsXtras
    pago_hrsXtras1 = aux1_hrs * 20000
    pagoTotal_hrsXtras = pago_hrsXtras1
    
if cant_anios > 5 and cant_anios <= 10:
    bono_antiguedad = 100000
elif cant_anios > 10 and cant_anios <= 15:
    bono_antiguedad = 200000
elif cant_anios > 15:
    bono_antiguedad = 300000
else:
    bono_antiguedad = 0
    
sueldo_bruto = sueldo_base + pagoTotal_hrsXtras + bono_antiguedad
monto_descuentos = sueldo_bruto * 0.2
sueldo_liquido = sueldo_bruto - monto_descuentos

print('\nLiquidación de Sueldo\n')
print(f'Rut del empleado: {rut_trabajador}\n')
print(f'Sueldo base = $ {sueldo_base}')
if aux1_hrs > 0:
    print(f'Monto por primeras {aux1_hrs} horas extras = $ {pago_hrsXtras1}')
if aux2_hrs > 0:
    print(f'Monto por siguientes {aux2_hrs} horas extras al {porcentaje}% = $ {round(pago_hrsXtras2)}')
if aux3_hrs > 0:
    print(f'Monto por restantes {aux3_hrs} horas extras = $ {round(pago_hrsXtras3)}')
print(f'Monto por bono de antiguedad = $ {bono_antiguedad}\n')
print(f'Monto sueldo bruto = $ {round(sueldo_bruto)}')
print(f'Descuento por salud y previsión = $ -{round(monto_descuentos)}\n')
print(f'Monto sueldo líquido = $ {round(sueldo_liquido)}')
