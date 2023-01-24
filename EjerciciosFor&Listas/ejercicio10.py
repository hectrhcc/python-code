#24 alumnos
rut=["12345678-9", "12345678-7", "123456789-1","12345670-1","98765432-1", "98765430-2", "98765433-4", "12345679-8", "25814736-5", "19376482-5", "74125863-1", "74125892-6", "12312345-8", "12341234-7", "99999999-9", "88888888-8", "42156378-1", "14142578-2","78945612-4", "11111111-1", "22222222-2", "33333333-3", "44444444-4", "55555555-5"]
#5 notas por cada alumno = 120
notas=[5.5, 7.0, 4.4, 3.8, 4.4, 6.5, 6.0, 2.4, 3.9, 5.4, 3.5, 4.0, 5.4, 7.0, 2.4, 5.0, 4.0, 3.4, 6.8, 2.4, 1.5, 4.0, 6.4, 5.8, 3.4, 6.5, 4.0, 5.4, 5.8, 6.4, 3.5, 6.0, 5.4, 2.8, 5.4, 6.5, 6.0, 6.4, 6.8, 5.4, 6.5, 1.0, 2.4, 4.8, 5.4, 5.5, 7.0, 4.4, 3.8, 4.4, 4.5, 5.0, 6.4, 4.8, 3.4, 3.5, 4.0, 3.4, 5.8, 6.4, 6.5, 6.0, 6.4, 4.8, 5.4, 5.2, 5.0, 5.4, 6.8, 2.4, 5.5, 7.0, 4.4, 3.8, 6.4, 6.5, 4.0, 4.7, 2.8, 3.4, 6.5, 3.0, 5.4, 6.8, 4.4, 5.1, 6.2, 4.5, 5.8, 5.4, 5.8, 6.0, 4.1, 2.9, 6.4, 2.5, 4.1, 5.0, 3.9, 2.8, 3.9, 3.7, 5.0, 4.0, 6.8, 6.4, 5.9, 5.0, 4.9, 2.8, 5.4, 3.3, 5.5, 7.0, 4.4, 3.8, 4.4, 6.7, 5.2, 1.8]

cont=0
prom=0
promedio=[]
for i in notas:
    cont+=1
    prom+=i
    if cont%5==0:
        #promedio[cont]= prom/5
        promedio.append(prom/5)
        prom=0
	
mayor=0
menor=notas[0]
who=0
who2=0
n_aprobados=0
n_reprobados=0
for i in promedio:
    if mayor<i:
        mayor=i
        who+=1
    elif menor>i:
        menor=i
        who2+=1
    if i>=4.0:
        n_aprobados+=1
    else:
        n_reprobados+=1
#print("Lista de promedio", promedio)
print("El promedio mas alto:",mayor, " rut:",rut[who])
print("El promedio mas bajo:",menor, " rut:",rut[who2])
print("Cantidad de alumnos aprobados:", n_aprobados)
print("Cantidad de alumnos reprobados:",n_reprobados)