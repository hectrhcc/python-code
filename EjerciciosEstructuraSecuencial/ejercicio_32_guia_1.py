#Datos de entrada
percent_reprob_a = float(input("El porcentaje de alumnos reprobados del curso A :"))
percent_aprob_b = float(input("El porcentaje de aprobados del curso B :"))

#a
num_alum_reprob_a = int( (percent_reprob_a*60)/100)


num_alum_aprob_b = int ((percent_aprob_b* 20)/100)

#b

num_alum_reprob_b = 20 - num_alum_aprob_b


#c
num_total_alum_reprob =  num_alum_reprob_b + num_alum_reprob_a
percent_reprob_ab =  (num_total_alum_reprob *100) / 80

#d
num_alum_aprob_a = 60 - num_alum_reprob_a
num_total_alum_aprob =  num_alum_aprob_b + num_alum_aprob_a

#Salida de datos
print(" El número de alumnos reprobados del curso A: ", num_alum_reprob_a )
print(" El número de alumnos reprobados del curso B: ", num_alum_reprob_b )
print(" El porcentaje de alumnos reprobados en relacion a los 2 cursos: %.2f" %percent_reprob_ab )
print(" El numero total de alumnos aprobados: ", num_total_alum_aprob)
