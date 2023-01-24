#Mientras  numero sea distinto de 136 hacer
#Si el numero es multiplo de 3 y de 5 entonces
#Mostrar el numero partiendo desde el 15

num = 15
while num!=136:
    if num % 3 == 0 and num % 5 == 0:
        print("Multiplo de 3 y 5 :", num)
    num+=1
