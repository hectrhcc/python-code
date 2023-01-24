n=""
while n!=0:
    rut=input("Ingrese rut alumno:")
    if rut=="0":break
    elif len(rut)>10:
        print("rut inválido")
    else:
        nota1=float(input("Ingrese nota de materia 1:"))
        nota2=float(input("Ingrese nota de materia 2:"))
        nota3=float(input("Ingrese nota de materia 3:"))
        nota4=float(input("Ingrese nota de materia 4:"))
        nota5=float(input("Ingrese nota de materia 5:"))
        nota6=float(input("Ingrese nota de materia 6:"))
        prom= (nota1+nota2+nota3+nota3+nota4+nota5+nota6)/6
        if prom<4: print("El alumno cuyo rut es", rut,"obtuvo de promedio un",prom," por lo que reprobo la asignatura")
        else:print("El alumno cuyo rut es", rut,"obtuvo de promedio un",prom," por lo que aprobo la asignatura")