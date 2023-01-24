def Metodoruso(x,y):
    if x>y:
        if y%2==0:#Es par
            while y>=1:
                print(x,int(y))
                x*=2
                y/=2
            return int(x*y)
        
        else: #Es impar
            y-=1
            z=x
            while y>=1:
                print(x,int(y))
                x*=2
                y/=2
            return int(x+z)
    
    else: #y>x => y*2  x/2
        if x%2==0: #Es par
            while x>=1:
                print(int(x),y)
                y*=2
                x/=2
            return int(x*y)
        
        else: #Es impar
            x-=1
            z=y
            while x>=1:
                print(x,y)
                y*=2
                x/=2
            return int(z+y)

print("Este programa realiza el Método Ruso de multiplicación")
num1=int(input("Ingresa un número:"))
num2=int(input("Ingresa otro número:"))
print("Resultado:",Metodoruso(num1,num2))