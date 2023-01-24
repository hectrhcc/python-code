opcion =""
while opcion!=4:
	print("Tipos de Triángulo según sus lados")
	print("Menu")
	print("====")
	print("1) Equilatero ")
	print("2) Isósceles ")
	print("3) Escaleno ")
	print("4) Finalizar ")
	opcion = int(input("Ingrese una opción:"))
	if opcion == 1:
		lado = int(input("Ingrese primer lado del triángulo:"))
		perímetro = 3*lado
		print("Perímetro: ",perímetro)
		
	elif opcion ==2:
		lado1 = int(input("Ingrese lado que se repite del triángulo:"))
		lado2 = int(input("Ingrese segundo lado del triángulo:"))
		perímetro = (2*lado1)+lado2
		print("Perímetro: ",perímetro)
		
	elif opcion ==3:
		lado1 = int(input("Ingrese primer lado del triángulo:"))
		lado2 = int(input("Ingrese segundo lado del triángulo:"))
		lado3 = int(input("Ingrese tercer lado del triángulo:"))
		perímetro = lado1+lado2+lado3
		print("Perímetro: ",perímetro)
	elif opcion ==4:
		break;
	else:
		print("Ingrese una opción válida")