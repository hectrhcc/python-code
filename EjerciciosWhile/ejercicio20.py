Solicite una fecha (día, mes y año) y muestre si es una fecha correcta o no. Para que una fecha sea correcta considere que un año tiene 12 meses, el número de días depende del mes (31 días para enero, marzo, mayo, julio, agosto, octubre y diciembre; 30 días para abril, junio, septiembre y noviembre), en el caso de febrero, el número de día depende además de si el año es bisiesto (29 días) o no (28 días). Recordar que son bisiestos todos los años múltiplos de 4, excepto aquellos que son múltiplos de 100 pero no de 400. Debe finalizar si se ingresa 0 en el número del mes.

mes=""
while mes!=0:
	dd = int(input("Ingrese un día:"))
	mm = input("Ingrese un mes:")
	yyyy = int(input("Ingrese un año:"))

	if yyyy>0:
		if ((yyyy %400) ==0) or ((yyyy %100) !=0 and (año%4) ==0):
			print("Es un año bisiesto")
		else:
			print("No es un año bisiesto")
		#if 0<mm<=12:
			if dd==31:
				if mm in ('enero', )
		else:
			print("Ingrese un mes válido")

	else:
		print("Ingrese un año válido")