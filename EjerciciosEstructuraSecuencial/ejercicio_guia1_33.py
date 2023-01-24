#Ingreso de datos
valor_alto_piso = float(input("Ingrese valor para el alto del piso:"))
valor_ancho_piso  = float(input("Ingrese valor para el ancho del piso:"))
valor_largo_piso  = float(input("Ingrese valor para el largo del piso:"))
valor_alto_puerta  = float(input("Ingrese valor para el alto de la puerta:"))
valor_ancho_puerta  = float(input("Ingrese valor para el ancho de la puerta:"))
valor_alto_ventana  = float(input("Ingrese valor para alto de la ventana:"))
valor_radio_respiradero  = float(input("Ingrese valor para el radio del respiradero:"))
 
#Calculo de las areas
#Parte frontal
area_piso1_frontal = valor_ancho_piso * valor_alto_piso - ( valor_ancho_puerta*valor_alto_puerta)
area_piso2_frontal =  valor_ancho_piso * valor_alto_piso - ( valor_alto_ventana**2)*4
area_piso3_frontal =  valor_ancho_piso * valor_alto_piso - ( valor_alto_ventana**2)*4
area_piso4_frontal =  valor_ancho_piso * valor_alto_piso - ( valor_alto_ventana**2)*4

area_total_frontal_atras = (area_piso1_frontal + area_piso2_frontal + area_piso3_frontal + area_piso4_frontal) *2

#Techo
area_techo = valor_ancho_piso * valor_largo_piso
 
#Costado
area_lado_piso1 = valor_largo_piso * valor_alto_piso
area_lado_piso2 = valor_largo_piso * valor_alto_piso - ( 3.1415* valor_radio_respiradero**2 )
area_lado_piso3 = valor_largo_piso * valor_alto_piso - ( 3.1415* valor_radio_respiradero**2 )
area_lado_piso4 = valor_largo_piso * valor_alto_piso - ( 3.1415* valor_radio_respiradero**2 )
area_costado_total = (area_lado_piso4 + area_lado_piso3 + area_lado_piso2 + area_lado_piso1) *2

area_total_edificio = area_costado_total + area_techo + area_total_frontal_atras
cantidad_tarros = round(area_total_edificio/3)
print("La cantidad de tarros es: ", cantidad_tarros)