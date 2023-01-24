hora = "nada"
while hora!=-1:
    hora=int(input("Ingrese una hora:")) 
    min =int(input("Ingrese minutos:"))

    if hora<0 or min<0:
        print("Usuario ingrese una hora y minutos validos")
    elif hora>23 or min>59:
        print("Usuario ingrese una hora y minutos validos")
    else:
        if hora==5 and min>=30: 
         print("Buenos dias")
        elif 6<= hora <= 11:
         print("Buenos dias")
        elif hora ==12 and min==0:
         print("Buenos dias") 
        elif 12<= hora <= 19:  
         print("Buenos tardes")
        elif hora==20 and 0<=min<=15:
         print("Buenos tardes")
        else:
         print("Buenas noches")  