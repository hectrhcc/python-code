#Hemisferio sur
#Primavera: 21 septiembre hasta 20 diciembre
#Verano: 21 diciembre hasta 20 marzo
#Otoño: 21 marzo hasta 20 junio
#Invierno: 21 junio hasta 20 septiembre
mm=""
while mm!=0:
	meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
 	estaciones = ('verano', 'otoño', 'invierno', 'primavera')	
    fechas = (21 21 21 21 )
    dd = int(input("Ingrese un día:"))
    mm = int(input("Ingrese un mes:"))
    if mm=="0":
        break;
    if 0<dd<=31:
    mes=mm/4	
    #if mm.lower() in meses :

    	print ("La estación es: " + estaciones[mm]) #los primeros 3 meses son verano
    else:
    	print ("La estación es: " + estaciones[mm])