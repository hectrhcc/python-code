num ="nada"
while num !=0:
    num =int(input("Ingresar un valor: "))
    if num>0:
        suma=0
        num2 = num
        while num2: # descomponer el numero en digitos
            digito = num2 % 10
            num2 //= 10
            suma+= digito
        #print("la suma es", suma)
        if suma % 2 == 0:
            print("la suma es par")
        else:
            print("la suma es impar")