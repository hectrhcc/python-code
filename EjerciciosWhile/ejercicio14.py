
mes=""
while mes!=0:
	print("Este programa determina su signo zodiacal:")
	mes = int(input("Ingrese su mes de nacimiento:"))
	if mes==0:
            break
	dia = int(input("Ingrese su dia de nacimiento:"))
	if mes <0 or mes >12 or dia<0 or dia>31:
            print("Ingrese una fecha válida")
	# Marzo
	if mes ==3 and dia>=21:print("Signo Aries ")
	elif mes ==3 and dia<21:print("Signo Piscis ")
	#Abril
	if mes==4 and dia<=20 :print("Signo Aries ")
	elif mes==4 and dia>20:print("Signo Tauro ")
	#Mayo
	if mes==5 and dia<=20:print("Signo Tauro ")
	elif mes==5 and dia >20:print("Signo Géminis ")	
	#Junio
	if mes==6  and dia>=21:print("Signo Cáncer ")
	elif mes==6  and dia <21:print("Signo Géminis ")
	#Julio
	if mes==7 and dia<=22 :
	    print("Signo Cáncer ")
	elif mes==7 and dia>22:
	    print("Signo Leo ")
	#Agosto
	if mes==8 and dia<=22:
	    print("Signo Leo ")
	elif mes==8 and dia>22:
	    print("Signo Virgo ")
	#Septiembre
	if mes==9 and dia<=22:
	    print("Signo Virgo ")
	elif mes==9 and dia>22:
	    print("Signo Libra ")
	#Octubre
	if mes==10 and dia<=22:
	    print("Signo Libra ")
	elif mes==10 and dia>22:
	    print("Signo Escorpio ")
	#Noviembre
	if mes==11 and dia <=22:
	    print("Signo Escorpio ")
	elif mes==11 and dia>22:
	    print("Signo Sagitario ")
	#Diciembre
	if mes==12 and dia <=21 :
	    print("Signo Sagitario ")
	elif mes==12 and dia>21:
	    print("Signo Capricornio ")
	#Enero
	if mes==1 and dia<=20:
	    print("Signo Capricornio ")
	elif mes==1 and dia>20:
	    print("Signo Acuario ")
	#Febrero
	if mes==2 and dia<=18:
	    print("Signo Acuario ")
	elif mes==2 and dia>18:
	    print("Signo Piscis ")