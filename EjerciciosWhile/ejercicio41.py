n=""
contm=0
conth=0
while n!=0:
    rut=int(input("Ingrese su rut sin digito verificador:"))
    if rut==0:break
    elif rut<0 or rut<10000000 or rut>100000000:
        print("rut inválido")
    else:
        sueldo=int(input("Ingrese su sueldo:"))
        sexo=input("Ingrese su sexo 1 mujer y 2 hombre:")
        if sexo =="1":
            sexo="mujer"
            if sueldo>500000:
                contm+=1
        elif sexo=="2":
            sexo="hombre"
            if sueldo<400000:
                    conth+=1
        else:
            print("ingrese un sexo válido")
print("Cantidad mujeres sueldo mayor 500k:",contm )
print("Cantidad hombres sueldo menor 400k:",conth )