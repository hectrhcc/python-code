#Hemisferio sur
#Primavera: 21 septiembre hasta 20 diciembre
#Verano: 21 diciembre hasta 20 marzo
#Otoño: 21 marzo hasta 20 junio
#Invierno: 21 junio hasta 20 septiembre
mes=""
while mes!=0:
    dia =int(input("dia:"))
    mes =int(input("mes:"))
    if mes==0:
        break
    #validacion de la fecha
    if 0<dia<=31 and 0<mes<=12:
        fecha = mes*100+dia  #agrupa para comparar de una vez
    if fecha<=320:estacion ='verano'
    elif fecha<=620:estacion = 'otoño'
    elif fecha<=920:estacion = 'invierno'
    elif fecha<=1220:estacion = 'primavera'
    else: estacion = 'verano'

    print("la estacion de",dia,'/',mes,'es',estacion)