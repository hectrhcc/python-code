def Primo(num):
    if num==0 or num==1:
        return False
    x=2
    while x<num:
        if num % x==0:
            return False
        x+=1
    return True
     
print("Determina si un número es primo o no:")
n=int(input("Ingresar un numero:"))
print(Primo(n))