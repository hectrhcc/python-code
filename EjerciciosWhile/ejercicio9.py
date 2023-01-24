num =""
while num!=0:
    num = int (input("Ingresar un número correspondiente a los días de una semana:"))
    if num==0:break
    elif num ==1:print("Lunes")
    elif num ==2:print("Martes")
    elif num ==3:print("Miercoles")
    elif num ==4:print("Jueves")
    elif num ==5:print("Viernes")
    elif num ==6:print("Sábado")
    elif num ==7:print("Domingo")
    else:
        print("Ingrese un número válido ")