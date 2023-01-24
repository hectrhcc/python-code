mt3_consumo = float(input("Ingrese la cantidad de agua consumida en metros cúbicos:"))
cobro_total=0
#66
if mt3_consumo<0:
 print("Ingrese una cantidad consumida válida ")
    #cobro_cont = 100*110
     #cobro_total =  mt3_consumo *110
elif mt3_consumo<10000000:
# 890 => 100 *1 + 400 + 500 + 1000
# 890 => 100 + 400 + 390

# entrada 150   | 250 /  150

#x =  mt3_consumo -100                          si le resto 100 y es positivo  entonces entra
#y =                                                           sino        

    if  mt3_consumo>=100: # *100 o por x
        x = mt3_consumo -100
       
        if x >=0:#x maneja si corresponde o no cobrarle en ese intervalo
            cobro_total+=100*110
            intervalo_consumo = mt3_consumo
            intervalo_consumo-=100  #intervalo consumo se resta lo cobrado lleva la cuenta
        #else:
           #
    else:
          cobro_total+= mt3_consumo*110       
         #si le resto 400  al intervalo_consumo y es positivo entonce entra 
    if  mt3_consumo>100: #*400  o por x  SEGUNDO INTERVALO                       sino entra a x
        x = intervalo_consumo-400
        if x >=0:
            cobro_total+= 400 *150   
            intervalo_consumo-=400 
        #mt3_consumo-=400
        else:
            cobro_total+= intervalo_consumo*150
    if  mt3_consumo>500:  #*500 o por x   TERCER INTERVALO
         x = intervalo_consumo-500
         if x >=0: 
            cobro_total+=500 *250
            intervalo_consumo-=500
         else:
            cobro_total+= intervalo_consumo*250 
    if  mt3_consumo>1000:#*1000 o por x   CUARTO INTERVALO
         x = intervalo_consumo-1000
         if x >=0:
             cobro_total+=1000*550
             intervalo_consumo-=1000
         else:
            cobro_total+= intervalo_consumo*550
#else:

print("El cobro de agua total es: %.0d" %cobro_total )
