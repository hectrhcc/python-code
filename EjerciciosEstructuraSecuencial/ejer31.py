segundos= float(input("Ingrese los segundos a convertir"))
# 8570 segundos son: 2 horas, 22 minutos y 50 segundos.

hora = int (segundos /3600)
hora_menos = segundos - hora*3600
minutos = int (hora_menos / 60)
min_menos = segundos - minutos*60
segundos2 = int (segundos - min_menos - hora_menos)*-1
        
print("La conversion de los segundos:  ", hora ," : " , minutos ,":" , segundos2 )