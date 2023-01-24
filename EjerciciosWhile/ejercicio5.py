hora ="nada"
while hora!=-1:
    hora = int(input("Ingrese una hora: "))

    if hora>23 or hora <=0:
        print("Ingrese una hora valida ")
    else:
        if 5<=hora<=12:
            print("Buenos dias ")
        elif 13<=hora<=20:
            print("Buenas tardes ")
        else:
            print("Buenas noches ")
        