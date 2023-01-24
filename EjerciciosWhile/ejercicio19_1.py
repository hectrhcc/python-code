ciudad_o = "origen"
ciudad_d = "destino"
while ciudad_o!=ciudad_d:
	lista_ciudades = ('arica', 'iquique', 'antofagasta', 'calama', 'tocopilla')
	distancia = ('195 km','575 km',' 465 km','399,96 km','382,66 km',' 279,20 km','207,08 km','200,24 km','174,74 km','137,13 km')
	ciudad_o = input("Ingrese ciudad de origen:")
	ciudad_d = input("Ingrese ciudad de destino:")	
	if ciudad_o == ciudad_d:break
	elif ciudad_o.lower() and ciudad_d.lower() not in lista_ciudades:print("Ingrese una ciudad válida")
	#Arica
	i=4
	while i!=-1:
            if ciudad_o==lista_ciudades[0] and ciudad_d == lista_ciudades[i]: print(distancia[i-1])
            #Iquique
            if ciudad_o==lista_ciudades[1] and ciudad_d == lista_ciudades[i]: print(distancia[i+2])
            i-=1
			
	#if ciudad_o =="iquique" and ciudad_d=="arica":print(distancia[0])
	#elif ciudad_o =="iquique" and ciudad_d=="antofagasta":print(distancia[4])
	#elif ciudad_o =="iquique" and ciudad_d=="calama":print(distancia[5])
	#elif ciudad_o =="iquique" and ciudad_d=="tocopilla":print(distancia[6])
	#Antofagasta
	if ciudad_o =="antofagasta" and ciudad_d=="arica":print(distancia[1])
	elif ciudad_o =="antofagasta" and ciudad_d=="iquique":print(distancia[4])
	elif ciudad_o =="antofagasta" and ciudad_d=="calama":print(distancia[7])
	elif ciudad_o =="antofagasta" and ciudad_d=="tocopilla":print(distancia[8])
	#Calama
	elif ciudad_o =="calama" and ciudad_d=="arica":print(distancia[2])
	elif ciudad_o =="calama" and ciudad_d=="iquique":print(distancia[5])
	elif ciudad_o =="calama" and ciudad_d=="antofagasta":print(distancia[7])
	elif ciudad_o =="calama" and ciudad_d=="tocopilla":print(distancia[9])
	#Tocopilla
	elif ciudad_o =="tocopilla" and ciudad_d=="arica":print(distancia[3])
	elif ciudad_o =="tocopilla" and ciudad_d=="iquique":print(distancia[6])
	elif ciudad_o =="tocopilla" and ciudad_d=="antofagasta":print(distancia[8])
	elif ciudad_o =="tocopilla" and ciudad_d=="calama":print(distancia[9])