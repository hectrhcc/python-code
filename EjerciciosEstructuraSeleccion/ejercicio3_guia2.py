#Saludar con “Buenos Días” (05 a 12), “Buenas Tardes” (13 a 20) ó
#“Buenas Noches” (21 a 04), según la hora que ingrese el usuario (hh).

hora = int (input("Ingrese una hora: "))

if hora>23:
    print("Ingrese una hora valida ")
else:
    if 5<=hora<=12:
        print("Buenos dias ")
    elif 13<=hora<=20:
        print("Buenas tardes ")
    else:
        print("Buenas noches ")
        
   # elif 21<=hora<=23:
    #    print("Buenas noches ")
    #elif 0<=hora<=4:
     #   print("Buenas noches ")
