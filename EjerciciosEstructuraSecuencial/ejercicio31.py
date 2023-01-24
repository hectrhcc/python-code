segundos=int(input("Ingrese cantidad de segundos: "))

hora = int(segundos /3600)
#int(segundos / 60)
menoshora = segundos - hora *3600
minuto= int (menoshora /60)
menosminuto = segundos - minuto*60
segundos2 =  (segundos - menoshora -menosminuto)*-1


print("Resultado: ", hora, " horas", minuto, "minutos y ", segundos2, "segundos" )