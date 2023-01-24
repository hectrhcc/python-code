n=1
num=""
while num!=0:
    num=int(input("Ingrese un número entero:"))
    if num==0:break
    print("La tabla de multiplicar:")
    n=1
    while n!=13:
        m=num*n
        print(num, " *",n,"=", m)
        n+=1