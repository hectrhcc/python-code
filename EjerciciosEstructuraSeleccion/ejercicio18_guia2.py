aaaa=int(input("Ingrese su año de nacimiento :"))
mm=int(input("Ingrese su mes de nacimiento :"))
dd=int(input("Ingrese su dia de nacimiento :"))
#datos actuales
ma=int(input("Ingrese mes actual :"))
da=int(input("Ingrese dia actual :"))

if 0<aaaa < 2020:
    if 0<mm <13:
        if 0<dd <32:
            año = 2020 -aaaa  # 23
            mes = ma - mm  # -1
            dia = da - dd  # cambiar a 27 o 29
            if mes <0: #and dia<0: #separarlo con un elif
                print("la edad de la persona en años es " , (año-1), "años ") #, 12 + mes, " meses", 30 + dia, "dias" )
            elif mes == 0 and dia <0:
                print("la edad de la persona en años es " , año-1, "años ")
            else:
                print("la edad de la persona en años es " , año, "años ") #, (5 -mm)*-1 , " meses", (22 -dd)*-1, "dias" )            
        else:
            print("seguro que naciste ese dia? ")
    else:
        print("seguro que naciste ese mes? ")
else:
    print("seguro que tienes esa edad? ")
