#definición de la funcion
def fibonacci(x):
    a=0
    b=1
    cont=0
    for i in range(x):#se repite x veces
        #print(a)
        c = a + b
        a = b
        b = c
        cont=cont+1
        #print("a",a)
        #print("b",b)
        #print("c",c)
        #print("cont",cont)
    return a #termina la iteracion y muestra a

#programa principal
n=int(input("Ingresar un número para la sucesión de fibonacci:"))
cont0=0
for i in range(n): #rango de terminos
#    cont0=cont0+1
#    print("cont0",cont0)
    print(fibonacci(i)) #tenia n y si es n el valor nunca comienza con los valores iniciales de fibonacci
#CONCLUSION: pasandole un valor n en el for de la funcion itera n veces y como el return esta fuera del for cuando termina de iterar las n veces a pierde los valores iniciales y queda con los finales
#por eso que se arregla con un simple print al comienzo asi se muestra todos los valores iniciales de la sucesion de fibanacci, gracias al print al comienzo del for ahi se ve que con un for es suficiente
#el tema esta con el return que esta fuera del bucle y por lo tanto se pierden los valores que toma a osea el comienzo de la sucesion de fibonacci
#si vamos a trabajar con return hay que pasarle a la funcion los valores desde el inicio, como le paso n return nunca pesca el cero por eso tengo que pasarle i en vez de n para que asi return pesque las primeros valores de la sucesion