RANGO1 = 300000
RANGO2 = 500000
RANGO3 = 1000000

sueldo_trabajador = float(input("Ingrese sueldo de trabajador:"))
if sueldo_trabajador>0:
    if sueldo_trabajador < RANGO1:
        impuesto = 0.02 * sueldo_trabajador
        print("Impuesto: %.0f" % impuesto)
    elif RANGO1<=sueldo_trabajador<=RANGO2:
        impuesto = 0.05 * sueldo_trabajador
        print("Impuesto: %.0f" % impuesto)
    elif RANGO2<sueldo_trabajador<RANGO3:
        impuesto = 0.08 * sueldo_trabajador
        print("Impuesto: %.0f" % impuesto)
    elif sueldo_trabajador>=RANGO3:
        impuesto = 0.10 * sueldo_trabajador
        print("Impuesto: %.0f" % impuesto)
else:
    print("Ingrese un sueldo válido")