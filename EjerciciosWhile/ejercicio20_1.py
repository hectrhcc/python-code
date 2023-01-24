mm=""
while mm!=0:
    meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    dd = int(input("Ingrese un día:"))
    mm = int(input("Ingrese un mes:"))
    if mm ==0: break
    año = int(input("Ingrese un año:"))
    #verificación de mes
    mm -=1
    if meses[mm] not in meses:print("Ingrese un mes válido") 
    #verificación del año
    if año>0:
        if ((año %400) ==0) or ((año %100)!=0 and (año%4) ==0): #print("Es un año bisiesto")
            dias = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            mm-=1
            #verificación del día
            if dd>dias[mm]:
                print("La fecha no es correcta")
            else:
                print("La fecha es correcta")
        else:#print("No es un año bisiesto")
            dias = (31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            mm-=1
            #verificación del día
            if dd>dias[mm]:
                print("La fecha no es correcta")
            else:
                print("La fecha es correcta")
    else:
        print("Ingrese un año válido")
    mm=""