alto_piso = float(input("Ingrese el alto del piso"))
ancho_piso =float(input("Ingrese el ancho del piso"))
largo_piso = float(input("Ingrese el largo del piso"))
alto_puerta = float(input("Ingrese el alto de la puerta"))
ancho_puerta = float(input("Ingrese el ancho de la puerta"))
alto_ventana = float(input("Ingrese el alto de la ventana"))
radio = float(input("Ingrese el radio del respiradero"))


area_techo = ancho_piso* largo_piso
area_primer_piso = ancho_piso * alto_piso - (ancho_puerta* alto_puerta)
area_segundo_piso=  ancho_piso * alto_piso - ( alto_ventana**2)*4
area_tercer_piso=  ancho_piso * alto_piso - ( alto_ventana**2)*4
area_cuarto_piso=  ancho_piso * alto_piso - ( alto_ventana**2)*4
area_frontal = area_cuarto_piso + area_tercer_piso + area_segundo_piso + area_primer_piso
area_frontal_total =  area_frontal*2
area_costado_primer_piso = largo_piso* alto_piso
area_costado_segundo_piso = largo_piso* alto_piso - ( 3.14* radio**2 )
area_costado_tercer_piso = largo_piso* alto_piso - ( 3.14* radio**2 )
area_costado_cuarto_piso = largo_piso* alto_piso - ( 3.14* radio**2 )
area_costado_total = (area_costado_cuarto_piso + area_costado_tercer_piso + area_costado_segundo_piso + area_costado_primer_piso)*2
area_total_a_pintar = area_costado_total + area_frontal_total + area_techo
cantidad_tarros = round(area_total_a_pintar/ 3)

print("La cantidad de tarros es: " , cantidad_tarros)