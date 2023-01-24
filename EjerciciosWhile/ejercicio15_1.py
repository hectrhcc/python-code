resultado=""
while resultado!=0:
	dado =(1,2,3,4,5,6)
	resultado = int(input("Ingrese resultado de lanzar un dado de 6 caras:"))
	if resultado==0:break
	elif resultado not in dado:print("Ingrese un resultado entre 1 y 6")
	elif resultado==1:print("Cara opuesta:", dado[resultado-2])
	elif resultado==2:print("Cara opuesta:", dado[resultado+2])
	elif resultado==3:print("Cara opuesta:", dado[resultado])
	elif resultado==4:print("Cara opuesta:", dado[resultado-2])
	elif resultado==5:print("Cara opuesta:", dado[resultado-4])
	elif resultado==6:print("Cara opuesta:", dado[resultado-6])