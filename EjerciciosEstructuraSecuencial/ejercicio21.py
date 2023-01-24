x=float(input("Ingrese la ganancia de venta en porcentaje :"))
precio_prod=float(input("Ingrese el precio del producto : "))
z=float(input("Ingrese cantidad de dinero : "))
#venta1 = precio_prod*x   #(20k)
venta1 = precio_prod*(x/100)
cant_prod = z / (venta1) #que no es lo mismo que  z/precio_prod*x    
print(round(cant_prod))
#print("%.2f" %cant_prod)