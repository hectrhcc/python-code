i=1
j=0
x=int(input("Ingrese N primeros números a sumar:"))
y=int(input("Ingrese un número para sumar los multiplos que tiene:"))
while i!=x+1:
    if i%y ==0:
        j+=i
    i+=1
print("La suma de los primeros", x, "números multiplos de", y,"es:",j)