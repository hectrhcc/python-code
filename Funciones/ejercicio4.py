def metodoruso(x,y):
    if x>y:
        if y%2==0:
            print(x,int(y))
            while y>1:#cuando llega a 1 termina
                x*=2
                y/=2
                print(x,int(y))
            return int(x*y)
        else:
            y-=1
            z=x
            print(x,int(y))
            while y>1:#cuando llega a 1 termina
                x*=2
                y/=2
                print(x,int(y))
        return int(x+z)
    else:
        if x%2==0:
            print(int(x),y)
            while x>1:#cuando llega a 1 termina
                y*=2
                x/=2
                print(int(x),y)
            return int(x*y)
        else:
            x-=1
            z=y
            print(int(x),y)
            while x>1:
                y*=2
                x/=2
                print(int(x),y)
            return int(y+z)
    #return int(x*y)

print("Este progarma realiza el Método ruso de multiplicación")
num1=int(input("Ingrese un número:"))
num2=int(input("Ingrese otro número:"))
print("Resultado:",metodoruso(num1,num2))