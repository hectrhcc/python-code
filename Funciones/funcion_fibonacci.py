#FUNCION FIBONACCI
def fibonacci(n):
    a=0 #valor inicial
    b=1 #valor inicial
    for k in range(n): #desde 0 hasta n-1
        c = a + b #1  #2 #3
        a = b     #1  #1 #2
        b = c     #1  #2 #3
    return b# 1er termino=0 .. 2do termino=1  3er termino = 1 4to termino=2
#PROGRAMA PRINCIPAL
n=int(input("Ingrese el número de término de la sucesión de fibonacci:"))
for x in range(n): # n°de terminos x va desde 0 hasta n-1
    print(fibonacci(x))