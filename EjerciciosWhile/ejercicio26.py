
j=""
j=0 #tiene que tener un valor entero para ser usado
x=int(input("Ingrese el inicio de la sumatoria:"))
i=x
x2=int(input("Ingrese el final de la sumatoria:"))
y=int(input("Ingrese el exponente:"))
while i!=x2+1:
	j+= i**y
	i+=1
print("Sumatoria desde ",x," hasta ",x2, "elevado a",y," :",j )

