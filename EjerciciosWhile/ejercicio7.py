JUAN = 915234677
JUANA = 988774455
MARIO = 966332255
MARIA = 987654321
ANTONIO = 912345678
num_tel="nada"
while num_tel!=0:
    num_tel = int (input("Ingrese numero de telefono  (9 digitos) "))

    if 100000000<=num_tel<1000000000: #mayor que 8 digitos y menor que 10
        if num_tel == JUAN:
            CONTACTO= "JUAN"
            print("el numero ingresado corresponde al contacto:", CONTACTO)
        elif num_tel == JUANA:
            CONTACTO= "JUANA"
            print("el numero ingresado corresponde al contacto:", CONTACTO)
        elif num_tel == MARIO:
            CONTACTO= "MARIO"
            print("el numero ingresado corresponde al contacto:", CONTACTO)
        elif num_tel == MARIA:
            CONTACTO = "MARIA"
            print("el numero ingresado corresponde al contacto:", CONTACTO)
        elif num_tel == ANTONIO:
            CONTACTO = "ANTONIO"
            print("el numero ingresado corresponde al contacto:", CONTACTO)
        else:
            print("contacto desconocido")
    else:
        print("No ingreso un número de telefono válido ")
