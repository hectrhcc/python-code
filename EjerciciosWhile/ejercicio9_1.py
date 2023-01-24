num =" "
while num!=0:
    dias = ('lunes','martes','miercoles','jueves','viernes','sabado','domingo')
    num = int(input("Ingresar un número correspondiente a los días de una semana:"))
    if num==0: break #Se rompe el bucle   
    elif num==1:print(dias[num-1])
    elif num==2:print(dias[num-1])
    elif num==3:print(dias[num-1])
    elif num==4:print(dias[num-1])
    elif num==5:print(dias[num-1])
    elif num==6:print(dias[num-1])
    elif num==7:print(dias[num-1])
    else:
        print("Ingrese un número válido")