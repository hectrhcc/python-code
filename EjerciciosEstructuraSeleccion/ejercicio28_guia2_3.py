mt3_consumo = float(input("Ingrese la cantidad de agua consumida en metros cúbicos:"))
cobro_total=0

if mt3_consumo<0:
 print("Ingrese una cantidad consumida válida ")

if  mt3_consumo>=100: 
    x = mt3_consumo -100
       
    if x >=0:
        cobro_total+=100*110
        intervalo_consumo = mt3_consumo
        intervalo_consumo-=100        
else:
    cobro_total+= mt3_consumo*110       
        
if  mt3_consumo>100: #  SEGUNDO INTERVALO                       
    x = intervalo_consumo-400
    if x >=0:
        cobro_total+= 400 *150   
        intervalo_consumo-=400 
        
    else:
        cobro_total+= intervalo_consumo*150
if  mt3_consumo>500:    #TERCER INTERVALO
    x = intervalo_consumo-500
    if x >=0: 
        cobro_total+=500 *250
        intervalo_consumo-=500
    else:
        cobro_total+= intervalo_consumo*250 
if  mt3_consumo>1000: #CUARTO INTERVALO
    x = intervalo_consumo-1000
    if x >=0:
        cobro_total+=1000*550
        intervalo_consumo-=1000
    else:
        cobro_total+= intervalo_consumo*550

print("El cobro de agua total es: %.0d" %cobro_total )