#Programa de binario a octal
#Funcion de binario a decimal
def bin_a_dec(b):
    numero = 0
    cont = 0
    for i in b[::-1]: 
      numero+= int(i)*(2**cont)
      cont+= 1
    return numero
#Funcion de decimal a octal
def decimal_a_octal(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal+= (decimal % 8) * i#1 #10 #100 #1000
        decimal//= int(8)
        i = i * 10;
    return octal;
#programa principal
binario=str(input("Ingrese un número en binario:"))
print("Equivalente número octal : ",decimal_a_octal(bin_a_dec(binario))) 