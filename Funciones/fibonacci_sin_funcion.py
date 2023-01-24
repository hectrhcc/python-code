#fibonacci
n=int(input("Ingresa un termino para la sucesión de fibonacci:"))
a=0
b=1
cont=0
for i in range(cont):
    #print(a)#toma los valores iniciales de la sucesion
    c = a +b
    a = b
    b = c
cont+=1
print(a)# equivale en la funcion al return para que funcione aqui
#para que funcione con el print en la linea anterior el for no se tiene que ejecutar la primera vez cosa que a tome el valor 0