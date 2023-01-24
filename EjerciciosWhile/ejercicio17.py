sueldo=""
while sueldo !=0:
    sueldo=float(input("Ingrese sueldo:"))
   # if sueldo==0:
    #    break
    antigüedad = int(input("Ingrese años de antigüedad:"))

    if antigüedad<=2:
        aumento= sueldo*0.05
        sueldofinal=sueldo+aumento
        print("El aumento es de: %.2f" %aumento)
        print("Sueldo final:%.2f"%sueldofinal)
    elif antigüedad<=5:
        aumento = sueldo*0.08
        sueldofinal=sueldo + aumento
        print("El aumento es de: %.2f" %aumento)
        print("Sueldo final:%.2f"%sueldofinal)
    else:
        aumento = sueldo*0.12
        sueldofinal=sueldo + aumento
        print("El aumento es de: %.0f" %aumento)
        print("Sueldo final:%.0f"%sueldofinal)