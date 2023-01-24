#ingreso de datos
cant_nulo=int(input("Ingrese numero de votos nulos"))
cant_blanco=int(input("Ingrese numero de votos blancos"))
cant_valido=int(input("Ingrese numero de votos válidos"))


#calculo
cant_total = cant_nulo+cant_blanco+cant_valido
porcent_nulo=cant_nulo*100/cant_total 
porcent_blanco=cant_blanco*100/cant_total 
porcent_valido=cant_valido*100/cant_total 

#salida de datos
print("Votos totales = ",cant_total )
print("El porcentaje de votos nulos = %.2f" %porcent_nulo, "%" )
print("El porcentaje de votos blancos = %.2f" %porcent_blanco, "%" )
print("El porcentaje de votos validos = %.2f" %porcent_valido, "%" )