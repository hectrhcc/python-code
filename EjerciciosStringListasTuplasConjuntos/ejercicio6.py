#Pide una cadena por teclado, mete los caracteres en una lista sin espacios

cadena = input("Dame una cadena: ")
 
print(cadena)
 
lista = []
 
for c in cadena:
    if(c != ' '):
        lista.append(c)
 
print(lista)