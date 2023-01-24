ciudad_o = "origen"
ciudad_d = "destino"
while ciudad_o!=ciudad_d:
	lista_ciudades = ('arica', 'iquique', 'antofagasta', 'calama', 'tocopilla')
	ciudad_o = input("Ingrese ciudad de origen:")
	ciudad_d = input("Ingrese ciudad de destino:")	
	if ciudad_o and ciudad_d not in lista_ciudades:print("Ingrese una ciudad válida")
	#Arica
	elif  ciudad_o =="arica" and ciudad_d=="iquique":print("La distancia entre Arica y Iquique es de 195 km. La distancia por carretera es de 312.4 km.")
	elif ciudad_o =="arica" and ciudad_d=="antofagasta":print("La distancia entre Arica y Antofagasta es de  575 km . La distancia por carretera es de 717 km.")
	elif ciudad_o =="arica" and ciudad_d=="calama":print("La distancia entre Arica y Calama es de   465 km  . La distancia por carretera es de  577 km.")
	elif ciudad_o =="arica" and ciudad_d=="tocopilla":print("La distancia entre Arica y Tocopilla es de   399,96 km . La distancia por carretera es de  537,54 km.")
	#Iquique
	elif ciudad_o =="iquique" and ciudad_d=="arica":print("La distancia entre Iquique  y Arica es de 195 km. La distancia por carretera es de 312.4 km.")
	elif ciudad_o =="iquique" and ciudad_d=="antofagasta":print("La distancia entre Iquique  y antofagasta es de 382,66 km. La distancia por carretera es de 417,88 km.")
	elif ciudad_o =="iquique" and ciudad_d=="calama":print("La distancia entre Iquique  y calama es de 279,20 km. La distancia por carretera es de 385,85 km.")
	elif ciudad_o =="iquique" and ciudad_d=="tocopilla":print("La distancia entre Iquique  y tocopilla es de 207,08 km. La distancia por carretera es de 229,39 km.")
	#Antofagasta
	elif ciudad_o =="antofagasta" and ciudad_d=="arica":print("La distancia entre Antofagasta y Arica es de  575 km . La distancia por carretera es de 717 km.")
	elif ciudad_o =="antofagasta" and ciudad_d=="iquique":print("La distancia entre Antofagasta y iquique es de  382,66 km . La distancia por carretera es de 417,88 km.")
	elif ciudad_o =="antofagasta" and ciudad_d=="calama":print("La distancia entre Antofagasta y calama es de  200,24 km . La distancia por carretera es de 215,36 km.")
	elif ciudad_o =="antofagasta" and ciudad_d=="tocopilla":print("La distancia entre Antofagasta y tocopilla es de  174,74 km . La distancia por carretera es de 187,68 km.")
	#Calama
	elif ciudad_o =="calama" and ciudad_d=="arica":print("La distancia entre Calama y Arica es de   465 km  . La distancia por carretera es de  577 km.")
	elif ciudad_o =="calama" and ciudad_d=="iquique":print("La distancia entre calama y Iquique es de 279,20 km. La distancia por carretera es de 385,85 km.")
	elif ciudad_o =="calama" and ciudad_d=="antofagasta":print("La distancia entre calama y antofagasta es de  200,24 km . La distancia por carretera es de 215,36 km.")
	elif ciudad_o =="calama" and ciudad_d=="tocopilla":print("La distancia entre calama y tocopilla es de 137,13 km . La distancia por carretera es de 159,34 km.")
	#Tocopilla
	elif ciudad_o =="tocopilla" and ciudad_d=="arica":print("La distancia entre Tocopilla y Arica es de   399,96 km . La distancia por carretera es de  537,54 km.")
	elif ciudad_o =="tocopilla" and ciudad_d=="iquique":print("La distancia entre tocopilla e Iquique  es de 207,08 km. La distancia por carretera es de 229,39 km.")
	elif ciudad_o =="tocopilla" and ciudad_d=="antofagasta":print("La distancia entre tocopilla y Antofagasta  es de  174,74 km . La distancia por carretera es de 187,68 km.")
	elif ciudad_o =="tocopilla" and ciudad_d=="calama":print("La distancia entre tocopilla y calama es de 137,13 km . La distancia por carretera es de 159,34 km.")
	elif ciudad_o == ciudad_d:break