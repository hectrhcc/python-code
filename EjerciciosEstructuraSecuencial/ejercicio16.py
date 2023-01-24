ancho = int(input ("Ingrese el ancho del rectangulo:"))
largo = int(input ("Ingrese el largo del rectangulo:"))

perimetro = 2 * (ancho + largo)
area = ancho*largo
diagonal = ( ancho**2 + largo**2)**(1/2)

print("El perimetro es:" , perimetro)
print("El area es: ", area)
print("La diagonal es: ", diagonal)