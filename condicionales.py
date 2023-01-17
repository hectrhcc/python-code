
respuesta = str(input("¿Quiere una pizza vegetariana? responda solo con si o no:"))
if (respuesta=="si"):
	pizza ="vegetariana"
	print("ingredientes disponibles: \n1-Pimiento\n2-Tofu")
	ingrediente=int(input("Ingrese el numero del ingrediente:"))
	if (ingrediente==1):
		ing= "pimiento"
	else:	
		ing = "tofu"
else:
	respuesta="no"
	pizza = "no vegetariana"
	print("ingredientes disponibles: \n1-Peperoni\n2-Jamon\n3-Salmon")
	ingrediente=int(input("Ingrese el numero del ingrediente:"))
	if (ingrediente==1):
	 	ing= "peperoni"
	elif (ingrediente==2):	
		ing = "jamon"
	else:
		ing = "salmon"

print("La pizza seleccionada es",pizza ," y el ingrediente es:\n",ing ,",tomate y mozzarrella")

