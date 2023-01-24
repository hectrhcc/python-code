def factoria(n):
    factorial=1 #reinicio para que no acumule los factoriales pasados
    while n:
        factorial*=n #8*7*6*5*4*3*2*1
        n-=1
    return factorial
        
n=""
factorial=1
while n!=-1:
    n=int(input("Ingrese un numero para obtener su factorial:"))
    if n==-1: break
    print("El factorial es:",factoria(n))