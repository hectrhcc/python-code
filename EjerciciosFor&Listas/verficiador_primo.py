def verificador_primo(num):
    if num<2:
        return False
    for i in range(2,num):
        print("i",i)
        if num%i==0:
            return False
    return True

#programa principal

n = int(input("ingrese numero:"))
resultado = verificador_primo(n)
print(resultado)

        