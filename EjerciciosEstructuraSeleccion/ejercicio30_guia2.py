rut =input("Ingrese rut con digito verificador: ") #algoritmo modulo 11
sueldo_base = float(input("Ingrese sueldo base: "))
cant_año = float(input("Ingrese cantidad de años: "))
cant_hrs_extra = float(input("Ingrese cantidad de horas extras: "))
x = cant_hrs_extra
y = cant_hrs_extra
PRIMERAS_10 = 0
HORAS_50 = 0
HORAS_75 = 0
HORAS_100 = 0
SOBRE_30 = 0
sueldo_extra = 0
if cant_hrs_extra>0:
    PRIMERAS_10 = 1
    if cant_hrs_extra>=10:
        sueldo_extra = 20000*10
    else:
        sueldo_extra = 20000*cant_hrs_extra
    #print("sueldo extra", sueldo_extra)
if 10<cant_hrs_extra<=30:
    y-=10
    if cant_año<10:
        HORAS_50=1
        #print("sueldo extra", sueldo_extra)
        sueldo_extra2 = (20000*y) + (20000*y)*0.50  #60000
        #print("sueldo extra", sueldo_extra)
    elif 10<cant_año<20:
        HORAS_75=1
        sueldo_extra2 = (20000*y) + (20000*y)*0.75
    elif cant_año>=20:
        HORAS_100=1
        sueldo_extra2 = 20000*y*2
if cant_hrs_extra>30:
    y -=30
    SOBRE_30 = 1
    sueldo_extra2= 20000*y2

if cant_año<10 and cant_año>5:
    bono = 100000
elif cant_año>=10 and cant_año<=15:
    bono = 200000
elif cant_año>15:
    bono = 300000

if cant_hrs_extra>10:
    monto_sueldo_bruto = sueldo_base +bono + sueldo_extra + sueldo_extra2
else:
    monto_sueldo_bruto = sueldo_base +bono + sueldo_extra 
descuento_salud = monto_sueldo_bruto*0.20
sueldo_liquido = monto_sueldo_bruto - descuento_salud
print("\n ")
print("Rut", rut, "sueldo base {:.2f}" .format(sueldo_base), "{:.2f} años de antiguedad" .format(cant_año), " {:.2f} horas extras trabajadas en el mes".format(cant_hrs_extra))
print("\n ")
#print("Horas extras %f: " % y)
print("Liquidación de Sueldo")
print("\n ")
print("Rut del empleado:", rut)
print("\n")
print("Sueldo base \t\t\t\t\t\t = \t$%d" % sueldo_base)
if PRIMERAS_10==1:
    print("Monto por primeras 10 horas extras \t\t\t\t\t\t = \t${:.2f}" .format(sueldo_extra))
if HORAS_50 == 1:
    x +=  - 10
    print("Monto por", x, "horas extras al 50% \t\t\t\t\t\t = \t${:.2f}" .format(sueldo_extra2))
if HORAS_75 == 1:
    x += - 10
    print("Monto por",x," horas extras al 75% \t\t\t\t = \t${:.2f}" .format(sueldo_extra2))
if HORAS_100 == 1:
    x +=  - 10
    print("Monto por",x," horas extras al 100% \t\t\t\t = \t${:.2f}" .format(sueldo_extra2))
if SOBRE_30 == 1:
    print("Monto por sobre 30 horas extras al 100% \t\t\t\t = \t${:.2f}" .format(sueldo_extra2))
print("Monto por bono de antigüedad\t\t\t\t\t\t = \t$%d"% bono)
print("\n ")
print("Monto sueldo bruto\t\t\t\t\t\t = \t $%d" % monto_sueldo_bruto)
print("Descuento por salud y previsión \t\t\t\t\t\t = \t $-%d" % descuento_salud)
print(" \n")
print("Monto sueldo líquido \t\t\t\t\t\t = \t $%d" % sueldo_liquido)