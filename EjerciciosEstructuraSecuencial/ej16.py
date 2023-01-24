#Escribir “Ingrese un valor para el ancho del rectangulo”
#Leer ancho
#Escribir “Ingrese un valor para el largo del rectangulo”
#Leer largo

#perimetro = (ancho +largo)*2
#area = ancho * largo
#diagonal = (ancho**2 +largo**2)** (½)

ancho = int(input("Ingrese el ancho del rectangulo: "))
largo = int(input("Ingrese el largo del rectangulo: "))

perimetro = (largo +ancho) *2
area = ancho * largo
diagonal = (ancho**2+largo**2)**(1/2)

print("El resultado del perimetro", perimetro)
print("El resultado del area", area)
print("El resultado del diagonal %.2f" %diagonal)
      