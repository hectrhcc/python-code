resultado=""
while resultado!=0:
	resultado = int(input("Ingrese resultado de lanzar un dado de 6 caras:"))
	if resultado==1:
		dado=6
		print("Cara opuesta:", dado)
	elif resultado==2:
		dado=5
		print("Cara opuesta:", dado)
	elif resultado==3:
		dado=4
		print("Cara opuesta:", dado)
	elif resultado==4:
		dado=3
		print("Cara opuesta:", dado)
	elif resultado==5:
		dado=2
		print("Cara opuesta:", dado)
	elif resultado==6:
		dado=1
		print("Cara opuesta:", dado)
	else:
		print("Ingrese un resultado entre 1 y 6 ")