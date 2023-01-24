#Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.

cadena = input("Dame una cadena: ")
 
print(cadena)
 
lista = []
 
for c in cadena:
    if(c not in lista):
        lista.append(c)
 
print(lista)