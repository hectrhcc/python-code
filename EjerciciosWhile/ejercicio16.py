opcion=""
while opcion!=7:
	print("Menu")
	print("====")
	print("1) Simple")
	print("2) Simple Superior")
	print("3) Matrimonial")
	print("4) Matrimonial Superior")
	print("5) Doble")
	print("6) Doble Superior")
	print("7) Finalizar")	
	if opcion==1:
		precio=5000 
		print("El valor por noche es de:", precio)
		nnoches=int(input("Ingrese numero de noches:"))
		cobro= precio*nnoches+precio*nnoches*0.19
		print("Total a pagar:", cobro)
	elif opcion ==2:
		precio=8000
		cobro= precio*nnoches+precio*nnoches*0.19
		print("El valor por noche es de:", precio)
		nnoches=int(input("Ingrese numero de noches:"))
		cobro= precio*nnoches+precio*nnoches*0.19
		print("Total a pagar:", cobro)
	elif opcion ==3:
		precio=12000
		print("El valor por noche es de:", precio)
		nnoches=int(input("Ingrese numero de noches:"))
		cobro= precio*nnoches+precio*nnoches*0.19
		print("Total a pagar:", cobro)
	elif opcion ==4:
		precio=16000
		print("El valor por noche es de:", precio)
		nnoches=int(input("Ingrese numero de noches:"))
		cobro= precio*nnoches+precio*nnoches*0.19
		print("Total a pagar:", cobro)
	elif opcion ==5:
		precio=20000
		print("El valor por noche es de:", precio)
		nnoches=int(input("Ingrese numero de noches:"))
		cobro= precio*nnoches+precio*nnoches*0.19
		print("Total a pagar:", cobro)
	elif opcion ==6:
		precio=25000
		print("El valor por noche es de:", precio)
		nnoches=int(input("Ingrese numero de noches:"))
		cobro= precio*nnoches+precio*nnoches*0.19
		print("Total a pagar:", cobro)
	else:
		print("Ingrese una opción válida")