PI = 3.141516
opcion =""
while opcion!=5:
	print("Calculo de área y perímetro")
	print("Menu")
	print("====")
	print("1) Círculo ")
	print("2) Cuadrado ")
	print("3) Rectángulo ")
	print("4) Triángulo ")
	print("5) Finalizar ")
	opcion = int(input("Ingrese una opción:"))
	if opcion == 1:
		r = int(input("Ingrese radio del círculo:"))
		perímetro = 2*PI*r
		area = PI *r**2
		print("Perímetro: %.2f" %perímetro)
		print("Area: %.2f" %area)
	elif opcion ==2:
		lado = int(input("Ingrese lado del cuadrado:"))
		perímetro = 4*lado
		area = lado**2
		print("Perímetro: %.2f" %perímetro)
		print("Area: %.2f" %area)
	elif opcion ==3:
		lado1 = int(input("Ingrese lado mayor del rectángulo:"))
		lado2 = int(input("Ingrese lado menor del rectángulo:"))
		perímetro = 2*(lado1+lado2)
		area = lado1*lado2
		print("Perímetro: %.2f" %perímetro)
		print("Area: %.2f" %area)
	elif opcion ==4:
		lado1 = int(input("Ingrese primer lado del triángulo:"))
		lado2 = int(input("Ingrese segundo lado del triángulo:")) #base
		lado3 = int(input("Ingrese tercer lado del triángulo:")) #altura
		perímetro = lado1+lado2+lado3
		s = perímetro/2
		area = (s*(s-lado1)*(s-lado2)*(s-lado3))**(1/2)
		#area = (base*altura)/2
		print("Perímetro: %.2f" %perímetro)
		print("Area: %.2f" %area)
	elif opcion ==5:
		break;
	else:
		print("Ingrese una opción válida")