#Solicitar cantidad de segundos
#Obtener hora dividiendo cantidad de segundos por 3600 
#Quitar los segundos convertidos en horas
#Obtener los minutos dividiendo cantidad de segundos por 60
#Quitar los segundos convertidos en minutos y los segundos convertidos a horas
#Obtener la cantidad en segundos

#Dato de entrada
segundos =float(input("Ingresar cantidad de segundos: "))

#Calculo

hora = int(segundos /3600)
menoshora= segundos- hora*3600 #descuenta la hora que ya converti
min = int(menoshora/60)
menosminuto = segundos - min*60 #descuento los minutos que ya converti
segundos2 = int (segundos - menoshora - menosminuto) *-1

#Dato de salida
print("Los segundos son equivalentes a  ", hora,"horas ", min , "minutos", segundos2, "segundos" )