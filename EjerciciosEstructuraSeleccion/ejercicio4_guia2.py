#“Buenos Días” (05:30 a 12:00), “Buenas Tardes” (12:01 a 20:15) ó “Buenas Noches” (20:16 a
#05:29)

hora=int(input("Ingrese una hora:")) 
min =int(input("Ingrese minutos:"))

#if (hora<0 and hora > 23 and min<0 and min>59 ):
if hora<0 or min<0:
    print("Usuario ingrese una hora y minutos validos")
elif hora>23 or min>59:
    print("Usuario ingrese una hora y minutos validos")
else:
    if hora==5 and min>=30: #and min <=59: 
     print("Buenos dias")
     #print("estoy entrando en el primer if")
    #elif 6<= hora<=12:
    elif 6<= hora <= 11:
     print("Buenos dias") #hasta aqui todo bien
     #print("estoy entrando en el segundo if")
    elif hora ==12 and min==0:
     print("Buenos dias")
     #print("estoy entrando en el tercer if")
    #elif hora ==12 and min>0:
     #print("Buenos tardes")
     #print("estoy entrando en el cuarto if")
    elif 12<= hora <= 19:   #0<=min <16:  # 01 min hasta 15 min
     print("Buenos tardes")
     #print("estoy entrando en el quinto if")
    elif hora==20 and 0<=min<=15:
     print("Buenos tardes")
     #print("estoy entrando en el sexto if")
    else:
     print("Buenas noches")
     #print("estoy entrando en el ultimo if")