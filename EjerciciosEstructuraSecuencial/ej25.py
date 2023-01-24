nota_trabajo1 =float(input("Ingrese nota de trabajo 1: "))
nota_trabajo2 =float(input("Ingrese nota de trabajo 2: "))
nota_trabajo3 =float(input("Ingrese nota de trabajo 3: "))
nota_trabajo4 =float(input("Ingrese nota de trabajo 4: "))
nota_trabajo5 =float(input("Ingrese nota de trabajo 5: "))
nota_trabajo6 =float(input("Ingrese nota de trabajo 6: "))
nota_participacion =float(input("Ingrese nota de participación: "))

#promedio = nota_trabajo1 *0.10 + nota_trabajo2 *0.10 + nota_trabajo3 *0.10 + nota_trabajo4 *0.10 + nota_trabajo5 *0.10 + nota_trabajo6 *0.10 + nota_participación *0.10 + nota_pro *0.30

#nota_pro = 4 - (nota_trabajo1 *0.10 + nota_trabajo2 *0.10 + nota_trabajo3 *0.10 + nota_trabajo4 *0.10 
#                                  + nota_trabajo5 *0.10 + nota_trabajo6 *0.10 + nota_participación *0.10)


nota_minima_proyecto_final =  ( 4 - (nota_trabajo1 *0.10 + nota_trabajo2 *0.10 + nota_trabajo3 *0.10 + nota_trabajo4 *0.10 + nota_trabajo5 *0.10 + nota_trabajo6 *0.10 + nota_participacion *0.10)) /0.30


print("La nota minima del proyecto final es: %.2f" %nota_minima_proyecto_final)