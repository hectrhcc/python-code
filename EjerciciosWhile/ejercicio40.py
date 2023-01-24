COMISION=0.05
cont=3
boletas=int(input("¿Hay boletas para cargar? 0 = no "))
while boletas!=0:
    if boletas==0 or cont==0:break
    else:
        num_vendedor=int(input("Ingrese el numero de vendedor:"))
        importe=int(input("Ingrese el importe:"))
        ganancia= importe*COMISION
        print("El vendededor ", num_vendedor,"gana $",ganancia)
        boletas=int(input("¿Hay boletas para cargar?"))
        cont-=1