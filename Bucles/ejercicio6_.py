#Solicitar numero extremo inferior
#solicitar numero extremo superior
#solicitar numero
#Mientras numero extremo inferior no sea igual al numero extremo superior 
#Si es multiplo del numero ingresado entonces
#Mostrar los multiplos del numero
#incrementar el numero extremo inferior en uno

num_inf = int(input("Ingresa extremo inferior:"))
num_sup = int(input("Ingresa extremo superior:"))
num = int(input("Ingresar un numero: "))

if num >0 and num_inf>0 and num_sup> 0:
    while num_inf!=num_sup+1:
        if num_inf % num == 0:
            print("Multiplos de ", num, " = ",num_inf)
        num_inf+=1
else:
    print("Ingrese un numero positivo ")
