porcentaje_reprob_a = float(input("Ingresa porcentaje de reprobados de A"))
porcentaje_aprob_b = float(input("Ingresa porcentaje de aprobados de B"))

# A = 60 = 100%
# B = 20  = 100%
# 80 = 100%

num_alum_reprob_a = int ((porcentaje_reprob_a *60) / 100)
num_alum_aprob_a = int (60 - num_alum_reprob_a)

num_alum_aprob_b = int ((porcentaje_aprob_b*20 )/100)

num_alum_reprob_b = 20 - num_alum_aprob_b

num_alum_reprob_total = num_alum_reprob_a + num_alum_reprob_b

porcent_reprob_total = (num_alum_reprob_total * 100)/80

num_alum_aprob_total = num_alum_aprob_a + num_alum_aprob_b

print("El numero de alumnos reprobados de A:", num_alum_reprob_a)
print("El numero de alumnos reprobados de B:", num_alum_reprob_b  )
print("El porcentaje de reprobados en relacion a los 2 cursos %.2f" %porcent_reprob_total )
print("Numero total de alumnos aprobados", num_alum_aprob_total   )
                           